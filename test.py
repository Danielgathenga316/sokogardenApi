from flask import *

# initialize the flask app
app=Flask(__name__)

# create route
@app.route('/api/home')
def home():
    return jsonify({'Message':'Welcome to home Api'})

# create the product route
@app.route('/api/product')
def product():
    return jsonify({'message':'Welcome to product Api'})

# create the sing ervices route
@app.route('/api/services')
def services():
    return jsonify({'Message':'Welcome to services Api'})

# Route for adding two numbers
@app.route('/api/calc',methods=['post'])
def calc():
    # request the data 
    num1=request.form['num1']
    num2=request.form['num2']

    sum=int(num1)+int(num2)

    

    return jsonify({'Answer':sum})

    # Route for multiply two numbers
@app.route('/api/multiply',methods=['post'])
def multiply():
    # request the data 
    num1=request.form['num1']
    num2=request.form['num2']

    multiplication=int(num1)*int(num2)

    

    return jsonify({'Answer':multiplication})

app.run(debug=True)
    