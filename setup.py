from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='biliapi',
    version='0.0.1',
    description='BPY: b站API的python库',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='你们的小f',
    author_email='nmdfzf404@163.com',
    url='https://github.com/fzf404/BPY',
    license="MIT",
    packages=find_packages(),
    install_requires=['qrcode >= 6.1',
                      'pillow >= 6.0.0', 'requests >= 2.22.0'],
)
