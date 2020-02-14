from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'bjasfub'


@app.route('/', methods=['GET','POST'])
def hello_world():
    return render_template('page/index.html')

@app.route('/iftest', methods=['GET','POST'])
def iftest():
    if request.method == 'POST':
        request_url = request.form.get('request_url')
        request_method = request.form.get('request_method')
        print(request_url,request_method)
    return render_template('page/IFTest.html')


if __name__ == '__main__':
    app.run()
