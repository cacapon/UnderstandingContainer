from flask import Flask, request, abort
from socket import gethostbyname
from hoge.ret_str import RetStr

app = Flask(__name__)
test = RetStr()


# 許可するIP一覧
ACCEPTED_IP = [gethostbyname('public_container')]


def ip_check(func):
    def wrapper(*args, **kwargs):
        if request.remote_addr in ACCEPTED_IP:
            print('IP Check : OK')
            return func(*args, **kwargs)
        else:
            print(request.remote_addr)
            return abort(403)
    return wrapper


@app.route('/private', methods=['GET'])
@ip_check
def hello_world():
    return test.data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
