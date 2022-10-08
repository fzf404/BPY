# BPY

> 🚧 弃坑了 QWQ 🚧

## 关于

基于 [SocialSisterYi](https://github.com/SocialSisterYi) / [bilibili-API-collect](https://github.com/SocialSisterYi/bilibili-API-collect) 开发的开源 Python 库。

使用 `requests` 库，为了扫码登录还引入了 `qrcode` 与 `pillow`。

调用时尽量保证调用简洁明快~

> 这是本咸鱼的第一个项目
>
> 不知道代码格式是否规范
>
> 有没有大佬一块开发呀，具体参见下面的开发文档

## 进度

> 刚弄完了扫描登录与用户信息查询（格式化输出都没做）
>
> 源码已打包上传至 test.pypi

## 安装

```
pip install -i https://test.pypi.org/simple/ biliapi==0.0.3
```

## 使用

> 🚨 建议在交互模式下使用

### 登录

```python
>>> form BPI import login, userinfo

# 登录
>>> user = login('qr')
请扫描弹出的二维码，超时时间180s。
登陆成功啦,可以开始你的操作啦~

# 登录 Cookie 信息
>>> print(user.cookies)
{
    "DedeUserID": "***已打码***",
    "DedeUserID__ckMd5": "***已打码***",
    "SESSDATA": "***已打码***",
    "bili_jct": "***已打码***",
    "sid": "***已打码***"
}

# 用户信息
>>> info = userinfo(login = user)

# 未经处理的用户信息
>>> info.raw

# 用户信息
>>> uid = userinfo(uid = 2)

# 未经处理的用户信息
>>> uid.raw

```
