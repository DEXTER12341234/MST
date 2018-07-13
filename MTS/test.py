from flask import *
import requests
from bs4 import BeautifulSoup as bs
import urllib.request

app=Flask(__name__)

@app.route('/static',methods=['GET'])
def submit