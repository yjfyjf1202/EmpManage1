import pymysql

def DBconn():
    #创建数据库连接
    conn = pymysql.connect(host="localhost",db="empmana",user="root",passwd="123456",charset="utf8")
    #定义游标
    cur = conn.cursor()
    return conn