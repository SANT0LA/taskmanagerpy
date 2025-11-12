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

# ===============================
# 📊 ROTA DE ESTATÍSTICAS
# ===============================
from sqlalchemy import func

@app.route("/stats")
def stats():
    total = Task.query.count()
    done = Task.query.filter_by(status="done").count()
    doing = Task.query.filter_by(status="doing").count()
    pending = Task.query.filter_by(status="pending").count()

    percent_done = (done / total * 100) if total > 0 else 0

    # Converter prioridade em valores numéricos
    priority_map = {"low": 1, "medium": 2, "high": 3}
    tasks = Task.query.all()
    if tasks:
        avg_priority = sum(priority_map.get(t.priority, 0) for t in tasks) / len(tasks)
    else:
        avg_priority = 0

    # Tarefas criadas por dia (agregação SQL)
    daily_counts = (
        db.session.query(func.date(Task.created_at), func.count(Task.id))
        .group_by(func.date(Task.created_at))
        .all()
    )

    return render_template(
        "stats.html",
        total=total,
        done=done,
        doing=doing,
        pending=pending,
        percent_done=percent_done,
        avg_priority=avg_priority,
        daily_counts=daily_counts
    )

if __name__ == "__main__":
    app.run(debug=True)
