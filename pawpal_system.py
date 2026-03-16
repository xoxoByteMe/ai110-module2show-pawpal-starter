class Task:
    """Represents a single pet care activity."""

    def __init__(self, description, duration, priority):
        self.description = description
        self.duration = duration      # in minutes
        self.priority = priority      # lower number = higher priority
        self.completed = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def __str__(self):
        """Return a readable summary of the task."""
        status = "Done" if self.completed else "Pending"
        return f"[Priority {self.priority}] {self.description} ({self.duration} min) - {status}"


class Pet:
    """Represents a pet owned by the user."""

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.tasks = []

    def add_task(self, task):
        """Add a Task object to this pet's task list."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return the list of tasks for this pet."""
        return self.tasks


class Owner:
    """Represents the user who owns one or more pets."""

    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        """Add a Pet object to the owner's list of pets."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks across every pet the owner has."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    """Organizes an owner's pet care tasks into a daily plan."""

    def __init__(self, owner):
        self.owner = owner

    def get_all_tasks(self):
        """Retrieve all tasks from the owner."""
        return self.owner.get_all_tasks()

    def generate_daily_plan(self):
        """Return all tasks sorted by priority (lowest number first)."""
        return sorted(self.get_all_tasks(), key=lambda task: (task.priority, task.duration))

    def explain_plan(self):
        """Print a human-readable version of the daily care plan."""
        plan = self.generate_daily_plan()
        if not plan:
            print("No tasks scheduled for today.")
            return

        print(f"\nDaily Care Plan for {self.owner.name}:")
        print("-" * 40)
        for i, task in enumerate(plan, start=1):
            print(f"{i}. {task}")
        print("-" * 40)
        total = sum(task.duration for task in plan)
        print(f"Total time needed: {total} minutes")
