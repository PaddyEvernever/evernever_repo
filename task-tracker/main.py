print("1. Add the task\n2. Add the deadline\n3. Mark the status\n4. Exit")

def add_task(task_dict):
    task = input("Add task: ")
    deadline = input("Enter deadline")
    

while True:
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
        continue


