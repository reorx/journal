#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from jinja2 import Environment, FileSystemLoader
import inliner
import sendex


env = Environment(loader=FileSystemLoader('templates'))

text = """Hi, Elijah Baily
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et.
"""
name = u'你好哇'
print repr(name)
html = env.get_template('hero.html').render(name=name)
#<html>
#<body>{{ name }}</body>
#</html>
#html = u"""<html>
#<body>你好</body>
#</html>
#"""
print type(html), repr(html)
print ''
inline_html = inliner.get_inline(html.encode('ascii', 'xmlcharrefreplace'))
print ''
print type(inline_html), repr(inline_html)
print ''
#sys.exit()

sendex.send_email(text, inline_html.encode('gbk'))
