from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
config = {
  "apiKey": "AIzaSyAr-3AZpY_b4jdjMPDsrXeLPrnJJAmg490",
  "authDomain": "hestiapoc.firebaseapp.com",
  "projectId": "hestiapoc",
  "storageBucket": "hestiapoc.appspot.com",
  "messagingSenderId": "874274274779",
  "appId": "1:874274274779:web:254544ff8b5c83e37f3bfe",
  "measurementId": "G-QSENWPXDP6"}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'