"""
用于向指定用户发送消息
前提：
    1. 申请账号
       自己的账号
       "appid": 'wxc937f52b24532ba0',
        "secret": '1b05f85bd620d15015b34e151ddeba4b',
    2. 知道用户的微信ID
        oQUp81U8veytwKBvqkGLNd8ENxGw





"""
import json
import requests

# 1. 伪造浏览器向 https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential... 发送GET请求，并获取token
r1 = requests.get(
    url="https://api.weixin.qq.com/cgi-bin/token",
    params={
        "grant_type": "client_credential",
        "appid": 'wxc937f52b24532ba0',
        "secret": '1b05f85bd620d15015b34e151ddeba4b',
    }
)

access_token = r1.json().get('access_token')

# 2. 给指定用户发送普通消息消息：access_token/

# wx_id = 'oQUp81U8veytwKBvqkGLNd8ENxGw'
# wx_id1 = 'oQUp81WXsMsbqW6ijr-Zm6-aCHE0'
#
# body = {
#     "touser": wx_id1,
#     "msgtype": "text",
#     "text": {
#         "content": '你个逗比'
#     }
# }
#
# r2 = requests.post(
#     url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
#     params={
#         'access_token': access_token
#     },
#     data=bytes(json.dumps(body,ensure_ascii=False),encoding='utf-8')
# )
#
# print(r2.text)

# 3. 给指定用户发送模板消息：access_token/

wx_id = 'oQUp81WXsMsbqW6ijr-Zm6-aCHE0'

body = {
    "touser": wx_id,
    "template_id": 'A0bn5wxtlQgAfrTyhcVbllD8J-hCj4QCsHKZE68HqcA',
    "data": {
        "user": {
            "value": "鹏程万里",
            "color": "#173177"
        }
    }
}

r2 = requests.post(
    url="https://api.weixin.qq.com/cgi-bin/message/template/send",
    params={
        'access_token': access_token
    },
    data=json.dumps(body)
)

print(r2.text)


# response = requests.post(
#     url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
#     params={
#         'access_token': access_token
#     },
#     data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
# )
# # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
# result = response.json()
# print(result)
