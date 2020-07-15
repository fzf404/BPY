import requests
import qrcode
import time


class Login(object):
    def __init__(self):
        self.bession = requests.session()
        self.bession.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    def login(self, log_meth):
        if log_meth == 'qr':
            self.qr_log()
        elif log_meth == 'pwd':
            raise EOFError("Error~正在研发中！")
            self.pwd()
        elif log_meth == 'sms':
            raise EOFError("Error~正在研发中！")
            self.sms()
        else:
            raise ValueError("传入的登录method暂不支持哦！")

    def qr_log(self):
        get_qr = 'http://passport.bilibili.com/qrcode/getLoginUrl'
        data = self.bession.get(get_qr).json()['data']
        # 获取二维码url以及oauthKey
        time_start = time.time()
        # 计时判断二维码是否失效
        print("请扫描弹出的二维码，超时时间180s。")
        qrcode.make(data['url']).show()
        # 展示二维码
        while True:
            # 持续post至登录成功
            if time.time()-time_start > 170:
                # 判断二维码是否失效
                raise TimeoutError("超时啦~二维码无效了!")
            if self.comfirm(data):
                break

    def comfirm(self, data):
        confirm_url = 'http://passport.bilibili.com/qrcode/getLoginInfo'
        time.sleep(1)
        verify = self.bession.post(confirm_url, data=data)
        if verify.json()['status'] == True:
            print('登陆成功啦,可以开始你的操作啦~')
            return 1
        else:
            return 0


if __name__ == "__main__":
    test = Login()
    test.log_choice('qr')
    print(test.bession.cookies)