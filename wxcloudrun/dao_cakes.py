import logging

from sqlalchemy import and_
from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.dao_user_type import query_user_type_by_type
from wxcloudrun.model import Cakes

# 初始化日志
logger = logging.getLogger('log')


def query_cake_by_botid_and_name(bot_id, name):
    try:
        # return Cakes.query.filter(Cakes.bot_id == bot_id and Cakes.name == name).first()
        return Cakes.query.filter(and_(Cakes.bot_id == bot_id, Cakes.name == name)).first()
    except OperationalError as e:
        logger.info("query_cake_by_botid_and_name errorMsg= {} ".format(e))
        return None


def query_cakes_by_bot_and_user_type(bot_id, user_type):
    try:
        user_type_obj = query_user_type_by_type(user_type)

        if user_type_obj is not None and user_type_obj.standard_user_type != '其他':
            # 查询指定用户类型的推荐列表
            return Cakes.query.filter(and_(Cakes.bot_id == bot_id, Cakes.user_type == user_type_obj.standard_user_type))
        else:
            # 返回所有的蛋糕列表（通用）
            return Cakes.query.filter(Cakes.bot_id == bot_id)
    except OperationalError as e:
        logger.info("query_cakes_by_bot_and_user_type errorMsg= {} ".format(e))
        return None


def insert_cake(cake):
    """
    插入一个cake实体
    :param cake: Cakes实体
    """
    try:
        db.session.add(cake)
        db.session.commit()
    except OperationalError as e:
        logger.info("insert_cake errorMsg= {} ".format(e))
