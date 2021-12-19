from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main():
    dict_user = {
        'username': '备案学习界面'
    }
    return render_template('main/index.html', user=dict_user)

@app.route('/index')
def user():
    dict_user = {
        'username': '备案学习界面'
    }
    return render_template('user/index.html', user=dict_user)


if __name__ == '__main__':
    # server = pywsgi.WSGIServer(('0.0.0.0', 8000), app)
    # server.serve_forever()
    app.run(host='0.0.0.0', port='80')
