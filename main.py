import requests
from lxml import etree
import pymysql
from DBConnection import DBconn
import re

#创建数据库连接
conn = DBconn.DBconn()
#定义游标
cur = conn.cursor()

#定义正则
pat = "\w+"

#伪装浏览器
headers_dict={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/86.0.4240.75 Safari/537.36 "

}

for p in range(1,148):
    url = "http://www.hrm.cn/jobs?keyType=0&keyWord=&jobTypeId=&jobType=&industry=&industryname=&workId=&workPlace=&salary=&entType=&experience=&education=&entSize=&benefits=&reftime=&workTypeId=&sortField=&pageNo="+str(p)
    res = requests.get(url=url,headers = headers_dict)
    #将获得的html内容转换成标准的HTML
    sele = etree.HTML(res.text)
    #提取岗位名称
    position = sele.xpath("//span[@class='jobs_name_list_name']/text()")
    #提取招聘单位
    corps = sele.xpath("//li[@class='list_com_name']/a/text()")
    #提取薪酬
    salarys = sele.xpath("//div[@class='list_jobs_box list clearfix']/ul/li[@class='list_jobs_salary']/text()")

    for i in range(0,len(position)):
        if (len(position) == 0):
            continue
        else:
            gw = position[i]
            gs = corps[i]
            xs = salarys[i]
            xs1=xs.strip()
            xse=xs1.replace(" ","")
            print(xse)
            sql = "insert into job(position ,corp,salary) values('"+gw+"','"+gs+"','"+xs+"')"
            cur.execute(sql)
            conn.commit()

conn.close()

