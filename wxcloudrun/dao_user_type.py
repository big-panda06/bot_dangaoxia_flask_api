import logging

from sqlalchemy.exc import OperationalError

from wxcloudrun import db
from wxcloudrun.model import UserType

# 初始化日志
logger = logging.getLogger('log')


def query_user_type_by_type(user_type):
    """
    查询用户类型
    :param user_type: 用户类型
    :return: 归一化的用户类型
    """
    try:
        return UserType.query.filter(UserType.user_type == user_type).first()
    except OperationalError as e:
        logger.info("query_user_type_by_type errorMsg= {} ".format(e))
        return None


