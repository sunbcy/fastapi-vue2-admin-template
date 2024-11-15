# https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=3937c8c4-ba15-458b-8f06-eb3db814d668

# -d '{"msgtype":"text","text":{"content":"Hello world"}}'
import json
from urllib.parse import unquote

import requests
from fastapi import APIRouter
from fastapi import Request
from utils import check_proxy
from utils import responses as resp
from utils.responses import response_with

router = APIRouter()


class QiYeWeChatBot:
    wechat_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key='

    def __init__(self, secret_key='3937c8c4-ba15-458b-8f06-eb3db814d668'):
        self.key = secret_key

    def send_text(self, msg, *mention_set):
        """
        文本类型
        报错：当msg为https://music.163.com/#/my/m/music/playlist?id=316590949的时候会报错
        """
        # msg = json.loads(msg)
        # encoded_msg = quote(msg)  # 编码加密函数在前端的函数里
        decoded_msg = unquote(msg['text'])
        print(decoded_msg)
        headers = {"Content-Type": "application/json"}
        if len(mention_set) >= 1:
            mentioned_mobile_list = [name for name in mention_set]
            para = {
                'msgtype': 'text',
                'text': {
                    'content': decoded_msg,
                    'mentioned_mobile_list': mentioned_mobile_list
                    }
                }
        else:
            para = {'msgtype': 'text',
                    'text': {'content': decoded_msg}}
        # print(self.wechat_url+self.key)
        res = requests.post(self.wechat_url+self.key, data=json.dumps(para), headers=headers, proxies=check_proxy())
        if res.status_code == 200:
            print('消息发送成功!')
        else:
            print(res.status_code)
        return res.text

    def send_markdown(self, msg, *mention_set):
        """
        markdown类型
        """
        headers = {"Content-Type": "application/json"}
        if len(mention_set) >= 1:
            mentioned_mobile_list = [name for name in mention_set]
            para = {
                'msgtype': 'markdown',
                'markdown': {
                    "content": "实时新增用户反馈<font color=\"warning\">132例</font>，请相关同事注意。\n>类型:<font color=\"comment\">用户反馈</font>>普通用户反馈:<font color=\"comment\">117例</font>>VIP用户反馈:<font color=\"comment\">15例</font>",
                    'mentioned_mobile_list': mentioned_mobile_list
                    }
                }
        else:
            para = {'msgtype': 'markdown',
                    'markdown': {'content': msg}}
        # print(self.wechat_url+self.key)
        res = requests.post(self.wechat_url+self.key, data=json.dumps(para), headers=headers, proxies=check_proxy())
        print(res.status_code)
        return res.text

    def send_image(self, msg, *mention_set):
        """
        图片类型
        """
        headers = {"Content-Type": "application/json"}
        if len(mention_set) >= 1:
            mentioned_mobile_list = [name for name in mention_set]
            para = {
                'msgtype': 'image',
                'image': {
                    "base64": "DATA",
                    "md5": "MD5",
                    }
                }
        else:
            para = {
                'msgtype': 'image',
                'image': {
                    "base64": "DATA",
                    "md5": "MD5"
                }
            }
        # print(self.wechat_url+self.key)
        res = requests.post(self.wechat_url+self.key, data=json.dumps(para), headers=headers, proxies=check_proxy())
        print(res.status_code)
        return res.text

    def send_news(self, msg, *mention_set):
        """
        图文类型
        """
        headers = {"Content-Type": "application/json"}
        if len(mention_set) >= 1:
            mentioned_mobile_list = [name for name in mention_set]
            para = {
                'msgtype': 'news',
                'news': {
                    "articles": [
                        {
                            "title": "中秋节礼品领取",
                            "description": "今年中秋节公司有豪礼相送",
                            "url": "www.qq.com",
                            "picurl": "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
                        }
                    ]
                    }
                }
        else:
            para = {
                'msgtype': 'news',
                'news': {
                    "articles": [
                        {
                            "title": "中秋节礼品领取",
                            "description": "今年中秋节公司有豪礼相送",
                            "url": "www.qq.com",
                            "picurl": "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
                        }
                    ]
                }
            }
        # print(self.wechat_url+self.key)
        res = requests.post(self.wechat_url+self.key, data=json.dumps(para), headers=headers, proxies=check_proxy())
        print(res.status_code)
        return res.text

    def send_file(self, msg, *mention_set):
        """
        文件类型
        """
        headers = {"Content-Type": "application/json"}
        if len(mention_set) >= 1:
            mentioned_mobile_list = [name for name in mention_set]
            para = {
                'msgtype': 'file',
                'file': {
                    "media_id": "3a8asd892asd8asd"
                    }
                }
        else:
            para = {
                'msgtype': 'file',
                'file': {
                    "media_id": "3a8asd892asd8asd"
                    }
                }
        # print(self.wechat_url+self.key)
        res = requests.post(self.wechat_url+self.key, data=json.dumps(para), headers=headers, proxies=check_proxy())
        print(res.status_code)
        return res.text

    def send_voice(self, msg, *mention_set):
        """
        语音类型
        """
        headers = {"Content-Type": "application/json"}
        if len(mention_set) >= 1:
            mentioned_mobile_list = [name for name in mention_set]
            para = {
                'msgtype': 'voice',
                'voice': {
                    "media_id": "MEDIA_ID"
                    }
                }
        else:
            para = {
                'msgtype': 'voice',
                'voice': {
                    "media_id": "MEDIA_ID"
                    }
                }
        # print(self.wechat_url+self.key)
        res = requests.post(self.wechat_url+self.key, data=json.dumps(para), headers=headers, proxies=check_proxy())
        print(res.status_code)
        return res.text


@router.post('/send_text')
async def send_msg_text(request: Request):
    # print('后端函数ok')
    data = await request.json()
    Bot_1 = QiYeWeChatBot()
    # Bot_1.send_text(snd_msg, (15524262440,)) -->  {"errcode":0,"errmsg":"ok"}
    try:
        value = {'sendResults': Bot_1.send_text(data, (15524262440,))}
        return response_with(resp.SUCCESS_200, value=value)
    except Exception as e:
        value = {'sendResults': []}
        return response_with(resp.NOT_FOUND_HANDLER_404, value=value)


if __name__ == '__main__':
    key = '3937c8c4-ba15-458b-8f06-eb3db814d668'
    Bot_1 = QiYeWeChatBot(key)
    send_cnt = 'Hello World, 爱你们哦'
    ret = Bot_1.send_text(send_cnt, (15524262440, ))
    print(ret)
