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
    total = len(todos)
    completed = sum(1 for task in todos if task["completed"])
    pending = total - completed

    priority_counts ={"high":0, "medium":0, "low":0}
    for task in todos:
        prio = task["priority"]
        if prio in priority_counts:
            priority_counts[prio] += 1
        else:
            priority_counts[prio] = 1

    return {
        "total_todos": total,
        "completed_todos": completed,
        "pending_todos": pending,
        "priority_counts": priority_counts
     }
result = summary_stats(todos)
print(result)