from flask import Flask, render_template
from person import Person

app = Flask(__name__)
@app.route('/table')
def table():
    people = [Person('Edona','Shkodra','Data Analyst'),Person('Ana','Tirana','Programming'),
    Person('Aldo','Lushnje','Nurse'),Person('Mira','Gjirokastra','Economist'),Person('Bledi','Durres','Teacher')]
    return render_template ('table.html',PEOPLE = people)
