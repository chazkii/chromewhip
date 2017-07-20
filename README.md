# Chromewhip - Google Chrome™ as a web service

[![Build Status](https://travis-ci.org/chuckus/chromewhip.svg?branch=master)](https://travis-ci.org/chuckus/chromewhip)
[![Docker Hub Status](https://img.shields.io/docker/build/chuckus/chromewhip.svg)](https://img.shields.io/docker/build/chuckus/chromewhip.svg)

### Chrome browser as an HTTP service with an splash compatible HTTP API

Chromewhip is an easily deployable service that runs headless Chrome process 
wrapped with an HTTP API. Inspired by the [`splash`](https://github.com/scrapinghub/splash) 
project, we aim to provide a drop-in replacement for the `splash` service by adhering to their documented API.

It is currently in early **alpha** and still being heavily developed. Please use the issue tracker 
to track the progress towards **beta**. For now, the required milestone can be summarised as 
**implementing the entire Splash API**.

### Python 3.6 asyncio driver for Chrome devtools protocol

Chromewhip communicates with the Chrome process with our own asyncio driver.

* Typed Python bindings for devtools protocol through templated generation - get autocomplete with your code editor.
* Can bind events to concurrent commands

## Running

### Deploying with Docker

```
docker run --init -it --rm --shm-size=1024m -p=127.0.0.1:8080:8080 --cap-add=SYS_ADMIN \
  chuckus/chromewhip
```

### Requirements for MacOS 10.12+

* Google Chrome Canary

## Implemented HTTP API

### /render.html

Query params:

* url : string : required
  * The url to render (required)

* js : string : optional
  Javascript profile name.
  
* js_source : string : optional
   * JavaScript code to be executed in page context

* viewport : string : optional
  * View width and height (in pixels) of the browser viewport to render the web
    page. Format is "<width>x<height>", e.g. 800x600.  Default value is 1024x768.

    'viewport' parameter is more important for PNG and JPEG rendering; it is supported for
    all rendering endpoints because javascript code execution can depend on
    viewport size. 
 
### /render.png

Query params (including render.html):

* render_all : int : optional
  * Possible values are `1` and `0`.  When `render_all=1`, extend the
    viewport to include the whole webpage (possibly very tall) before rendering.
   
### Why not just use Selenium?
* chromewhip uses the devtools protocol instead of the json wire protocol, where the devtools protocol has 
greater flexibility, especially when it comes to subscribing to granular events from the browser.

## Bug reports and requests
Please simply file one using the Github tracker

## Contributing
Please :)

## Implementation

Developed to run on Python 3.6, it leverages both `aiohttp` and `asyncio` for the implementation of the 
asynchronous HTTP server that wraps `chrome`.

 