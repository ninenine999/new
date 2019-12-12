# import pymysql
# conn= pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='abc123',db='test')
# cursor = conn.cursor()
# cursor.execute("select * from emp")
# #一条条取
# row_1 = cursor.fetchone()
# row_2 = cursor.fetchone()
#
# #取前几行数据
# row_3 = cursor.fetchmany(3)
# row_4 = cursor.fetchall()
# print(row_1)
# print(row_2)
# print(row_3)
# print(row_4)
# conn.close()

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper
#创建链接
engine = create_engine("mysql+pymysql://root:abc123@localhost/test",encoding='utf-8', echo=True)
Base = declarative_base()  # 生成orm基类
#
#
# class User(Base):
#     __tablename__ = 'user'  # 表名
#     id = Column(Integer, primary_key=True)
#     name = Column(String(32))
#     password = Column(String(64))
#
#
# Base.metadata.create_all(engine)  # 创建表结构
metadata = MetaData()

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('fullname', String(50)),
             Column('password', String(12))
             )


class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password


mapper(User, user)

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

user_obj = User(name="alex", password="alex3714")  # 生成你要创建的数据对象
print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None

Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
print(user_obj.name, user_obj.id)  # 此时也依然还没创建

Session.commit()  # 现此才统一提交，创建数据
