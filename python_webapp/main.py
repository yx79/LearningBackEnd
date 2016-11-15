# Copyright 2016 Google Inc.
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

import webapp2

form="""
<form action="http://www.google.com/search">
	<input name="q">
	<input type="submit">

</form>

<form method="post" action="/testform">
	<input name="q">
	<input type="submit">

</form>

<form>
	<input type="password" name="q">
	<input type="submit">
</form>

<form>
	<input type="checkbox" name="q">
	<input type="submit">
</form>

<form>
	<input type="checkbox" name="q">
	<input type="checkbox" name="r">
	<input type="checkbox" name="s">
	<br>
	<input type="submit">
</form>

<form>
	<label>
		One
		<input type="radio" name="q" value="one">
	</label>

	<label>
		Two
		<input type="radio" name="q" value="two">
	</label>

	<label>
		Three
		<input type="radio" name="q" value="three">
	</laebl>
	<br>
	<input type="submit">
	<br>
</form>

<form>
	<select name="q">
		<option>one</option>
		<option>two</option>
		<option>three</option>
	</select>
	<br>
	<input type="submit">
</form>


<form>
	<select name="q">
		<option value="1">the number one</option>
		<option>two</option>
		<option>three</option>
	</select>
	<br>
	<input type="submit">
</form>

"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Weclome, this is my first web app!')
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
	def post(self):
		q = self.request.get("q")
		self.response.out.write(q)
		
		# print the request
		#self.response.headers['Content-Type'] = 'text/plain'
		#self.response.out.write(self.request)


		

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', TestHandler)
], debug=True)








