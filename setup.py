
#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='BPY',
    version='v0.1',
    description='BPY: b站API的python库',
    long_description="一个bilibiliAPI的python封装库",
    author='你们的小f',
    author_email='nmdfzf404@163.com',
    url='无',
    license="Public domain",
    packages=find_packages(),
    install_requires=['qrcode >= 6.1', 'pillow >= 6.0.0', 'requests >= 2.22.0']
)
