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
import cgi
import os

form="""



<form method="post">
    <br>
    When is your birthday?
	<br>

	<label>
		Month
		<input type="text" name="month" value="%(month)s">
	</label>

	<label>
		Day
		<input type="text" name="day" value="%(day)s">
	</label>

	<label>
		Year
		<input type="text" name="year" value="%(year)s">
	</label>

    <div style="color: red">%(error)s</div>

	<br>
	<input type="submit">
</form>


"""

months = ['January', 'February', 'March', 'April', 'May',
                'June', 'July', 'August', 'September', 'October',
                'November', 'December']
month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
    if month:
        short_month = month[:3].lower()            
        return month_abbvs.get(short_month)
def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day
def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year < 2017:
            return year

def escape_html(s):
    return cgi.escape(s, quote = True)





class MainPage(webapp2.RequestHandler):
    def write_form(self, error="",month="",day="",year=""):
        self.response.out.write(form % {"error": error,
            "month": escape_html(month),
            "day": escape_html(day),
            "year": escape_html(year)})

   

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Weclome, this is my first web app!')
        self.write_form()

        
    def post(self):
        user_day = self.request.get('day')
        day = valid_day(user_day)

        user_month = self.request.get('month')
        month = valid_month(user_month)

        user_year = self.request.get('year')
        year = valid_year(user_year)


        if not (year and month and day):
            self.write_form("The input date is not valid.", user_month,user_day,user_year)
        else:
            self.redirect("/thanks")

    

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/thanks', ThanksHandler)
], debug=True)








