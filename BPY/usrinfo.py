import requests


class usrinfo(object):

    def __init__(self, info_meth, login=None, uid=None):
        self.login = login
        self.uid = uid
        self.info = None
        self.raw = None
        if info_meth == 'me':
            if self.login == None:
                raise LookupError('查看个人信息是需要传入Login对象的哦~')
            self.my_info()
        elif info_meth == 'uid':
            if uid == None:
                raise LookupError("请传入uid哦~")
            self.pid_info()
        else:
            raise ValueError("传入的登录method暂不支持哦！")

    def my_info(self):
        bession = self.login.bession
        usrurl = 'http://api.bilibili.com/nav'
        r = bession.get('http://api.bilibili.com/nav')
        if r.json()['code'] != 0:
            raise EOFError('哇，你的登录居然过期了~')
        # 格式化函数弄完后要修改
        self.raw = r.text
        print(r.text)

    def my_info_format(self):
        pass

    def pid_info(self):
        if not isinstance(self.uid, int):
            raise ValueError("uid必须为int型整数哦~")
        data = {'mid': self.uid}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        r = requests.get(
            'http://api.bilibili.com/x/space/acc/info', headers=headers, params=data)
        # 格式化函数弄完后要修改
        self.raw = r.text
        print(r.text)


if __name__ == "__main__":
    pass
