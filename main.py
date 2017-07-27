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
import webapp2
import jinja2
import os
import sys
import json

sys.path.append('source/')
from pages import Page
from pages import pages
from pages import excerptPages
from pages import art1sections

env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))

def constructPage(page):
    pageDict = page.toDictionary()
    pageTemp = env.get_template("template.html")
    print pageDict
    pageFinal = pageTemp.render(pageDict)
    return pageFinal

class MainHandler(webapp2.RequestHandler):
    def get(self):
        home = pages[0]
        self.response.out.write(constructPage(home))


class SectionHandler(webapp2.RequestHandler):
    def get(self):
        page = pages[int(self.request.get('id'))]
        self.response.out.write(constructPage(page))

    def constructPage(self, page):
        pageDict = page.toDictionary()
        pageTemp = env.get_template("template.html")
        pageFinal = pageTemp.render(pageDict)
        return pageFinal

class ExHandler(webapp2.RequestHandler):
    #curr = 1
    def get(self):
        page = excerptPages[int(self.request.get('id'))]
        page.sectionID = 1
        self.response.out.write(constructPage(page))
        #curr = 1

    def post(self):
        #curr = curr
        page = excerptPages[int(self.request.get('id'))]
        if self.request.get('choice')=="incorrect" :
            self.response.out.write(constructPage(page))
        else:
            page.sectionID = page.sectionID + 1
            page.content = art1sections[page.sectionID]
            self.response.out.write(constructPage(page))

    def constructPage(self, page):
        pageDict = page.toDictionary()
        pageTemp = env.get_template("template.html")
        pageFinal = pageTemp.render(pageDict)
        return pageFinal

class SpeedHandler(webapp2.RequestHandler):
    def get(self):
        page = excerptPages[int(self.request.get('id'))]
        pageDict = page.toDictionary()
        pageTemp = env.get_template("templateForSpeed.html")
        pageFinal = pageTemp.render(pageDict)
        self.response.out.write(pageFinal)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/view-section', SectionHandler),
    ('/view-excerpt', ExHandler),
    ('/get-speed', SpeedHandler)
], debug=True)
