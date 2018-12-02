#!/usr/bin/env python

from flask import Flask, send_from_directory
import json
import yaml
import pprint

app = Flask(__name__, static_url_path='')
conferences = ''

with open("conferences.yml", 'r') as confs:
    try:
        conferences = yaml.load(confs)
        pprint.pprint(conferences)
    except yaml.YAMLError as exc:
        print(exc)

@app.route('/')
def index(filename='index.html'):
    return send_from_directory(filename)

@app.route('/get_data')
def get_data():
    print('you are here ...')
    # return json.dumps({'data': conferences })
    return json.dumps({ 'a': 123 })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8998, debug=False)

