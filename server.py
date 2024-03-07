from flask import Flask
import check

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/<name>?<location>&<birthday>&<rand>')
def trans(name, location, birtday, rand):

    return check.check(name, location, birtday, rand)

if __name__ == '__main__':
    app.run(debug=True)
