from flask import Flask, render_template, url_for, request, redirect
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/episodes', methods=['POST', 'GET'])
def episodes():
    return render_template('episodes.html')


if __name__ == "__main__":
    app.run(debug=True)