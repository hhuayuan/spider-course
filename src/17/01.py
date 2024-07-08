# coding=utf-8
# 导入Flask模块
from flask import Flask, render_template, request, jsonify

# 创建一个Flask应用
app = Flask(__name__)

# 定义一个路由/，接口返回网页
@app.route('/')
def index():
    return render_template('index.html')

# 运行程序
if __name__ == '__main__':
    app.run()

