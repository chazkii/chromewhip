#!/usr/bin/env bash

rm -rf devtools-protocol
git clone --depth=1 https://github.com/ChromeDevTools/devtools-protocol.git
cd devtools-protocol
LATEST_GIT_MSG=$(git log --oneline --no-color)
CHROMEWHIP_GIT_MSG=$(cat ../../data/devtools_protocol_msg)
echo $LATEST_GIT_MSG
echo $CHROMEWHIP_GIT_MSG
if [ "$LATEST_GIT_MSG" != "$CHROMEWHIP_GIT_MSG" ]
then
  echo "devtools-protocol has been updated. Regenerating chromewhip protocol files."
  cd ../..
  jsonpatch scripts/devtools-protocol/json/browser_protocol.json data/browser_protocol_patch.json > data/browser_protocol.json
  jsonpatch scripts/devtools-protocol/json/js_protocol.json data/js_protocol_patch.json > data/js_protocol.json
  rm -rf scripts/devtools-protocol
  cd scripts
  python generate_protocol.py
fi
