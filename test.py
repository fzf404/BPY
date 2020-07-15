import BPY
test = BPY.Login()
test.login('qr')
test2 = BPY.UserInfo()
test2.my_info(test)
print(test.bession.cookies)
