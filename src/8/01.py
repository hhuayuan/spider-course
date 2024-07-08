#coding=utf-8
# 导入Flask模块
from flask import Flask
# 创建一个Flask应用
app = Flask(__name__)

# 定义一个路由/，接口返回文本‘spiderbuf’
@app.route('/')
def index():
    return 'spiderbuf'

# 运行程序
if __name__ == '__main__':
    app.run()

