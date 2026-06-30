import os
import sys

FILE_PATH = 'Tasks.txt'

def read_tasks():
    with open(FILE_PATH, 'r') as f:
        tasks = f.read().splitlines()
    return tasks

def write_tasks(tasks):
    with open(FILE_PATH, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def display_menu():
        print('\n===\t\t MENU\t   ===')
        print('Type 1 - to add a task')
        print('Type 2 - to edit a task')
        print('Type 3 - to remove a task')
        print('Type 4 - to show all tasks')
        print('Type 5 - to clear all tasks')
        print('Type 6 - to exit')
        while True:
            try:
                menu = int(input('Choose an option: '))
                if menu not in (1, 2, 3, 4, 5, 6):
                    print('Invalid option.')
                else:
                    return menu
            except ValueError:
                print('Please enter a number.')

def add_task():
    user_add_task = input('Enter a task: ')
    if user_add_task == '':
        print('Task cannot be empty.')
    else:
        tasks = read_tasks()

        if user_add_task not in tasks:
            with open(FILE_PATH, 'a') as f:
                f.write(f'{user_add_task}\n')
            print('Task added successfully')
        else:
            print('Task already exists.')


def edit_task():
    old_task = input('Enter a task to edit: ')

    tasks = read_tasks()

    if old_task in tasks:
        change_task = input('With what do you want to edit your task: ')

        index = tasks.index(old_task)
        tasks[index] = change_task

        write_tasks(tasks)

        print("Task updated successfully.")
    else:
        print("Task not found.")

def remove_task():
    user_remove_task = input('Enter a task to remove: ')

    tasks = read_tasks()

    if user_remove_task in tasks:
        tasks.remove(user_remove_task)

        write_tasks(tasks)
    else:
        print('Task does not exist.')

def show_all_tasks():
    tasks = read_tasks()

    for i, task in enumerate (tasks, start=1):
        print(f'Task {i} - {task.strip()}')

def clear_all_tasks():
    with open(FILE_PATH, "w"):
        pass

    print('Tasks cleared successfully.')

def main():
    if not os.path.exists(FILE_PATH):
        open(FILE_PATH, "w").close()

    while True:
        menu = display_menu()

        if menu == 1:
            add_task()
        elif menu == 2:
            edit_task()
        elif menu == 3:
            remove_task()
        elif menu == 4:
            show_all_tasks()
        elif menu == 5:
            clear_all_tasks()
        elif menu == 6:
            sys.exit('\nExiting program with exit code: 0')


if __name__ == '__main__':
    main()