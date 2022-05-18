from datetime import datetime

from wxcloudrun import db


# 计数表
class Counters(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Counters'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=1)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())


# 蛋糕
class Cakes(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Cakes'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    bot_id = db.Column(db.String)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    sweetness = db.Column(db.Integer, default=0)
    desc = db.Column(db.String)
    size = db.Column(db.String)
    user_type = db.Column('userType', db.String)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())


# 用户类型
class UserType(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'UserType'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column('userType', db.String)
    standard_user_type = db.Column('standardUserType', db.String)