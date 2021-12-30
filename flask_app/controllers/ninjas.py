from flask import render_template,redirect,request
from flask_app import app
from flask_app.models import ninja, dojo


@app.route('/ninjas')
def ninjas():
    return render_template("add_ninja.html", dojos = dojo.Dojo.get_all())

@app.route('/ninjas/add',methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')

# @app.route('/')
# def index():
#     return redirect('/users')

# @app.route('/users/new')
# def new():
#     return render_template("create.html")


# @app.route('/user/edit/<int:id>')
# def edit(id):
#     data ={
#         "id":id
#     }
#     return render_template("edit.html", user = User.get_one(data))

# @app.route('/user/show/<int:id>')
# def show(id):
#     data ={
#         "id":id
#     }
#     return render_template("read_one.html", user = User.get_one(data))

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