# Entry point for the application.
#from . import app    # For application discovery by the 'flask' command. 
#from . import views  # For import side-effects of setting up routes. 

# Time-saver: output a URL to the VS Code terminal so you can easily Ctrl+click to open a browser
# print('http://127.0.0.1:5000/hello/VSCode')

import json
import os
from flask import request,render_template,redirect, url_for
from . import create_app, database
from .models import  Contacts , db
from datetime import datetime,timedelta
from time import gmtime, strftime
import datetime


app = create_app()

'''
import uuid
uuid.uuid4().hex
'3d6f45a5fc12445dbac2f59c3b6c7cb1'
'''
#app.secret_key = os.environ['APP_SECRET_KEY']
app.secret_key = '3d6f45a5fc12445dbac2f59c3b6c7cb1'


@app.route('/', methods=["GET", "POST"])
def home():
    contactobj = None
    if request.form:
        try:
            _name = request.form['inputName']
            _email = request.form['inputEmail']
            #_password = request.form['inputPassword']
            now = strftime("%Y-%m-%d %H:%M:%S", gmtime())

            contactobj = Contacts(name=_name, email=_email,  date_signed_up=now)
            db.session.add(contactobj)
            db.session.commit()
        except Exception as e:
            print("Failed to aded book")
            print(e)
    contactlist = Contacts.query.all()
    return render_template('postgres.html', rows=contactlist)

'''
@app.route("/")
def main():
    contactlist = Contacts.query.all()
    
    return render_template('signup.html', rows=contactlist)
    

@app.route("/success")
def success():
    return "Thank you for signing up!"


@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route('/signUp/',methods=['POST','GET'])
def signUp():
    
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    now = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    # validate the received values
    if _name and _email and _password:
        
        # All Good, let's call MySQL
        signup = Signups(name=_name, email=_email, password = _password, date_signed_up=now)
        db.session.add(signup)
        db.session.commit()
        return redirect(url_for('success'))




@app.route('/', methods=['GET'])
def fetch():
    cats = database.get_all(Cats)
    all_cats = []
    for cat in cats:
        new_cat = {
            "id": cat.id,
            "name": cat.name,
            "price": cat.price,
            "breed": cat.breed
        }

        all_cats.append(new_cat)
    return json.dumps(all_cats), 200


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    database.add_instance(Cats, name=name, price=price, breed=breed)
    return json.dumps("Added"), 200


@app.route('/remove/<cat_id>', methods=['DELETE'])
def remove(cat_id):
    database.delete_instance(Cats, id=cat_id)
    return json.dumps("Deleted"), 200


@app.route('/edit/<cat_id>', methods=['PATCH'])
def edit(cat_id):
    data = request.get_json()
    new_price = data['price']
    database.edit_instance(Cats, id=cat_id, price=new_price)
    return json.dumps("Edited"), 200
'''