#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import markdown
from torext.app import TorextApp
from torext.handlers import BaseHandler as _BaseHandler
from torext import params
try:
    from . import app_settings
except ValueError:
    print 'execute app.py as __main__'
    import app_settings


app = TorextApp(app_settings)


from jinja2 import Environment, PackageLoader
from workjournal.gitutil import UserRepo


env = Environment(loader=PackageLoader('workjournal', 'templates'))

repo = UserRepo('/home/reorx/workspace/current/torext')


def timestamp2strftime(ts):
    dt = datetime.datetime.fromtimestamp(ts)
    return dt.strftime('%m-%d %H:%M:%S')


def joincommitshex(l):
    return ','.join(i[0].hexsha for i in l.commits)


def text2var(s):
    s = s.replace('"', '\\"')
    s = s.replace("'", "\\'")
    return s.replace('\n', '')

env.filters['timestamp2strftime'] = timestamp2strftime
env.filters['joincommitshex'] = joincommitshex
env.filters['text2var'] = text2var


class BaseHandler(_BaseHandler):
    commits = None

    def render_html(self, template_name, **kwargs):
        template = env.get_template(template_name)
        self.write(template.render(**kwargs))


@app.route('/')
class HomeHandler(BaseHandler):
    def get(self):
        BaseHandler.commits = repo.get_date_commits('2013-11-01')
        #commits = repo.get_date_commits(datetime.datetime.now().strftime('%Y-%m-%d'))
        self.render_html('home.html', commits=BaseHandler.commits)


@app.route('/preview')
class PreviewHandler(BaseHandler):
    @params.define_params({
        'commits': params.Field(),
        'myjournal': params.Field(),
    })
    def post(self):
        if not self.params.commits and self.params.myjournal:
            self.render_html('error.html', notice='You should write journal if there are no commits')

        kwargs = {}
        if self.params.commits:
            kwargs['commits'] = [BaseHandler.commits.get(i)[0]
                                 for i in self.params.commits.split(',')]
        if self.params.myjournal:
            kwargs['myjournal'] = markdown.markdown(self.params.myjournal)
        self.render_html('preview.html', preview=self.get_preview(**kwargs))

    def get_preview(self, **kwargs):
        print kwargs
        template = env.get_template('email/basic.html')
        return template.render(**kwargs)

    def get(self):
        pass


if __name__ == '__main__':
    # Only for testing purpose
    app.command_line_config()
    app.run()
