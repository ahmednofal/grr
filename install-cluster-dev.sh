#!/bin/bash

ndb_mgmd_config="[ndbd default]
# Options affecting ndbd processes on all data nodes:
NoOfReplicas=2  # Number of replicas
MaxNoOfTriggers = 3000
MaxNoOfOrderedIndexes = 2000
MaxNoOfAttributes = 20000
MaxNoOfTables = 4096
DataMemory = 1G
MaxBufferedEpochBytes = 26214400
MaxBufferedEpochs = 100
MaxNoOfExecutionThreads = 2
MaxNoOfConcurrentOperations = 32768
MinDiskWriteSpeed = 10M
FragmentLogFileSize = 16M
NoOfFragmentLogFiles = 16
NoOfFragmentLogParts = 4
LockPagesInMainMemory = 0 

[ndb_mgmd]
# Management process options:
hostname=localhost # Hostname of the manager
datadir=/var/lib/mysql-cluster  # Directory for the log files

[ndbd]
hostname=localhost # Hostname/IP of the first data node
NodeId=2            # Node ID for this data node
datadir=/usr/local/mysql/data   # Remote directory for the data files

[ndbd]
hostname=localhost # Hostname/IP of the second data node
NodeId=3            # Node ID for this data node
datadir=/usr/local/mysql/data   # Remote directory for the data files

[mysqld]
# SQL node options:
hostname=localhost # In our case the MySQL server/client is on the same Droplet as the cluster manager"

nbd_mgmd_service="[Unit]
Description=MySQL NDB Cluster Management Server
After=network.target auditd.service

[Service]
Type=forking
ExecStart=/usr/sbin/ndb_mgmd -f /var/lib/mysql-cluster/config.ini
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=on-failure

[Install]
WantedBy=multi-user.target"

ndbd_config="[mysqld]
# Options for mysqld process:
ndbcluster                      # run NDB storage engine

[mysql_cluster]
# Options for NDB Cluster processes:
ndb-connectstring=\"localhost\"  # location of management server"

ndbd_service="[Unit]
Description=MySQL NDB Data Node Daemon
After=network.target auditd.service

[Service]
Type=forking
ExecStart=/usr/sbin/ndbd
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=on-failure

[Install]
WantedBy=multi-user.target"

mysqld_config="[mysqld]
# Options for mysqld process:
ndbcluster                      # run NDB storage engine

[mysql_cluster]
# Options for NDB Cluster processes:
ndb-connectstring=localhost  # location of management server"

function remove_mysql {
    sudo service mysql stop;
    sudo killall -KILL mysql mysqld_safe mysqld;
    sudo apt --yes purge mysql-server mysql-client mysql-common dbndb_mgmd_config-mysql;
    sudo apt --yes autoremove --purge;
    sudo apt autoclean;
    sudo deluser --remove-home mysql;
    sudo delgroup mysql;
    sudo rm -rf /etc/mysql;
    sudo rm -rf /var/lib/mysql;
    sudo rm -rf /var/log/mysql;
    sudo rm -rf /etc/apparmor.d/abstractions/mysql /etc/apparmor.d/cache/usr.sbin.mysqld /etc/mysql /var/lib/mysql /var/log/mysql* /var/log/upstart/mysql.log* /var/run/mysqld;
    sudo updatedb;
}

function install_cluster_ubuntu {
    sudo apt update -qq;
    sudo apt install libclass-methodmaker-perl libaio1 libmecab2;
    sudo dpkg -i mysql-cluster-community-management-server_8.0.16-dmr-1ubuntu18.04_amd64.deb;
    sudo dpkg -i mysql-cluster-community-data-node_8.0.16-dmr-1ubuntu18.04_amd64.deb;
    sudo dpkg -i mysql-common_8.0.16-dmr-1ubuntu18.04_amd64.deb;
    sudo dpkg -i mysql-cluster-community-client-core_8.0.16-dmr-1ubuntu18.04_amd64.deb;
    sudo dpkg -i mysql-cluster-community-client_8.0.16-dmr-1ubuntu18.04_amd64.deb;
    sudo dpkg -i mysql-client_8.0.16-dmr-1ubuntu18.04_amd64.deb;
    sudo dpkg -i mysql-cluster-community-server-core_8.0.16-dmr-1ubuntu18.04_amd64.deb;
    sudo dpkg -i mysql-cluster-community-server_8.0.16-dmr-1ubuntu18.04_amd64.deb;
    sudo dpkg -i mysql-server_8.0.16-dmr-1ubuntu18.04_amd64.deb;
}

