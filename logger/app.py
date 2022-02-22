from flask import request, render_template

from apps import create_app

app= create_app()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        username = request.form.get('name')
        ip = request.remote_addr
        if username == 'admin':
            app.logger.warning('这是一个常规信息 %s' % ip)
        else:
            app.logger.warning('这是一个警告%s' % ip)
    else:
        app.logger.error('这个是一个error测试')
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
