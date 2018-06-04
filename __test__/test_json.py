# JSON testing

import sys
import json
from urllib.request import Request, urlopen
from datetime import datetime

try:
    url = 'http://192.168.1.11:8080/mysite3/api/guestbook/list'
    request = Request(url)
    response = urlopen(request)

    response_body = response.read().decode('utf-8')
    print(response_body, type(response_body))

    json_result = json.loads(response_body)
    print(json_result, type(json_result))
except Exception as e:
    print('%s : %s' % (e, datetime.now), file=sys.stderr)

