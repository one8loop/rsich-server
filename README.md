# rsich-server
Dummy server implemented using Flask framework for the RSI Interactive Application made in the context of the HackTheCity 2018 hackaton (Lugano - Apr, 27-29).

Setup guide:

1. Install python-3.6 and virtualenv
2. Create a new virtual environment and activate it by exectuting
```
virtualenv RSI_Server
cd RSI_Server
source bin/activate
```
  This will create a new RSI_Server folder and prepare a fresh python environment with pip automatically installed.

3. Install Flask-restful
```
pip install flask-restful
```

4. Clone this repository in an 'app' folder
```
git clone https://github.com/one8loop/rsich-server.git app
```

5. Create a Sqlite3 database for the server application
```
cd app
sqlite3 RSI.db
python setupdb.py
```

6. Execute the server
```
python server.py
```

It will listen on http://127.0.0.1:5000/
