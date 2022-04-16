from flask import Flask, render_template, request, redirect
from database import insert_data
import datetime
app = Flask(__name__)  # creating flask app name


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")


@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")


@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

# creating a route getting the post data and calling the database.py file


@app.route('/store', methods=['GET', 'POST'])
def store():
    stat = "404"
    if request.method == 'POST':
        data = request.get_json()
        if data['name'] and data['email'] and data['phone']:
            name, email, phone = data['name'], data['email'], data['phone']
            print("Data: ")
            print(name, email, phone)
            # get current data and time in 12 hour and human readable format
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            period = current_date + " | " + current_time
            stat = insert_data(name, email, phone, period)
        else:
            stat = "400"
    return stat


if(__name__ == "__main__"):
    app.run()
