# Chromewhip - Google Chrome™ as a web service

[![Build Status](https://travis-ci.org/chuckus/chromewhip.svg?branch=master)](https://travis-ci.org/chuckus/chromewhip)

### Chrome browser as an HTTP service with an splash compatible HTTP API

Chromewhip is an easily deployable service that runs headless Chrome process 
wrapped with an HTTP API. Inspired by the [`splash`](https://github.com/scrapinghub/splash) 
project, we aim to provide a drop-in replacement for the `splash` service by adhering to their documented API.

It is currently in early **alpha** and still being heavily developed. Please use the issue tracker 
to track the progress towards **beta**. For now, the required milestone can be summarised as 
**implementing the entire Splash API**.

## Usage with Docker

```
docker run --init -it --rm --shm-size=1024m -p=127.0.0.1:8080:8080 --cap-add=SYS_ADMIN \
  chuckus/chromewhip
```

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

 