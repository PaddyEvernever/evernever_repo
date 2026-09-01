print("1. Add the task\n2. Edit the task\n3. Delete the task\n4. List all tasks\n5. List task in the 'In Progress' status\n6. List task in the 'Done' status\n7. Complete the task")

def add_task(task_dict):
    task = input("Add task: ")
    deadline = input("Enter deadline: ")
    task_dict["task"] = task
    task_dict["deadline"] = deadline
    print("Task added succesfully")
    print(task_dict)

add_task({})


'''while True:
    user_input = int(input("Choose action: "))
    if user_input == 1:
        tasks['task'] = input()
    elif user_input == 2:
        tasks['deadline'] = input()
    elif user_input == 3:
        tasks['completion'] = None # I want to add "True / False" here
    elif user_input == 4:
        print(f"Your tasks: {tasks}")
        break
    else:
        print("Invalid input. Please, try again.")
        continue'''


