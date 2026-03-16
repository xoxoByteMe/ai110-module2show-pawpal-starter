from pawpal_system import Owner, Pet, Task, Scheduler

# --- Setup ---
owner = Owner("Alex")

dog = Pet("Buddy", "Dog")
cat = Pet("Luna", "Cat")

owner.add_pet(dog)
owner.add_pet(cat)

# --- Tasks ---
dog.add_task(Task("Walk Buddy",  duration=30, priority=1))
dog.add_task(Task("Brush Buddy", duration=15, priority=3))
cat.add_task(Task("Feed Luna",   duration=10, priority=2))

# --- Schedule ---
scheduler = Scheduler(owner)
plan = scheduler.generate_daily_plan()

# --- Output ---
print("=" * 42)
print("       Today's Pet Care Schedule")
print(f"             Owner: {owner.name}")
print("=" * 42)

for i, task in enumerate(plan, start=1):
    status = "✓" if task.completed else "○"
    print(f"  {i}. [{status}] {task.description}")
    print(f"       Duration : {task.duration} min")
    print(f"       Priority : {task.priority}")
    print()

total_time = sum(task.duration for task in plan)
print("-" * 42)
print(f"  Total time needed : {total_time} minutes")
print("=" * 42)
