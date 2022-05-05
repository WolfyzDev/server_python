from flask import Flask, render_template, request
from flask.helpers import make_response

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/message-confirmation', methods=["POST"])
def confirmation():
    data = request.form
    print('data', data)
    email = data.get('email')
    message = data.get('message')

    print('email', email)
    print('message', message)
    return render_template('confirmation.html', **locals())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)