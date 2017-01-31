import urllib2

# Request source file
url = 'https://www.youtube.com'
request = urllib2.Request(url) # write a letter
response = urllib2.urlopen(request) # Send the letter and get the reply
page = response.read() #Read the reply

#Save source file
webFile = open('webPage.html', 'wb')
webFile.write(page)
webFile.close()
