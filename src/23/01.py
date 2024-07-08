from flask import Flask, render_template, jsonify
import time
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    return jsonify({"data":[{"id":1,"ranking":1,"passwd":"password","time_to_crack_it":"< 1 Second","used_count":4929113,"year":2022},{"id":2,"ranking":2,"passwd":"123456","time_to_crack_it":"< 1 Second","used_count":1523537,"year":2022},{"id":3,"ranking":3,"passwd":"123456789","time_to_crack_it":"< 1 Second","used_count":413056,"year":2022},{"id":4,"ranking":4,"passwd":"guest","time_to_crack_it":"10 Seconds","used_count":376417,"year":2022},{"id":5,"ranking":5,"passwd":"qwerty","time_to_crack_it":"< 1 Second","used_count":309679,"year":2022}]})

if __name__ == '__main__':
    app.run()