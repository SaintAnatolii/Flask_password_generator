import requests
from flask import Flask, render_template, url_for, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        passlen = request.form.get('passlen')
        uppercase = request.form.get('uppercase')
        numbers = request.form.get('numbers')
        special = request.form.get('special')
        default_password = 'abcdefghijklmnopqrstuvwxyz'
        password = ''
        if uppercase:
            default_password += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if numbers:
            default_password += '0123456789'
        if special:
            default_password += '!@#$%&*№|'
        default_password = list(default_password)
        for i in range(int(passlen)):
            password += random.choice(default_password) 
        return render_template('index.html', password=password)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

