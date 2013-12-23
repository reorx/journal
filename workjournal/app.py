#!/usr/bin/env python
# -*- coding: utf-8 -*-

from torext.app import TorextApp
from torext.handlers import BaseHandler
try:
    from . import app_settings
except ValueError:
    print 'execute app.py as __main__'
    import app_settings


app = TorextApp(app_settings)


@app.route('/')
class HomeHandler(BaseHandler):
    def get(self):
        self.render('home.html')


if __name__ == '__main__':

    # Only for testing purpose
    app.command_line_config()
    app.run()
