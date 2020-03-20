from yahoo_fin import stock_info as si
import time 
from flask import Flask
from flask import jsonify

app = Flask(__name__)

def getLosers():
    x = si.get_day_losers()
    print(x)

while True:
    getLosers()
    time.sleep(10)

#@app.route('/')
#def home():

@app.route('/losersData')
def stockLosers():
    return jsonify(x)

if __name__ == "__main__":
    app.run(debug = True)