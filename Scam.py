import os
import string
import requests
import json 
import random

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'website'
names = json.loads(open('names.json').read())

for name in names:
  name_extra = ''.join(random.choice(string.digits))
  username = name.lower() + name_extra + '@gmail.com'
  password = ''.join(random.choice(chars) for i in range(8))
  requests.post(url, allow_redirects = False, data = {
    'emaildata': username,
    'passworddata': password
  })

print ('sending username %s password  %s' % (username, password))