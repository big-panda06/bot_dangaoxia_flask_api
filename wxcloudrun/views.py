from datetime import datetime
from flask import render_template, request, jsonify
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.dao_cakes import query_cakebyid, query_cake_by_botid_and_name, insert_cake
from wxcloudrun.model import Counters
from wxcloudrun.model import Cakes
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response


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

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

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



@app.route('/api/cake/get_by_id', methods=['POST'])
def cake_get_by_id():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    id = params['id']

    if id is None:
        return make_err_response('参数错误！')

    cake = query_cakebyid(id)
    print('cake', cake)

    if cake is not None:
        return make_succ_response(jsonify(cake))
    else:
        return make_err_response('此数据不存在')


@app.route('/api/cake/get_by_botid_and_name', methods=['POST'])
def query_cake_by_botid_and_name():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    bot_id = params['bot_id']
    name = params['name']

    cake = query_cake_by_botid_and_name(id)

    if cake is not None:
        print('cake', cake)
        return make_succ_response(jsonify(cake))
    else:
        return make_err_response('此数据不存在')


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
