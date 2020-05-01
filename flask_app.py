
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
# redirect, url_for
from person import Person

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Edona!'

@app.route('/profile')
def profile():
    return 'This is the profile page.'

"""
@app.route('/profile')
def profile():
    return redirect(url_for('.index'))
"""

@app.route('/index')
def index():
    x = [10,20,30]
    y = {'name' : 'Edona' , 'profession' : 'data analyst' }
    z = ['hello' , 'everybody' ]

    return render_template('index.html', NUMBERS = x, PERSON = y, WORDS = z)

"""
@app.route('/index')
def index():
    return render_template('index.html')
"""
@app.route('/forms', methods = ['GET', 'POST'])
def forms():
    if request.method == 'GET':

        return render_template('forms.html')

    elif request.method == 'POST':

        name = request.form.get('last_name')
        return f'hello {name}'


@app.route('/table')
def table():
    people = [Person('Edona','Shkodra','Data Analyst'),
    Person('Ana','Tirana','Programming'),
    Person('Aldo','Lushnje','Nurse'),
    Person('Mira','Gjirokastra','Economist'),
    Person('Bledi','Durres','Teacher')]

    return render_template ('table.html',PEOPLE = people)


