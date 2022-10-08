import json

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
myurl = 'http://api.bilibili.com/nav'


class userinfo(object):

    def __init__(self, uid=None, login=None):
        self.login = login
        self.uid = uid
        self.info = None
        self.raw = None
        if login != None:
            self.my_info()
        elif isinstance(self.uid, int):
            self.pid_info()
        else:
            raise ValueError("请传入正确的method哦！")

    def my_info(self):
        bession = self.login.bession
        r = bession.get(myurl)
        if r.json()['code'] != 0:
            raise EOFError('哇，你的登录居然过期了~')
        # TODO:格式化函数弄完后要修改
        self.raw = r.json()
        self.info_format()
        print(self.info)

    def info_format(self):
        self.info = json.dumps(self.raw, sort_keys=True, indent=4,
                               separators=(', ', ': '), ensure_ascii=False)

    def pid_info(self):
        if not isinstance(self.uid, int):
            raise ValueError("uid必须为int型整数哦~")
        data = {'mid': self.uid}
        r = requests.get(
            'http://api.bilibili.com/x/space/acc/info', headers=headers, params=data)
        # 格式化函数弄完后要修改
        self.raw = r.json()
        self.info_format()
        print(self.info)


if __name__ == "__main__":
    pass
