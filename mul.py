from flask import Flask

app= Flask(__name__)
@app.route('/mul/<int:variable1>/<int:variable2>')
def multi(a,b):
    return a*b

@app.route('/')
def hi():
    return 'Welcome to Calculator!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
