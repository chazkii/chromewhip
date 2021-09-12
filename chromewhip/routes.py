from chromewhip.views import render_html


def setup_routes(app):
    app.router.add_get('/render.html', render_html)
