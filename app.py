from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Task
import os
from datetime import datetime

def create_app():
    app = Flask(__name__)
    db_path = os.path.join(os.path.dirname(__file__), "app.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

app = create_app()

with app.app_context():
    db.create_all()

# QuickSort por prioridade (high > medium > low) - implementado manualmente
PRIORITY_VALUE = {"high": 3, "medium": 2, "low": 1}

def quicksort_tasks(tasks, key_func):
    if len(tasks) <= 1:
        return tasks
    pivot = tasks[len(tasks)//2]
    pivot_key = key_func(pivot)
    left = [t for t in tasks if key_func(t) > pivot_key]
    middle = [t for t in tasks if key_func(t) == pivot_key]
    right = [t for t in tasks if key_func(t) < pivot_key]
    return quicksort_tasks(left, key_func) + middle + quicksort_tasks(right, key_func)

@app.route('/')
def index():
    tasks = Task.query.all()
    # ordenar por prioridade com QuickSort
    sorted_tasks = quicksort_tasks(tasks, key_func=lambda t: PRIORITY_VALUE.get(t.priority, 0))
    return render_template('index.html', tasks=sorted_tasks)

@app.route('/task', methods=['POST'])
def create_task():
    title = request.form.get('title')
    description = request.form.get('description')
    priority = request.form.get('priority', 'medium')
    if not title:
        return "Title required", 400
    task = Task(title=title, description=description, priority=priority)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        task.priority = request.form.get('priority')
        task.status = request.form.get('status')
        if task.status == 'done' and task.completed_at is None:
            task.completed_at = datetime.utcnow()
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

@app.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

# Endpoints API JSON (opcional)
@app.route('/api/tasks', methods=['GET'])
def api_list_tasks():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks])
