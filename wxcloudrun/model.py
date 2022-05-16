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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bot_id = db.Column(db.String)
    name = db.Column(db.String)
    price = db.Column(db.DECIMAL)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())