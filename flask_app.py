
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from person import Person

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Edona!'

@app.route('/profile')
def profile():
    return 'This is the profile page.'


@app.route('/table')
def table():
    people = [Person('Edona','Shkodra','Data Analyst'),
    Person('Ana','Tirana','Programming'),
    Person('Aldo','Lushnje','Nurse'),
    Person('Mira','Gjirokastra','Economist'),
    Person('Bledi','Durres','Teacher')]

    return render_template ('table.html',PEOPLE = people)


