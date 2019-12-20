#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import MySQLdb
import sys,urllib,urllib2
import commands
import json
#避免译码问题
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

app = Flask(__name__)
#以下三行打开uwsgi debug模式
from werkzeug.debug import DebuggedApplication
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
app.debug = True


#测试用       
@app.route('/student', methods=['GET', 'POST'])
def home():
    return '<h1>HomePage</h1>'

#输出表单form    
@app.route('/student/chengji', methods=['GET'])
def chengji_form():
    return json.dumps("test")

#处理表单提交信息，查询数据库，输出结果 
@app.route('/student/query', methods=['POST'])
def query():
    ClassName=request.form['ClassName']
    TestLevel=request.form['TestLevel']
    if ClassName=='': 
        ClassName="1807"
    if TestLevel=='':
        TestLevel='1'
  #  try:
  #测试代码
  #print TestLevel
    conn=MySQLdb.connect(host='192.168.31.140',user='yanght',passwd='yanght',db='students',port=3306,charset='utf8')
    cur=conn.cursor()
	#查询成绩的SQL
    sql1=("select a.name,b.* from base as a,chengji as b where a.stud_no=b.stud_no and a.stud_no like '"+ClassName+"%'")
	#查询基本信息的SQL
    sql=("select * from base order by stud_no")
    if TestLevel == '1' :
        sql=sql1

    count=cur.execute(sql)

    #字段名在index中
    index = cur.description
    result = []
	#所有记录行在result中
    result=cur.fetchall()

  

   #关闭连接
    conn.commit()
    cur.close()
    conn.close()
   # except MySQLdb.Error,e:
   #     ret= "Mysql Error %d: %s" % (e.args[0], e.args[1])
  #  content=text_content+ret
    context = {}
    context['sql']=sql
    context['count']=count
    context['index']=index
    context['result']=result
    context = json.dumps(context)
    print(context)    
   # return render_template("student.html",sql=sql,count=count,index=index,result=result)
    return context


if __name__ == '__main__':
    app.run()
