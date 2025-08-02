from flask import Flask

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    return float(celsius) * 9 / 5 + 32

@app.route('/')
def home():
    return '<h1>Hello World :)</h1>'

app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<celsius>')
def convert(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    return str(round(fahrenheit, 2))

if __name__ == '__main__':
    app.run()
