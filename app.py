from flask import Flask, render_template, url_for, request, redirect
import requests
import os
import socket
import pickle
# ---------------------------------------------------------------------------------------
#                                   Configuration
# ---------------------------------------------------------------------------------------
app = Flask(__name__)
scraper = []
# ---------------------------------------------------------------------------------------
#                                   Home Page 
# ---------------------------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')
# ---------------------------------------------------------------------------------------
#                                   Episodes Page 
# ---------------------------------------------------------------------------------------
@app.route('/episodes', methods=['POST', 'GET'])
def episodes():
        return render_template('episodes.html')

@app.route('/search_results', methods=['POST'])
def search_results():
    if request.method == "POST":
        season = request.form.get("season")
        episode = request.form.get("episode")

        FORMAT = 'utf-8'

        #create a client 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), 5102))
        print("Connecting to server")
        print("Sending request")

        #function to receive reply from server
        def receive():
            msg = s.recv(1024)
            data = pickle.loads(msg)    #serialize using pickle
            scraper.append(data)
            # print(scraper)

        #function to send request to server
        def send(msg):
            data = pickle.dumps(msg)
            s.send(data)

        send(["tt1305826", season, episode])  #send a list of 3 inputs: IMDB's ID, season #, episode #
        receive()
        
        return render_template('search_results.html', scraper=scraper)
    else:
        return render_template('episodes.html')
# ---------------------------------------------------------------------------------------
#                                       Listener
# ---------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
