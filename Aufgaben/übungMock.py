from datetime import datetime

todos = [
    {"id": 1, "title": "Write unit tests", "completed": False,
     "due_date": "2025-04-10", "priority": "high",
     "tags": ["testing", "backend"], "assigned_to": "Ashley"},

    {"id": 2, "title": "Design homepage mockup", "completed": True,
     "due_date": "2025-04-05", "priority": "medium",
     "tags": ["design", "frontend"], "assigned_to": "Frank"},

    {"id": 3, "title": "Fix login bug", "completed": False,
     "due_date": "2025-04-08", "priority": "high",
     "tags": ["bugfix", "backend"], "assigned_to": "Sam"},

    {"id": 4, "title": "Update documentation", "completed": False,
     "due_date": "2025-04-12", "priority": "low",
     "tags": ["docs"], "assigned_to": "Ashley"},

    {"id": 5, "title": "Optimize images", "completed": True,
     "due_date": "2025-04-07", "priority": "medium",
     "tags": ["performance", "frontend"], "assigned_to": "Frank"},
]
def get_pending_high_priority(todos):
    offene_todos = [todo for todo in todos if not todo["completed"]]
    high_priority = [todo for todo in offene_todos if todo.get("priority", "").lower() =="high"]

    sortierte_todos = sorted(
        high_priority,
        key=lambda todo: datetime.strptime(todo["due_date"], "%Y-%m-%d")
    )
    return sortierte_todos

result = get_pending_high_priority(todos)
for todo in result:
    print(todo)
