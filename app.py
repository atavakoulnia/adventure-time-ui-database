from flask import Flask, render_template, url_for, request, redirect
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/characters', methods=['POST', 'GET'])
def characters():
    return render_template('characters.html')

@app.route('/episodes', methods=['POST', 'GET'])
def episodes():
    return render_template('episodes.html')

@app.route('/music', methods=['POST', 'GET'])
def music():
    return render_template('music.html')

@app.route('/world_map', methods=['POST', 'GET'])
def world_map():
    return render_template('world_map.html')


if __name__ == "__main__":
    app.run(debug=True)