from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt, mpld3

# im = plt.imread("static/columbia_river_basin.png")
# implot = plt.imshow(im)
# fig = plt.figure(figsize = (18,8))
# plt.scatter([240,285,320,370,440,440,310,260,270,220,240,160,195,400,80,140], [150,150,150,75,85,140,80,230,130,180,130,130,80,160,100,95], c = 'g', s = 80)
# plt.title("Salmon Positions")
# plt.savefig("static/plotted_map.png")
# html_str = mpld3.fig_to_html(fig)
# Html_file= open("static/columbiaMap.html","w")
# Html_file.write(html_str)
# Html_file.close()
#<img src="https://storage.googleapis.com/very_unique_name/static/columbia_river_basin.png"/>

# This disables the requirement to use HTTPS so that you can test locally.
app = Flask(__name__)

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

@app.route('/')
@app.route('/index')
def index():
    return '''
<html>
    <head>
        <title>2018 Columbia River Chinook</title>
    </head>
    <body>
        <h1>Columbia River System Chinook Run</h1>
        <form method="POST" action="setDate">
            <input type="range" min="0" max="364" name="requestedDate" />
            <input type="submit" value="submit" />
        </form>
    </body>
</html>'''

@app.route("/setDate", methods=["POST"])
def setDate():
    inputDate = request.form["requestedDate"]
    bodyHTML = '''
<html>
    <head>
        <title>2018 Columbia River Chinook</title>
    </head>
    <body>
        <h1>Columbia River System Chinook Run</h1>
        <form method="POST" action="setDate">
            <input type="range" min="0" max="364" name="requestedDate" />
            <input type="submit" value="submit" />
        </form>
        <div>Date Selected: {{{myDate}}}</div>
    </body>
</html>'''
    return bodyHTML.format(myDate=inputDate)

if __name__ == '__main__':
    app.run()
