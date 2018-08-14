from flask import jsonify
class RespUtils():
    @staticmethod
    def error(msg="请求失败",data={}):
        resp={
            'code': 0,
            'msg': msg,
            'data': data
        }
        return jsonify(resp)

    @staticmethod
    def success(msg="请求成功", data={}):
        resp = {
            'code': 1,
            'msg': msg,
            'data': data
        }
        return jsonify(resp)

    @staticmethod
    def loginError(msg="登陆失效，请重新登录", data= {}):
        resp = {
            'code': 2,
            'msg': msg,
            'data': data
        }
        return jsonify(resp)