from analysis_fb.collection.api import api

# url 잘 만들어지나 테스트
# url = api.fb_gen_url(pagename='jtbcnews', a=1, b=2, no=10, token='12345')
# print(url)

# json 데이터중 id 값 가져와보기 test
# id = api.fb_name_to_id('jtbcnews')
# print(id)

# posts = api.fb_fetch_post('jtbcnews', '2018-05-01', '2018-05-31')
# print(posts)

# yield사용했을 때
for posts in api.fb_fetch_post('jtbcnews', '2018-05-01', '2018-05-31'):
    print(posts)