function install_cluster_debian {
    sudo apt update -qq;
    sudo apt install libclass-methodmaker-perl libaio1 libmecab2;
    sudo dpkg -i mysql-cluster-community-management-server_8.0.16-dmr-1debian9_amd64.deb;
    sudo dpkg -i mysql-cluster-community-data-node_8.0.16-dmr-1debian9_amd64.deb;
    sudo dpkg -i mysql-cluster-community-client-core_8.0.16-dmr-1debian9_amd64.deb;
    sudo dpkg -i mysql-cluster-community-client_8.0.16-dmr-1debian9_amd64.deb;
    sudo dpkg -i mysql-cluster-community-server-core_8.0.16-dmr-1debian9_amd64.deb;
    sudo dpkg -i mysql-cluster-community-server_8.0.16-dmr-1debian9_amd64.deb;
}

function install_cluster_common {
    sudo mkdir -p /var/lib/mysql-cluster;
    sudo mv /var/lib/mysql-cluster/config.ini /var/lib/mysql-cluster/config.ini.bak 2> /dev/null;
    sudo touch /var/lib/mysql-cluster/config.ini && sudo echo -e $ndb_mgmd_config >> /var/lib/mysql-cluster/config.ini;
    sudo touch /etc/my.cnf && sudo echo $ndbd_config >> /etc/my.cnf;
    sudo mkdir -p /usr/local/mysql/data;
    sudo echo -e $mysqld_config >> /etc/mysql/my.cnf;
    sudo systemctl restart mysql;
    sudo systemctl enable mysql;
}

function install_systemd {
    sudo touch /etc/systemd/system/ndb_mgmd.service && sudo echo -e $nbd_mgmd_service >> /etc/systemd/system/ndb_mgmd.service;
    sudo touch /etc/systemd/system/ndbd.service && sudo echo -e $ndbd_service >> /etc/systemd/system/ndbd.service;
    sudo systemctl daemon-reload;
    sudo systemctl enable ndb_mgmd;
    sudo systemctl start ndb_mgmd;
    sudo systemctl enable ndbd;
    sudo systemctl start ndbd;
}

function start_cluster {
    sudo ndb_mgmd --initial -f /var/lib/mysql-cluster/config.ini;
    sudo ndbd;
    sudo ndbd;
}

cd ~
mkdir mysql_cluster && cd mysql_cluster

echo "Which distribution are you on?"
options=("Ubuntu 18.04 x64" "Debian 9")
PS3=':'
select opt in "${options[@]}"
do
    case $opt in
        "Ubuntu 18.04 x64")
            echo "Downloading from https://dev.mysql.com/get/Downloads/MySQL-Cluster-8.0/mysql-cluster_8.0.16-dmr-1ubuntu18.04_amd64.deb-bundle.tar";
            download="https://dev.mysql.com/get/Downloads/MySQL-Cluster-8.0/mysql-cluster_8.0.16-dmr-1ubuntu18.04_amd64.deb-bundle.tar";
            option=1;
            break;;
        "Debian 9")
            echo "Downloading from https://dev.mysql.com/get/Downloads/MySQL-Cluster-8.0/mysql-cluster_8.0.16-dmr-1debian9_amd64.deb-bundle.tar";
            download="https://dev.mysql.com/get/Downloads/MySQL-Cluster-8.0/mysql-cluster_8.0.16-dmr-1debian9_amd64.deb-bundle.tar";
            option=2;
            break;;
        *) echo "invalid option $REPLY";;
    esac
done

echo "Do you want to destroy existing mysql installation in its entirety?
This is an extremely destructive operation and very dangerous but it's best to do it guarantee correct operation of the cluster, it will however cause issues for other programs but all resolvable by installing some dependencies."
select yn in "Yes" "No"; do
    case $yn in
        Yes)
            remove_mysql;
            break;;
        No)
            break;;
        *) echo "invalid option $REPLY";;
    esac
