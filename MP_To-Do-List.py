tasks = []
completed_tasks = []

def daily_to_do_list():
    while True:
        print("\nWelcome to the To-Do List App!")
        print('1. Add a task')
        print('2. View Tasks')
        print('3. Mark a task as complete')
        print('4. Delete a task')
        print('5. Quit')
        choice = input("Enter your choice: ")

        if choice == "1":
            new_task = input("Please enter a new task title: ")
            tasks.append(new_task.capitalize())
            print(f"\'{new_task.capitalize()}\' has been added to your to-do list!")            
        elif choice == "2":
            print("To-do:")
            for task_view in tasks:
                print(f"- {task_view}")
            if completed_tasks:
                print(f"Completed:")
                for finished_view in completed_tasks:
                    print(f"- {finished_view}")
            else:
                print("No tasks completed yet, but still plenty of time to get something done!")
        elif choice == "3":
            print("Way to go! Which of the following tasks did you complete?")
            for task_completed in tasks:
                print(f"- {task_completed}")
            completed = input("Please select from one of the above tasks: ").capitalize()
            if completed in tasks:
                tasks.remove(completed)
                completed_tasks.append(completed)
                print(f"Way to go! \'{completed.capitalize()}\' has been checked off your to-do list!")
            else:
                print("Task to mark complete not found. Please try again")
        elif choice == "4":
            print("Days too full? No worries! Which of the following tasks would you like to remove?")
            for task_removed in tasks:
                print(f"- {task_removed}")
            task_removal = input("Please select from one of the above tasks: ").capitalize()
            if task_removal in tasks:
                tasks.remove(task_removal)
                print(f"\'{task_removal.capitalize()}\' removed from to-do list.")
            else:
                print("Task to remove not found. Please try again")
        elif choice == "5":
            print("Thanks for using our app. Hope you have a productive day!")
            break
        else:
            print("Invalid entry, please choose again")


daily_to_do_list()