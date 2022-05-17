import json

from flask import Response

"""
{
  "err_code": 0,                // 状态码，可在获得响应后区分下一步操作
  "data_list": [
    {                           // 目前返回信息需要包裹在 `data_list` 中唯一对象内
      "param_a": "content_a",   // 参数，可在获得响应后填充进对应语义槽
      "param_b": "content_b"
    }
  ]
}
"""


def make_succ_empty_response():
    data = json.dumps({'err_code': 0, 'data_list': {}})
    return Response(data, content_type='application/json;charset=utf-8')


def make_succ_response(data):
    data = json.dumps({'err_code': 0, 'data_list': data})
    return Response(data, content_type='application/json;charset=utf-8')


def make_err_response(err_msg):
    data = json.dumps({'err_code': -1, 'err_msg': err_msg})
    return Response(data, content_type='application/json;charset=utf-8')
