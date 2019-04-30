#!/bin/bash
source "${HOME}/.virtualenv/grr/bin/activate"

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
