from flask import Flask, render_template, url_for, request, redirect
import requests
import os
from IMDB_scraper.socket_client import receive, send
from IMDB_scraper.IMDB_Scraper import imdb


app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/episodes', methods=['POST', 'GET'])
def episodes():

    return render_template('episodes.html')


if __name__ == "__main__":
    app.run(debug=True)
