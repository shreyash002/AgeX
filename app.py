#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps, Map

app = Flask(__name__)

GoogleMaps(app, key="my-key")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aggregator')
def aggregator():
    return render_template('map.html')

@app.route('/aggregatorNext')
def aggregatorNext():
    return render_template('aggregator.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/companion')
def companion():
    return render_template('aggregator.html')

@app.route('/getNurse', methods=['POST'])
def getNurse():
    name = request.form.get('name')
    time = request.form.get('time')
    comments = request.form.get('comments')
    print(name)
    import re
    timeTemp = re.split('T', time)
    print(timeTemp)
    date = timeTemp[0]
    time = timeTemp[1]
    print(comments)

    return render_template('nurseConfirm.html', name=name, date=date, time=time,comments=comments)
if __name__ == '__main__':
    app.run(debug = True) # run app