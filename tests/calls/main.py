#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

import os
import calls
import simplejson

class TemplateHandler(webapp.RequestHandler):
    
    def render(self, temp, ctx):
        path = os.path.join(os.path.dirname(__file__), temp)
        self.response.out.write(template.render(path, ctx))
    

class MainHandler(TemplateHandler):
    
    def get(self):
        self.render('index.html',{'n': 2})
    
    def post(self):
        n = int(self.request.get('num'))
        if n > 15:
            self.render('index.html', {'n': n, 'toobig': True})
        else:
            res = calls.fibcalls(n)
            pprinted = simplejson.dumps(res)
            self.render('index.html', {'n': n, 'res': pprinted})
    


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
