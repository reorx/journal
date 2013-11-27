#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests


def get_inline(source):
    url = 'http://zurb.com/ink/skate-proxy.php'
    resp = requests.post(url, data={'source': source})
    if resp.status_code != 200:
        raise Exception('Inliner failed')
    print 'json', repr(resp.content)
    return json.loads(resp.content, encoding='utf8')['html']
