# task1
# To-Do List
class Task:
  def __init__(self,description,priority):
    self.description=description
    self.priority=priority
    self.completed=False

  def set_completed(self,completed):
    self.completed=completed

def create_task():
  description=input("Enter task description: ")
  priority=input("Enter task priority(low,medium,high): ").lower()
  tasks.append(Task(description,priority))
  print("Task created successfully!")

def view_tasks():
  if not tasks:
    print("There are no tasks in your list.")
    return
  for i,task in enumerate(tasks):
    completion_status="Completed" if task.completed else "Pending"
    print(f"{i+1} . {completion_status} - {task.priority.upper()} - {task.description}")

def mark_task_complete():
  if not tasks:
    print("There are no tasks in your list to mark complete.")
    return
  view_tasks()
  while True:
    try:
      task_number=int(input("Enter number of the task to mark complete (or 0 to go back):"))
      if task_number==0:
        return
      if 1<=task_number<=len(tasks):
        tasks[task_number-1].set_completed(True)
        print("Task marked complete successfully!")
        break
      else:
        print("Invalid task number.Please try again.")
    except ValueError:
      print("Invalid input.Please enter a number.")

def delete_task():
  if not tasks:
    print("There are no tasks in your list to delete.")
    return
  view_tasks()
  while True:
    try:
      task_number=int(input("Enter the number of task to delete(or 0 to go back):"))
      if task_number==0:
        return
      if 1<=task_number<=len(tasks):
        del tasks[task_number-1]
        print("Task deleted successsfully!")
        break
      else:
        print("Invalid task number.Please try again.")
    except ValueError:
      print("Invalid input.Please enter a number.")

tasks=[]
while True:
  print("\To-Do List Options:")
  print("1.Create a Task")
  print("2.View Tasks")
  print("3.Mark Task Complete")
  print("4.Delete Task")
  print("5.Exit")

  choice = input("Enter your choice(1-5):")
  if choice=="1":
    create_task()
  elif choice=="2":
    view_tasks()
  elif choice=="3":
    mark_task_complete()
  elif choice=="4":
    delete_task()
  elif choice=="5":
    print("Exiting To-Do List application.")
    break
  else:
    print("Invalid choice.Please enter a number between 1 and 5")








    


    
    