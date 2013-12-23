#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from torext.app import TorextApp
from torext.handlers import BaseHandler as _BaseHandler
try:
    from . import app_settings
except ValueError:
    print 'execute app.py as __main__'
    import app_settings


app = TorextApp(app_settings)


from jinja2 import Environment, PackageLoader
from workjournal.gitutil import UserRepo


env = Environment(loader=PackageLoader('workjournal', 'templates'))

repo = UserRepo('/home/reorx/workspace/sohu/changyancommunity', ['felixzhu@sohu-inc.com'])


def timestamp2strftime(ts):
    dt = datetime.datetime.fromtimestamp(ts)
    return dt.strftime('%m-%d %H:%M:%S')

env.filters['timestamp2strftime'] = timestamp2strftime


class BaseHandler(_BaseHandler):
    def render_html(self, template_name, **kwargs):
        template = env.get_template(template_name)
        self.write(template.render(**kwargs))


@app.route('/')
class HomeHandler(BaseHandler):
    def get(self):
        #commits = repo.get_date_commits('2013-12-11', '2013-12-12')
        commits = repo.get_date_commits(datetime.datetime.now().strftime('%Y-%m-%d'))
        self.render_html('home.html', commits=commits)


if __name__ == '__main__':
    # Only for testing purpose
    app.command_line_config()
    app.run()
