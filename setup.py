# -*- coding: utf-8 -*-
# @Time    : 19/1/2 下午2:01
# @Author  : Edward
# @Site    :
# @File    : setup.py
# @Software: PyCharm Community Edition

from setuptools import setup, find_packages

setup(
    name="Flask-Base-API",
    packages=find_packages(),
    version='0.1.3',
    description="Flask的Api包，用于快速开发API接口",
    author="L_zejie",
    author_email='lzj_xuexi@163.com',
    url="https://github.com/Lzejie/Flask-API",
    license="MIT Licence",
    keywords=["Flask API", "API"],
    classifiers=[],
    install_requires=[
        'Click==7.0',
        'Flask==1.0.2',
        'itsdangerous==1.1.0',
        'Jinja2==2.10',
        'MarkupSafe==1.1.0',
        'Werkzeug==0.14.1',
    ]
)
