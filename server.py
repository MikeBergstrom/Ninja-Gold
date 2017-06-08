from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key= 'ThisIsSecret'

@app.route('/')
def index():
    session['goldCount'] = 0
    session['activities'] = []
#   session['stuff'] = session['stuff']
    print session['goldCount']
    return render_template("index.html")

@app.route('/process_money', methods=['post'])
def process_money():
 if request.form['building'] == 'farm':
    goldresp = random.randint(10,20)
    print goldresp
    session['goldCount'] = session['goldCount'] + goldresp
    session['activities'].append("Earned "+ str(goldresp) + " golds from the farm! " + str(datetime.datetime.now()))
    return render_template('index.html')
 elif request.form['building'] == 'cave':
    goldresp = random.randint(5,10)
    print goldresp
    session['goldCount'] = session['goldCount'] + goldresp
    session['activities'].append("Earned "+ str(goldresp) + " golds from the cave! " + str(datetime.datetime.now()))
    return render_template('index.html')
 elif request.form['building'] == 'house':
    goldresp = random.randint(2,5)
    print goldresp
    session['goldCount'] = session['goldCount'] + goldresp
    session['activities'].append("Earned "+ str(goldresp) + " golds from the house! " + str(datetime.datetime.now()))
    return render_template('index.html')
 elif request.form['building'] == 'casino':
    goldresp = random.randint(-50,50)
    print goldresp
    if goldresp >=0:
        session['goldCount'] = session['goldCount'] + goldresp
        session['activities'].append("Entered a casino and won "+ str(goldresp) + " golds! Yipee!! " + str(datetime.datetime.now()))
        return render_template('index.html')
    elif goldresp < 50:
        session['goldCount'] = session['goldCount'] + goldresp
        session['activities'].append("Entered a casino and lost "+ str(goldresp) + " golds...ouch! " + str(datetime.datetime.now()))
        return render_template('index.html')

app.run(debug=True)