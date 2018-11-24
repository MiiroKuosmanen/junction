from flask import Flask
from flask import request
import pandas as pd

from flask import Flask, request


#eval does good
app = Flask(__name__)

df = pd.read_csv('./customers/customers_0_4.csv')
df = df.loc[df['CustomerID'] == 1]

#####
def summarize_data():
    print(df.head())

@app.route("/output")
def output():
	return "Hello World!"

@app.route("/login")
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    return(username)

@app.route("/commands")
def commands():
    command = request.args.get('command')

    if command == "head":
        # return first few rows of data
        #return(summarize_data())
        df.to_csv("test_file.csv")

    if command == "update":
        # Recalculate using new params
        pass
    
    if command == 'read':
        return app.send_static_file('./test_file.csv')



#####


if __name__ == "__main__":
	app.run()
