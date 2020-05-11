# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request,redirect,url_for
from person import Person
from pony.orm import Database, Required, Optional,PrimaryKey,select, db_session

app = Flask(__name__)
db = Database()

class Todo(db.Entity):
    id = PrimaryKey(int, auto = True)
    task_name = Required(str)
    duration = Required (int)
    location = Optional (str)

class Product(db.Entity):
    id = PrimaryKey(int, auto = True)
    name = Required(str)
    quantity = Required (int)
    price = Required (float)


db.bind(provider = 'sqlite', filename = 'productdb', create_db = True)
db.generate_mapping(create_tables =True)

@app.route('/todo2', methods = ['GET', 'POST'])
@db_session
def todo2():

    if request.method == 'GET':

        #to modify an object:

        task = Todo.get(task_name = 'hiking')
        #thing.duration = 10000

        if task:
            task.delete()

        new_things = list(select(t for t in Todo)) #list of query object

        return render_template('todo.html',TODO = new_things)


    elif request.method == 'POST':

        task_name = request.form.get('task_name')
        duration = request.form.get('duration')
        location = request.form.get('location')

        Todo(task_name = task_name, duration = duration, location = location) #create a new row in our table

        new_things = list (select(t for t in Todo)) #list of items that the query object retrieves

        return render_template('todo.html', TODO=new_things)





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


# Make a new route called table with endpoint '/table' that renders table.html
# Make a table html file containing a table with 3 columns: Name, City, Profession
# Make a Person class containing attributes name, city, and profession
# Make 5 objects from this class, add them to a list, and pass the list to the frontend.
# For every person, create a row in your table and display all the data.

@app.route('/table')
def table():
    people = [Person('Edona','Shkodra','Data Analyst'),
    Person('Ana','Tirana','Programming'),
    Person('Aldo','Lushnje','Nurse'),
    Person('Mira','Gjirokastra','Economist'),
    Person('Bledi','Durres','Teacher')]

    return render_template ('table.html',PEOPLE = people)


# Create todo.html, create a form with 3 inputs:
# task_name, duration, location
# make sure to extend the base and put everything inside a content block
# Create another route called todo with the endpoint "/todo"
# return the rendered todo.html


# When a request comes in, if it's a GET request , simply render the template and pass in the things list as the TODO variable
# If the request comes through the POST method, create a new dictionary containing task_name,duration,location as keys
# Add that dictionary to your list of things

things = [{'task_name':'eat', 'duration': 10, 'location': 'home'},
                {'task_name':'sleep', 'duration': 9000, 'location': 'home'}]

@app.route('/todo', methods = ['GET', 'POST'])
def todo():
    # when working with GET, use request.args.get()
    # when working with POST, use request.form.get()

     #search = request.args.get('task_name', 'eat')

    if request.method == 'GET':
        # request.args.get()
        return render_template('todo.html', TODO=things)

    elif request.method == 'POST':
        # request.form.get()

        new_dict = {'task_name': request.form.get('task_name',''),
                    'duration': request.form.get('duration',''),
                    'location': request.form.get('location','')}

        things.append(new_dict)

        # when a user sends a POST REQUEST, process the request by adding a new dictionary
        # to list of things

        return render_template('todo.html', TODO=things)


@app.route('/products', methods = ['GET', 'POST'])
@db_session
def products():

    if request.method == 'GET' :

        #http://edonaaaaa1096.pythonanywhere.com/products

        searchtext = request.args.get('SearchText','')
        result = list (select(p for p in Product if searchtext in p.name))

        return render_template('product_table.html', PRODUCT = result)

    elif request.method == 'POST' :
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        price = request.form.get('price')

        Product(name = name, quantity = quantity, price = price) #create a new row in our table

        return redirect(url_for('products'))


@app.route('/delete/<id>', methods = ['GET', 'POST'])
@db_session
def delete(id):

    if Product[id] :
        Product[id].delete()
    return redirect(url_for('products'))


@app.route('/products/<id>', methods = ['GET', 'POST'])
@db_session
def update(id):

    if id :

        p = Product[id]

        return render_template('product_update.html',PRODUCT=p)

        if request.method == 'GET' :

            if p:

                return render_template('product_update.html', PRODUCTS = p)

        elif request.method == 'POST' :

            if Product[id]:

                #id = request.form.get('id','')
                name = request.form.get('name','')
                quantity = request.form.get('quantity','')
                price = request.form.get('price','')

                Product[id].set(name=name,quantity=quantity,price=price)

                return redirect(url_for('products'))

            #Product[id].id = id
            #Product[id].name = name
            #Product[id].quantity = quantity
            #Product[id].price = price
            return 'This product does not exist'




if __name__ == '__main__':
    app.run(threaded=True,port=5000)

