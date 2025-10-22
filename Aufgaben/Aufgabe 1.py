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

def summary_stats(todos):

     total_todos = len(todos)

     completed_todos = sum(1 for todo in todos if todo.get("completed"))

     pending_todos = sum(1 for todo in todos if not todo.get("completed"))

     priority_counts ={"high": 0,"medium": 0,"low": 0}

     for todo in todos:
         priority = todo.get("priority","").lower()
         priority_counts[priority] += 1
     else:
         priority_counts[priority] = 1

     return {
        "total_todos": total_todos,
        "completed_todos": completed_todos,
        "pending_todos": pending_todos,
        "priority_counts": priority_counts
}

def get_assigned_to(name):

    assigned_to = []
    for todo in todos:
        todo_name = todo.get("assigned_to","")
        if todo_name.lower() == name.lower():
            assigned_to.append(todo)

    return assigned_to

def get_pending_high_priority(todos):
    #  Nur offene Aufgaben behalten (completed == False)
    offene_todos = []
    for todo in todos:
        if not todo["completed"]:
            offene_todos.append(todo)

    #  Nur Aufgaben mit hoher Priorität ("high") behalten
    high_priority = []
    for todo in offene_todos:
        if todo.get("priority", "").lower() == "high":
            high_priority.append(todo)

    #  Nach Fälligkeitsdatum sortieren (Datum ist im ISO-Format)
    sortierte_todos = sorted(
        high_priority,
        key=lambda todo: datetime.strptime(todo["due_date"], "%Y-%m-%d")
    )

    #  Ergebnis zurückgeben
    return sortierte_todos

result = get_assigned_to("Sam")
#result = get_pending_high_priority(todos)
for todo in result:
    print(todo)
#for todo in result:
    #print(todo["id"], "-", todo["title"], "-", todo["due_date"])
stats = summary_stats(todos)
print(stats)