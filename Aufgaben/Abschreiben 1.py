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
    # Nur offene Aufgaben behalten (completed == False)
    offene_todos =[]
    for todo in todos:
        if not todo["completed"]:
            offene_todos.append(todo)

    # Nur Aufgaben mit hoher Priorität ("high") behalten
    high_priority = []
    for todo in offene_todos:
        if todo.get("priority","").lower() == "high":
            high_priority.append(todo)

    # Nach Fälligkeitsdatum sortieren (Datum ist im ISO-Format)
    sortierte_todo = sorted(
        high_priority,
        key=lambda t:datetime.strptime(t["due_date"],"%Y-%m-%d")
    )

    # Ergebnis zurückgeben
    return sortierte_todo

#Funktion testen,
result = get_pending_high_priority(todos)

#Ausgabe prüfen,
for todo in result:
    print(todo["id"],"-",todo["title"],"-",todo["due_date"])