done

wget --no-check-certificate $download -O bundle.tar
tar -xvf bundle.tar -C install/
cd install

case $option in
    1)
        install_cluster_ubuntu;
        break;;
    2)
        install_cluster_debian;
        break;;
esac
install_cluster_common;

echo "How do you want database to operate?"
options=("Systemd service (auto start at boot)" "I'll start on my own each time [Recommended for RAM concerns]")
PS3=':'
select opt in "${options[@]}"
do
    case $opt in
        "Systemd service (auto start at boot)")
            install_systemd;
            break;;
        "I'll start on my own each time [Recommended for RAM concerns]")
            start_cluster;
            break;;
        *) echo "invalid option $REPLY";;
    esac
done

echo "Congratulations! MySQL Cluster Community Server 8.0.16 dmr is now installed on your machine. If anything is broken, such is life :/"
echo "To confirm installation please follow these instructions:"
echo "shell> mysql -u root -p"
echo "This should bring up MySQL monitor and the greeting should include \"Server version: 8.0.16-cluster MySQL Cluster Community Server - GPL\", if not then you should have probably picked to destroy existing mysql deployment, you can rerun with that option."
echo "mysql> SHOW ENGINE NDB STATUS \G"
echo "This should bring up a set of rows, the first row should have some cluster information with the Type: ndbcluster or ndbclu"
echo "shell> ndb_mgb"
echo "This should bring up ndb management server."
echo "ndm_mgm> SHOW"
echo "This should show something similar to the following:
Connected to Management Server at: localhost:1186
Cluster Configuration
---------------------
[ndbd(NDB)]     2 node(s)
id=2    @127.0.0.1  (mysql-8.0.16 ndb-8.0.16, Nodegroup: 0, *)
id=3    @127.0.0.1  (mysql-8.0.16 ndb-8.0.16, Nodegroup: 0)

[ndb_mgmd(MGM)] 1 node(s)
id=1    @127.0.0.1  (mysql-8.0.16 ndb-8.0.16)

[mysqld(API)]   1 node(s)
id=4    @127.0.0.1  (mysql-8.0.16 ndb-8.0.16)"
echo "For this time only, ndb management server and data nodes have been started for you. To shut them down use"
echo "shell> ndb_mgm -e shutdown"
echo "To start them up later use"
echo "shell> sudo ndb_mgmd -f /var/lib/mysql-cluster/ndb_mgmd_config.ini && sudo ndbd && sudo ndbd"
echo "We hope you're satisfied with our service. If not, please promptly proceed to complain to your immediately facing brick wall."

echo "
Would you like to install GRR now? [This option is offered because a certain someone is too lazy to exec multiple shell scripts]"
select yn in "Yes" "No"; do
    case $yn in
        Yes)
            install_grr;
            break;;
        No)
            break;;
        *) echo "invalid option $REPLY";;
    esac
done

function install_grr {
    set -ex
    echo "GRR will be installed into a virtualenv at ~/.virtualenv/cluster"
    virtualenv virtualenv --python=/usr/bin/python2.7 ~/.virtualenv/cluster
    source "${HOME}/.virtualenv/cluster/bin/activate"
    pip install --upgrade pip wheel six setuptools nodeenv
    nodeenv -p --prebuilt --node=10.12.0
    source "${HOME}/.virtualenv/cluster/bin/activate"

    pip install --no-cache-dir -f https://storage.googleapis.com/releases.grr-response.com/index.html grr-response-templates

    pip install -e grr/proto --progress-bar off
    pip install -e grr/core --progress-bar off
    pip install -e grr/client --progress-bar off
    pip install -e api_client/python --progress-bar off
    pip install -e grr/client_builder --progress-bar off
    pip install -e grr/server/[mysqldatastore] --progress-bar off
    pip install -e grr/test --progress-bar off

    cd grr/proto && python makefile.py && cd -
    cd grr/core/grr_response_core/artifacts && python makefile.py && cd -
    grr_config_updater initialize
}