from application import app
from flask import render_template, jsonify, request
from application import api, db
from flask_restful import Resource , marshal_with , fields
from application.models import schedule

getTasks = {
    'tasks':fields.String,
    'date':fields.String,
    'time':fields.String,
    'description':fields.String
}

class allTasks(Resource):
    @marshal_with(getTasks)
    def get(self):
        tasks = schedule.query.all()
        return tasks

    @marshal_with(getTasks)
    def post(self):
        print(request.form)
        new_task = schedule(task=request.form['tasks'], date=request.form['date'],
                            description=request.form['description'])
        db.session.add(new_task)
        db.session.commit()
        tasks = schedule.query.all()
        return tasks

class updateTask(Resource):
    @marshal_with(getTasks)
    def put(self,task_name):
        queried_task = schedule.query.filter_by(task=task_name).first()
        queried_task.task = request.form['tasks']
        queried_task.date = request.form['date']
        queried_task.description = request.form['description']
        db.session.commit()
        return queried_task

class deleteTask(Resource):
    @marshal_with(getTasks)
    def delete(self,task_name):
        queried_task = schedule.query.filter_by(task=task_name).first()
        db.session.delete(queried_task)
        all_tasks = schedule.query.all()
        return all_tasks

api.add_resource(allTasks, '/')
api.add_resource(deleteTask,'/deletetask/<task_name>')
api.add_resource(updateTask,'/updatetask/<task_name>')

