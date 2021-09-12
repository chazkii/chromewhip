# Chromewhip - Google Chrome™ as a web service

### Chrome browser as an HTTP service with an splash compatible HTTP API

Cosive/chromewhip is a fork of the ~~chukus/chromewhip~~ [chazkii/chromewhip](https://github.com/chazkii/chromewhip) Google Chrome DevTools client.


### How to regenerate the Python protocol files

In `scripts`, you can run `regenerate_protocol.sh`, which downloads HEAD of offical devtools specs, regenerates, 
runs some sanity tests and creates a commit with the message of official devtools specs HEAD.

From time to time, it will fail, due to desynchronization of the `chromewhip` patch with the json specs, or 
mistakes in the protocol.

Under `data`, there are `*_patch` files, which follow the [RFC 6902 JSON Patch notation](https://tools.ietf.org/html/rfc6902). 
You will see that there are some checks to see whether particular items in arrays exist before patching. If you get 
a `jsonpatch.JsonPatchTestFailed` exception, it's likely to desynchronization, so check the official spec and adjust 
the patch json file.

