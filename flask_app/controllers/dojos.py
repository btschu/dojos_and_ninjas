from flask import render_template,redirect,request
from flask_app import app
from flask_app.models import dojo

# redirect to /dojo

@app.route('/')
def index():
    return redirect('/dojos')

# add a new dojo

@app.route('/dojos')
def dojos():
    context = {
        'dojos' : dojo.Dojo.get_all()
    }
    return render_template("dojo.html", **context)

@app.route('/dojos/create',methods=['POST'])
def create():
    dojo.Dojo.save(request.form)
    return redirect('/dojos')

# show dojo with a list of members (ninjas)

@app.route('/dojo/<int:id>')
def show(id):
    data ={
        "id":id
    }
    context = {
        'dojo' : dojo.Dojo.dojo_with_members(data)
    }
    return render_template("dojo_members.html", **context)