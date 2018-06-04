from urllib.parse import urlencode
from analysis_fb.collection.api import json_request as jr
# import 문제였음. .json_request로 함수 자체를 불러왔었는데
# 나는 모듈을 불러와서 값을 못 찾았었음.

BASE_URL_FB_API = 'https://graph.facebook.com/v3.0'
ACCESS_TOKEN = 'EAACEdEose0cBAEzGfOZATzLOqXLrDmTGaZCJJl6ZBBrFaHOWaUx6F2rv4shOpKgtZAlCNptcAVPbvvdXI8tWGZCoqJUCoZBNa6Gluror0uXX8dHuKttSBReUEfZB44uJODmGoeWF6ttmXRCX9tKRtLq5X8QGZBZBrBCFRC83D8WMKBVlrZBv3D0CQHfzwsV1qcoq8gLroUrj5LZBgZDZD'

# fb_gen_url(pagename='jtbcnews', a=1, b=2, token)

def fb_gen_url(base=BASE_URL_FB_API, node='', **param):
    return '%s/%s/?%s' % (base, node, urlencode(param))

# url을 pagename으로 떄리는 것이 아니라 id값으로 때리기 때문에 필요한 부분.
def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    print(url)
    json_result = jr.json_request(url)
    print(json_result)
    return json_result.get('id')

def fb_fetch_post(pagename, since, until):
    url = fb_gen_url(
        node=fb_name_to_id(pagename) + '/posts',
        fields='id,message,link,name,type,shares,created_time,\
                reactions.limit(0).summary(true),\
                comments.limit(0).summary(true)',
        since=since,
        until=until,
        limit=50,
        access_token=ACCESS_TOKEN
    )

    isnext = True
    # data = []

    while isnext is True:
        json_result = jr.json_request(url=url)

        paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

        url = None if paging is None else paging.get('next')
        isnext = url is not None

        # data += posts

    # return data
        yield posts