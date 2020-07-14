from flask import Flask,render_template, redirect, url_for,session,flash,get_flashed_messages
from app import app,db
import form

from models import Task
from datetime import datetime

@app.route("/")
@app.route("/index")
def index():
    tasks = Task.query.all()
    return render_template("index.html",tasks = tasks)


@app.route("/add", methods= ['POST','GET'])
def add():
    formm  = form.AddTaskForm()
    if(formm.validate_on_submit()):
        t = Task(title = formm.title.data, date = datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash('Task Added To DataBase')
        return redirect(url_for('index'))

    return render_template("add.html",form = formm)


@app.route("/edit/<int:task_id>", methods = ["GET","POST"])
def edit(task_id):
    task = Task.query.get(task_id)
    formm  = form.AddTaskForm()

    if(task):
        if(formm.validate_on_submit()):
            task.title = formm.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash("Task has been updated")
            return redirect(url_for('index'))

        formm.title.data = task.title
        return render_template("edit.html", form =formm, task_id =task_id)
    else:
        flash("Task Not Found")
    return redirect(url_for('index'))

@app.route("/delete/<int:task_id>", methods = ["GET","POST"])
def delete(task_id):
    task = Task.query.get(task_id)
    formm  = form.DeleteTaskForm()

    if(task):
        if(formm.validate_on_submit()):
            db.session.delete(task)
            db.session.commit()
            flash("Task has been Deleted")
            return redirect(url_for('index'))


        return render_template("delete.html", form =formm, task_id =task_id, title = task.title)
    else:
        flash("Task Not Found")
    return redirect(url_for('index'))
