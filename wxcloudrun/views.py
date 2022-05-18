import json
import logging
from datetime import datetime
from flask import render_template, request, jsonify
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.dao_cakes import query_cake_by_botid_and_name, insert_cake, \
    query_cakes_by_bot_and_user_type
from wxcloudrun.dao_user_type import query_user_type_by_type
from wxcloudrun.model import Counters
from wxcloudrun.model import Cakes
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response, \
    make_succ_response_with_code

# 初始化日志
logger = logging.getLogger('log')


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/api/count', methods=['POST'])
def count():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 执行自增操作
    if action == 'inc':
        counter = query_counterbyid(1)
        if counter is None:
            counter = Counters()
            counter.id = 1
            counter.count = 1
            counter.created_at = datetime.now()
            counter.updated_at = datetime.now()
            insert_counter(counter)
        else:
            counter.id = 1
            counter.count += 1
            counter.updated_at = datetime.now()
            update_counterbyid(counter)
        return make_succ_response(counter.count)

    # 执行清0操作
    elif action == 'clear':
        delete_counterbyid(1)
        return make_succ_empty_response()

    # action参数错误
    else:
        return make_err_response('action参数错误')


@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)


@app.route('/api/cake/get_by_botid_and_name', methods=['GET'])
def cake_get_by_botid_and_name():
    bot_id = request.args.get('bot_id')
    name = request.args.get('name')

    cake = query_cake_by_botid_and_name(bot_id, name)

    if cake is not None:
        data = [{'cake_price': cake.price}]
        return make_succ_response(data)
    else:
        return make_err_response("不存在此数据")


@app.route('/api/cake/get_by_bot_and_user_type', methods=['GET'])
def get_cakes_by_bot_and_user_type():
    bot_id = request.args.get('bot_id')
    user_type = request.args.get('user_type')
    cakes = query_cakes_by_bot_and_user_type(bot_id, user_type)
    if cakes is not None:
        data = []
        for cake in cakes:
            data.append({'cake_name': cake.name, 'cake_price': cake.price,
                         'cake_sweetness': cake.sweetness, 'cake_size': cake.size, 'cake_desc': cake.desc})
        return make_succ_response(data)
    else:
        return make_err_response("不存在此数据")


@app.route('/api/cake/add', methods=['POST'])
def cake_add():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    bot_id = params['bot_id']
    name = params['name']
    price = params['price']

    cake = Cakes()
    cake.bot_id = bot_id
    cake.name = name
    cake.price = price
    cake.created_at = datetime.now()
    cake.updated_at = datetime.now()
    insert_cake(cake)
    return make_succ_response('插入成功')


@app.route('/api/user_type/get_standard_user_type', methods=['GET'])
def get_standard_user_type():
    user_type = request.args.get('user_type')

    user_type_obj = query_user_type_by_type(user_type)

    if user_type_obj is not None:
        data = [{'standard_user_type': user_type_obj.standard_user_type}]
        err_code = 0

        if user_type_obj.standard_user_type == '儿子':
            err_code = 1
        elif user_type_obj.standard_user_type == '女儿':
            err_code = 2
        elif user_type_obj.standard_user_type == '男朋友':
            err_code = 3
        elif user_type_obj.standard_user_type == '女朋友':
            err_code = 4
        elif user_type_obj.standard_user_type == '长辈':
            err_code = 5
        else:
            err_code = 6

        return make_succ_response_with_code(data, err_code)
    else:
        err_code = 6
        data = [{'standard_user_type': '其他'}]
        return make_succ_response_with_code(data, err_code)
