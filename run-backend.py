#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server import app
from gevent.wsgi import WSGIServer

http_server = WSGIServer(('', 8080), app)
http_server.serve_forever()