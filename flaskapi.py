# -*- coding: utf-8 -*-
# @Time    : 18/12/26 上午11:40
# @Author  : Edward
# @Site    :
# @File    : flaskapi.py
# @Software: PyCharm Community Edition

from flask import Flask
from flask import jsonify
from flask import Blueprint


class API(Flask):
    blueprint_list = []

    # 创建蓝图
    def create_model(self, name, prefix=None):
        if not isinstance(prefix, str):
            prefix = None
        elif prefix.startswith('/'):
            prefix = prefix
        else:
            prefix = '/%s' % prefix
        blueprint = {
            'blueprint': Blueprint(name, __name__ + name),
            'prefix': prefix
        }
        self.blueprint_list.append(blueprint)

        return blueprint['blueprint']

    def set_response_class(self, rc):
        self.response_class = rc

    def run(self, **kwargs):
        for bluprint in self.blueprint_list:
            self.register_blueprint(
                bluprint['blueprint'],
                url_prefix=bluprint['prefix']
            )

        super(API, self).run(**kwargs)

    def dispatch_request(self):
        resp = super(API, self).dispatch_request()
        if isinstance(resp, tuple):
            return jsonify({
                'data': resp[0],
                'code': resp[1]
            }), resp[1]
        else:
            return jsonify({
                'data': resp,
                'code': 200
            }), 200


if __name__ == '__main__':
    api = API('ttc')

    @api.route('/main')
    def index():
        return '首页'


    @api.route('/test')
    def error():
        return ['ERROR'], 200

    info = api.create_model('info', 'info')
    @info.route('/info')
    def get_info():
        return 'Show Info', 201


    api.config['JSON_AS_ASCII'] = False
    api.run(debug=True)

