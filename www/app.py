#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__= 'du'
'''
async web apllication
'''

from aiohttp import web
from datetime import datetime
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

async def init(loop):
   app = web.Application(loop=loop)
   app.router.add_route('GET','/', index)
   srv = await loop.create_server(app.make_handler(), '', 9001)
   logging.info('server start at http://localhost:9001')
   return srv

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()


