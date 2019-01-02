# Flask-API

## quick start

安装
```shell
pip install Flask-Base-API
```

使用
```python
from flaskapi import API


api = API('ttc')

@api.route('/main')
def index():
    return '首页'


@api.route('/test')
def error():
    return ['ERROR'], 200


# 创建蓝图，第一项为蓝图名称，第二项为访问前缀
info = api.create_model('info', 'info')
@info.route('/info')
def get_info():
    return 'Show Info', 201


api.config['JSON_AS_ASCII'] = False
api.run()
```


返回的结果会直接包装成json格式数据，并将具体内容和http码返回
```shell
curl localhost:5000/main
{
  "code": 200,
  "data": "首页"
}

curl localhost:5000/test
{
  "code": 200,
  "data": [
    "ERROR"
  ]
}

curl localhost:5000/info/info
{
  "code": 201,
  "data": "Show Info"
}
```

