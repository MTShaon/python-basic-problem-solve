#Write a Python program to access and print a URL's content to the console.
from http.client import HTTPConnection
cann = HTTPConnection("example.com")
cann.request("GET","/")
result = cann.getresponse()
# retrieves the entire contents.
content = result.read()
print(content)