from flask import Flask, render_template, request

from app.main.basePage import BasePage

app = Flask(__name__)
bp = BasePage()
app.secret_key = 'bjasfub'


@app.route('/', methods=['GET','POST'])
def hello_world():
    return render_template('page/index.html')

@app.route('/iftest', methods=['GET','POST'])
def iftest():
    res_test = ''
    if request.method == 'POST':
        request_url = request.form.get('request_url')
        request_method = request.form.get('request_method')
        request_boby = request.form.get('request_boby')
        res = bp.send_requests(request_url,request_method,request_boby)
        print(request_url,request_method,request_boby,res.text)
        res_test = res.text
    return render_template('page/IFTest.html',res_test=res_test)


if __name__ == '__main__':
    app.run()
