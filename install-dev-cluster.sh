#!/bin/bash

set -ex
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
