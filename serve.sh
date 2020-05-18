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

# Unless we are in incremental mode, the source filesystem should
# be read-only. Incremental mode sadly requires writing a file to the
# source directory.
READ_ONLY=',readonly'
if [[ $* == *--incremental* ]]; then
  READ_ONLY=''
fi

# Run the image.
# Add '-e PAGES_API_URL=https://[domain]/api/v3/ \' if connecting to a
# GitHub Enterprise AIP repository
docker run --rm \
  -e PAGES_REPO_NWO=googleapis/aip \
  -p 4000:4000/tcp   -p 4000:4000/udp   \
  -p 35729:35729/tcp -p 35729:35729/udp \
  --mount type=bind,source=`pwd`,destination=/code/${READ_ONLY} \
  aip-site \
  "$@"
