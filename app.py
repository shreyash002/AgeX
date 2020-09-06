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

@app.route('/postmethod', methods=['POST'])
def my_map():
    mymap = Map(
                identifier="view-side",
                varname="mymap",
                style="height:720px;width:1100px;margin:0;", # hardcoded!
                lat=37.4419, # hardcoded!
                lng=-122.1419, # hardcoded!
                zoom=15,
                markers=[(37.4419, -122.1419)] # hardcoded!
            )

    return render_template('example.html', mymap=mymap)

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
    print(time)
    print(comments)
    return render
if __name__ == '__main__':
    app.run(debug = True) # run app