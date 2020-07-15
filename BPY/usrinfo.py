import requests


class UserInfo(object):
    # def __init__(self,):
    #     self.uid = '2'

    def my_info(self, login):
        bession = login.bession
        cookie_empty = requests.session().cookies
        usrurl = 'http://api.bilibili.com/nav'
        if bession.cookies == cookie_empty:
            raise EOFError('查看个人信息是需要登录的哦~')
        r = bession.get('http://api.bilibili.com/nav')
        if r.json()['code'] != 0:
            raise EOFError('这里是不会出错的地方呀，看到这条消息的话请联系作者~')
        return r.text

    def my_info_format(self):
        pass

    def pid_info(self, uid):
        if not isinstance(uid, int):
            raise ValueError("uid必须为int型整数哦~")
        data = {'mid': uid}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        r = requests.get(
            'http://api.bilibili.com/x/space/acc/info', headers=headers, params=data)
        return r.text


if __name__ == "__main__":
    test = UserInfo()
    # test.my_info()
    print(test.pid_info(123))
