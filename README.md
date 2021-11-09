***A Website dedicated to honoring the TV show Adventure Time.***

------------------------------------

**Steps on how to run app.py**

1. Open terminal and type “cd /Users/<username>/Documents" (or wherever else you want to save the project)
2. Then type “git clone https://github.com/atavakoulnia/adventure_time_fanpage” to clone the project into that folder
3. Open the adventure_time_fanpage folder in VScode
4. Open a new terminal in VScode and make sure you are in the root project directory (cd /Users/<username>/Documents/adventure_time_fanpage)
5. Run “pip3 install virtualenv” to install the virtual environment
6. Then run "python3 -m venv ./venv”
7. Now, activate the virtual environment by running “source ./venv/bin/activate”
8. Run “pip3 install -r requirements.txt” to install the packages required to run the project
9. Run "python3 socket_server.py" to start the server
9. Finally, run “python3 app.py” and boom it should work! 