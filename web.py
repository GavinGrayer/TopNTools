
from flask import Flask,jsonify,request,json

import SplitWords

app = Flask(__name__)

'''
    使用  http://127.0.0.1:8777/split?data=*************
    词频分析API接口
'''

@app.route('/split',methods=['POST'])
def index2():
    data = request.args.get('data')
    # print('test::::'+data)
    data1 = SplitWords.split(data)
    return jsonify(data1)


if __name__ == '__main__':
    app.run(debug=True, port=8777)