from flask import Flask
import json
import sqlserver_connect

app = Flask(__name__)
# 通过python装饰器的方法定义一个路由地址/test/是接口的url
@app.route('/api/test')
def start():
  sqlserver_connect.connectSql()# 连接数据库
  result = sqlserver_connect.selectJson()# 取数据
  return json.dumps(result)# 发送请求 转换成JSON

if __name__ == '__main__':
  # 一个python的文件有两种使用的方法，
  # 第一是直接作为脚本执行，
  # 第二是import到其他的python脚本中被调用（模块重用）执行
  # 在if name == 'main': 下的代码只有作为脚本直接执行而import到其他脚本中不会被执行.
  app.run()# 可设置公用网络 host="0.0.0.0" 不写参数 默认本地服务