import pymysql

# 创建连接
db=pymysql.connect(host='120.77.182.221',port=3306,user='root',passwd='tds2018888 ',db='liaoshequ',charset='utf8')
# cur = db.cursor()
# create_table_sql='''select * from chat_room_material'''
# cur.execute(create_table_sql)
# cur.close()      # 关闭游标
# db.close()     # 关闭数据库连接