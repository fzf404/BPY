> 为什么这个项目被叫做BPY呢？
> 
> Bilibili aPi pYthon
## Description

基于 [@社会易姐QWQ](https://github.com/SocialSisterYi) [`bilibili-API-collect`](https://github.com/SocialSisterYi/bilibili-API-collect) 开发的开源Python库。(快去标⭐呀~

主要使用`requests`库，为了扫码登录还引入了`qrcode`与`pillow`。


>这是本咸鱼的第一个项目，有没有大佬一块开发呀，具体参见下面的开发文档~

**[开发文档&进度](https://www.notion.so/BPY-1d139fae04d44a879927e3009911bc6e)**

源码已打包上传至test.pypi


## 安装
- pip安装

    ```
    pip install -i https://test.pypi.org/simple/ biliapi==0.0.2
    ```

## 使用
> 🚨建议在交互模式下使用
### 登录
```python
>>> form biliapi import *
>>> log_info = login('qr')
# 接着会弹出二维码,请扫描登录
请扫描弹出的二维码，超时时间180s。
# 扫描成功后会提示
```

Waiting...正在施工中🚧
