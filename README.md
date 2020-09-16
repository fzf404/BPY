## 🚧弃坑了QWQ🚧

> 为什么这个项目被叫做BPY呢？
> 
> Bilibili aPi pYthon
## Description

基于 [@社会易姐QWQ](https://github.com/SocialSisterYi) [`bilibili-API-collect`](https://github.com/SocialSisterYi/bilibili-API-collect) 开发的开源Python库。(快去标⭐呀~

主要使用`requests`库，为了扫码登录还引入了`qrcode`与`pillow`。

调用时尽量保证调用简洁明快~


> 这是本咸鱼的第一个项目
> 
> 不知道代码格式是否规范~
> 
> 有没有大佬一块开发呀，具体参见下面的开发文档~

## [开发文档&进度](https://www.notion.so/BPY-1d139fae04d44a879927e3009911bc6e)

> 刚弄完了扫描登录与用户信息查询（格式化输出都没做）
> 
> 详见[传送门](https://www.notion.so/BPY-1d139fae04d44a879927e3009911bc6e)
> 
> 源码已打包上传至test.pypi


## 安装
- pip安装

    ```
    pip install -i https://test.pypi.org/simple/ biliapi==0.0.3
    ```

## 使用
> 🚨建议在交互模式下使用
### 登录
```python
>>> form BPI import *

>>> log_info = login('qr')
# 接着会弹出二维码,请扫描登录
请扫描弹出的二维码，超时时间180s。
# 扫描成功后会提示
登陆成功啦,可以开始你的操作啦~

>>> print(log_info.cookies)
# 将输出格式化后的cookie值
{
    "DedeUserID": "***已打码***",
    "DedeUserID__ckMd5": "***已打码***",
    "SESSDATA": "***已打码***",
    "bili_jct": "***已打码***",
    "sid": "***已打码***"
}

>>> my = usrinfo(login = log_info)
# 打印log_info函数对应的信息（格式化处理函数暂未施工）
>>> my.raw  
# 查看未处理的json

>>> u2 = usrinfo(uid = 2)
# 将返回 uid=2（碧诗）的用户信息
>>> u2.raw

```
### 使用文档

...

Waiting...正在施工中🚧
