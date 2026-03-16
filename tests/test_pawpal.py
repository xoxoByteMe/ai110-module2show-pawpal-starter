import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pawpal_system import Task, Pet


def test_task_completion():
    task = Task("Walk Buddy", duration=30, priority=1)
    assert task.completed == False

    task.mark_complete()
    assert task.completed == True


def test_add_task_to_pet():
    pet = Pet("Luna", "Cat")
    assert len(pet.get_tasks()) == 0

    task = Task("Feed Luna", duration=10, priority=2)
    pet.add_task(task)
    assert len(pet.get_tasks()) == 1
