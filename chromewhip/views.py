import asyncio
import functools
import logging

from bs4 import BeautifulSoup
from aiohttp import web

from chromewhip.protocol import page, emulation, browser, dom, runtime

BS = functools.partial(BeautifulSoup, features="lxml")

log = logging.getLogger('chromewhip.views')

async def _go(request: web.Request):

    js_profiles = request.app['js-profiles']
    c = request.app['chrome-driver']

    url = request.query.get('url')
    if not url:
        return web.HTTPBadRequest(reason='no url query param provided')  # TODO: match splash reply

    wait_s = float(request.query.get('wait', 0))

    raw_viewport = request.query.get('viewport', '1024x768')
    parts = raw_viewport.split('x')
    width = int(parts[0])
    height = int(parts[1])

    js_profile_name = request.query.get('js', None)
    if js_profile_name:
        profile = js_profiles.get(js_profile_name)
        if not profile:
            return web.HTTPBadRequest(reason='profile name is incorrect')  # TODO: match splash

    # TODO: potentially validate and verify js source for errors and security concerrns
    js_source = request.query.get('js_source', None)

    await c.connect()
    tab = c.tabs[0]
    cmd = page.Page.setDeviceMetricsOverride(width=width,
                                             height=height,
                                             deviceScaleFactor=0.0,
                                             mobile=False)
    await tab.send_command(cmd)
    await tab.enable_page_events()
    await tab.go(url)
    await asyncio.sleep(wait_s)
    if js_profile_name:
        await tab.evaluate(js_profiles[js_profile_name])

    if js_source:
        await tab.evaluate(js_source)

    return tab


async def render_html(request: web.Request):
    # https://splash.readthedocs.io/en/stable/api.html#render-html
    tab = await _go(request)
    return web.Response(text=BS((await tab.html()).decode()).prettify())

