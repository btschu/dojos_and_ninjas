from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template("dojo.html", dojos = Dojo.get_all())

@app.route('/dojos/create',methods=['POST'])
def create():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template("dojo_members.html", dojo = Dojo.dojo_with_members(data))

# @app.route('/users/new')
# def new():
#     return render_template("create.html")


# @app.route('/user/edit/<int:id>')
# def edit(id):
#     data ={
#         "id":id
#     }
#     return render_template("edit.html", user = User.get_one(data))


# @app.route('/user/update',methods=['POST'])
# def update():
#     User.update(request.form)
#     return redirect('/users')

# @app.route('/user/delete/<int:id>')
# def delete(id):
#     data = {
#         'id': id
#     }
#     User.delete(data)
#     return redirect('/users')