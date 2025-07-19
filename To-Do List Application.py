# Simple To-Do List Application
tasks = []  # store all our tasks
running = True  #loop control

print("Welcome to your To-Do List!")
print("You can add tasks, view them, mark them complete, or delete tasks.")

while running:
    # Show menu options
    print("What would you like to do?")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Exit")
    
    # Get user choice
    choice = input("Enter your choice (1-5): ")
    
    # Add new task
    if choice == "1":
        new_task = input("\nWhat task would you like to add? ")
        tasks.append({"task": new_task, "completed": False})
        print(f"'{new_task}' has been added to your list!")
    
    # View all tasks
    elif choice == "2":
        if not tasks:
            print("Your to-do list is empty!")
        else:
            print("===== YOUR TASKS =====")
            for i, task in enumerate(tasks, 1):
                if task["completed"]:
                    status = "✓"
                else:
                    status = " "
                print(f"{i}. [{status}] {task['task']}")
    
    # Mark task as complete
    elif choice == "3":
        if not tasks:
            print("Your to-do list is empty!")
        else:
            print("===== YOUR TASKS =====")
            for i, task in enumerate(tasks, 1):
                if task["completed"]:
                    status = "✓"
                else:
                    status = " "
                print(f"{i}. [{status}] {task['task']}")
            
            try:
                task_num = int(input("\nEnter the number of the task to mark complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num-1]["completed"] = True
                    task_name = tasks[task_num-1]["task"]
                    print(f"'{task_name}' has been marked complete!")
                else:
                    print("That's not a valid task number.")
            except ValueError:
                print("Please enter a number.")
    
    # Delete task
    elif choice == "4":
        if not tasks:
            print("Your to-do list is empty!")
        else:
            print("===== YOUR TASKS =====")
            for i, task in enumerate(tasks, 1):
                if task["completed"]:
                    status = "✓"
                else:
                    status = " "
                print(f"{i}. [{status}] {task['task']}")
            
            try:
                task_num = int(input("\nEnter the number of the task to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num-1)
                    print(f"'{removed_task['task']}' has been removed from your list!")
                else:
                    print("That's not a valid task number.")
            except ValueError:
                print("Please enter a number.")
    
    # Exit program
    elif choice == "5":
        print("Goodbye! Your tasks will be saved until next time.")
        running = False
    

    else:
        print("That's not a valid choice. Please enter a number between 1 and 5.")

print("Thanks for using the To-Do List!")