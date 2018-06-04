# http testing

import sys
from urllib.request import Request, urlopen
from datetime import datetime

try:
    url = 'http://192.168.1.11:8080/mysite3/gb/ajax'
    request = Request(url)
    response = urlopen(request)

    response_body = response.read().decode('utf-8')
    print(response_body)
except Exception as e:
    print('%s : %s' % (e, datetime.now), file=sys.stderr)

