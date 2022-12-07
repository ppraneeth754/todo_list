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

if __name__ == '__main__':
    app.run(debug=True)   

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

         