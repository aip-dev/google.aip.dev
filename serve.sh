#!/bin/bash
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -----------------------------------------------------------------------------
#   This script runs a "development server" from Docker.
# -----------------------------------------------------------------------------

# Build the image (if and only if it is not already built).
if [[ "$(docker images -q aip-site 2> /dev/null)" == "" ]]; then
  docker build -t aip-site .
  if [ $? != 0 ]; then
    exit $?
  fi
fi

# Run the image.
docker run --rm \
  -p 4000:4000/tcp -p 4000:4000/udp \
  -p 35729:35729/tcp -p 35729:35729/udp \
  --mount type=bind,source=`pwd`,destination=/code/,readonly \
  aip-site \
  "$@"
