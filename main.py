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
from caesar import encrypt

form = """
<form method = "post" action = "/">
    <label>
        Rotation Number:
        <input type="text" name="rot_num" value="%(rot_num)s">
    </label>
    <br>
    <label>
        Text to Encrypt:
        <input type="text" name="encrypt_box" value="%(encrypt_box)s">
    <br>
    <input type="submit">
</form>
"""




class MainHandler(webapp2.RequestHandler):
    def form_Writer(self, rot_num="", encrypt_box=""):
        self.response.out.write(form % {"rot_num": rot_num,
                                        "encrypt_box": encrypt_box})

    def get(self):
        self.form_Writer()

    def post(self):
        q = self.request.get("encrypt_box")
        user_num = self.request.get("rot_num")
        user_num = int(user_num)
        encrypt_txt = encrypt(q, user_num)

        self.form_Writer(user_num, encrypt_txt)
        #self.response.out.write(encrypt_txt)
        #self.response.out.write(user_num)





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
