from flask import Flask,render_template
from person import Person



@app.route('/table')
def table():
    people = []

    p1 = Person('Edona','Shkodra','Data Analyst')
    p2 = Person('Ana','Tirana','Programming')
    p3 = Person('Aldo','Lushnje','Nurse')
    p4 = Person('Mira','Gjirokastra','Economist')
    p5 = Person('Bledi','Durres','Teacher')
   return render_template ('table.html',person=PEOPLE)
