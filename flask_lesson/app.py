from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hallo, Welt!"

@app.route("/impressum")
def impressum():
    return "Hier müssen eigentlich das <b> Impressum </b> stehen"

@app.route("/greet/<username>")
def greet():
    return f"Willkommen auf meine Seite, {username}"

@app.route("/square/<int:number>")
def square(number):
    return f"Das Quadrat von {number} ist {number ** 2}"

@app.route("/unicorn")
def show_unicorn():
    return 
if __name__ == "__main__":
    app.run(debug=True)
