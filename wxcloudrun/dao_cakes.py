import logging

from sqlalchemy import and_
from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.model import Cakes

# 初始化日志
logger = logging.getLogger('log')


def query_cakebyid(id):
    """
    根据ID查询cake实体
    :param id: cake的ID
    :return: cake实体
    """
    try:
        return Cakes.query.filter(Cakes.id == id).first()
    except OperationalError as e:
        logger.info("query_cakebyid errorMsg= {} ".format(e))
        return None


def query_cake_by_botid_and_name(bot_id, name):
    try:
        # return Cakes.query.filter(Cakes.bot_id == bot_id and Cakes.name == name).first()
        return Cakes.query.filter(and_(Cakes.bot_id == 'ed', Cakes.name == 'ed jones')).first()
    except OperationalError as e:
        logger.info("query_cake_by_botid_and_name errorMsg= {} ".format(e))
        return None


def delete_cakebyid(id):
    """
    根据ID删除cake实体
    :param id: cake的ID
    """
    try:
        cake = Cakes.query.get(id)
        if cake is None:
            return
        db.session.delete(cake)
        db.session.commit()
    except OperationalError as e:
        logger.info("delete_cakebyid errorMsg= {} ".format(e))


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


def update_cakebyid(cake):
    """
    根据ID更新cake的值
    :param cake实体
    """
    try:
        cake = query_cakebyid(cake.id)
        if cake is None:
            return
        db.session.flush()
        db.session.commit()
    except OperationalError as e:
        logger.info("update_cakebyid errorMsg= {} ".format(e))
