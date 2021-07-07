#!/usr/bin/env bash

if [ "$1" = "" ]; then
  echo "Usage: $0 path/to/browser_protocol.json"
  exit 1
fi
INPUT_FILE=$1
BASE_DIR=$(cd $(dirname $0)/.. && pwd)

jsonpatch --indent 4 ${INPUT_FILE} ${BASE_DIR}/data/browser_protocol_patch.json > ${BASE_DIR}/data/browser_protocol.json
cd ${BASE_DIR}/scripts
if $(python generate_protocol.py --one-input-file); then
  echo "Regeneration complete!"
else
  echo "Regeneration failed! Exiting"
  exit 1
fi
if $(python check_generation.py); then
  echo "Sanity check passed!"
else
  echo "Sanity check failed! Please manually check the generated protocol files"
  exit 1
fi
