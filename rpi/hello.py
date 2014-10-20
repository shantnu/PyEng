from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/<string:name>")
def hello_name(name):
    hello = "Hello " +  name
    return hello

# For the RPI    
#app.run(host='0.0.0.0', port=80, debug=True)

# For testing on a normal Pc
app.run(debug=True)
