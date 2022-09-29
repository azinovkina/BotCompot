import json

import requests

# r = requests.get('https://api.github.com')
# # texts = json.loads(r.content)
# # print(type(texts))
# #
# # for text in texts:
# #     print(text[:50], '\n')
# d = json.loads(r.content)
#
# print(type(d))
# print(d['following_url'])
#
# data = {'key': 'value'}
# r = requests.post('https://httpbin.org/post', json=json.dumps(data))
# print(r.content)
r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
r = json.loads(r.content)

print(r[0])
