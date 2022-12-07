from datetime import datetime

from flask import Flask,render_template ,redirect 
from flask import flash,session ,request ,url_for
from flask_session import Session



# ------------ Owen Lib ------------- # 
from subpython.validate import login_required
from subpython.form import LoginForm , RegisterForm
from subpython.config import Development,Production
import subpython.validate as validate

import os

app = Flask(__name__)
# app.config.from_object(Production)

app.config['SECRET_KEY'] = 'secret'


@app.route("/temp")
def temp():
    # return render_template("base.html")   
    return "hello"



@app.route("/add_new_task",methods=['POST'])
@login_required
def add_new_task():
    title = request.form.get("Task_Info")
    info = request.form.get("Task_Name")   

    if not validate.validate_tasks(title):
        return redirect('/')
    if not validate.validate_tasks(info):
        return redirect('/')
    

    # add task to user db
    new_task = Task(user_id=session['user_id'],task_info=info.title(),task_title=title.title())
    try:
        db.session.add(new_task)
        db.session.commit()
        flash("Task Added SuccessFully")
        return redirect('/')
    except:
        return error_500_server()


@app.route("/edit",methods=["POST","GET"])
@login_required
def edit():
    if request.method == "GET":
        return render_template("edit.html",post_id=request.args.get("post_id"))
    if request.method == "POST":
        # edit section
        title = request.form.get("Edit_Task_Name")
        info = request.form.get("Edit_Task_Info")
        task_id = request.form.get("post_id")

        if not validate.validate_tasks(title):
            return redirect('/')
        if not validate.validate_tasks(info):
            return redirect('/')
        if not validate.validate_tasks(task_id):
            return redirect('/')
        
        try:
            new_task = Task.query.filter_by(id=task_id).first()
            if not new_task:
                return redirect("/")

            new_task.task_title=title.title()
            new_task.task_info=info.title()
            db.session.commit()
            flash("Task Edited Successfully")
            return redirect("/")
        except:
            return error_500_server
@app.route("/delete",methods=["POST","GET"])
@login_required
def delete():
    if request.method == "GET":
        return render_template("delete.html",post_id=request.args.get('post_id'))
    if request.method == "POST":
        if request.form.get('delete') == "Yes":
            try:
                new_task = Task.query.filter_by(id=request.form.get('post_id'),user_id=session["user_id"]).first()
                if new_task == None:
                    return redirect("/")
                db.session.delete(new_task)
                db.session.commit()
                flash("Task Deleted successfully")
                return redirect("/")
            except:
                flash(message="Invalid Task",category="error")
                return redirect("/")
        else:
            return redirect("/")
    else:
        return redirect("/")
    

@app.route("/done" ,methods=["POST"])
@login_required
def done():
    if request.method == "POST":
        task_id=request.form.get("post_id")

        # query to data base for change task status to done
        new_task = Task.query.filter_by(id=task_id ,user_id=session["user_id"]).first()
        
        if new_task == None:
            return redirect("/")
        # status code 1 equal to done
        new_task.status = 1
        print(new_task.status)
        print(new_task)
        db.session.commit()
        flash("Task Done. You can See Your all Done Tasks In history Section")
        return redirect("/")            

if __name__ == '__main__':
    app.run(debug=True)           