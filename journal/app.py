#!/usr/bin/env python
# -*- coding: utf-8 -*-

from torext.app import TorextApp
from torext.handlers import BaseHandler
import settings


app = TorextApp(settings)


@app.route('/')
class HomeHandler(BaseHandler):
    def get(self):
        self.render('home.html')


if __name__ == '__main__':

    app.command_line_config()
    app.run()
