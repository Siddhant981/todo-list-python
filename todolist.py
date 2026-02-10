# make TODO List from python 

def menu():
    print("Option 1: Add Task")
    print("Option 2: View Task")
    print("Option 3: Delete Task")
    print("Option 4: Exit")


def Add_task():
    with open("TodoList.txt","r") as f:
        data = f.read()

    with open("TodoList.txt","a") as f:
        newtask = (input("Enter New Task: "))
        f.write(newtask +  "\n")

    with open("TodoList.txt","r") as f:
        data = f.read()
        print(data)

def Remove_task():  
    with open("TodoList.txt", "r") as f:
        lines = f.readlines()

    with open("TodoList.txt", "r") as f:
        data = f.read()
        print(data)

    line_no = int(input("Enter line number to delete: "))

    with open("TodoList.txt", "w") as f:
        for i, line in enumerate(lines):
            if i != line_no - 1:
                f.write(line)

    print("Data")

    with open("TodoList.txt", "r") as f:
        data = f.read()
        print(data)

def View_task():
    from datetime import datetime
    f = open("TodoList.txt","r")
    data = f.readlines()

    
    now = datetime.now()  
    timestamp = now.strftime("%d-%m-%Y %H:%M")

    if len(data) == 0:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(data):
            print(f"{i + 1}. {task.strip()} | {timestamp}\n")

while True:
    print("Welcome To 'TODO List' ")
    1 == "Add Task"
    2 == "View Task"
    3 == "Delete Task"
    4 == "Exit"
    print(menu())
    
    option = int(input("Enter The Number"))
        
    if option == 1:
        print(Add_task())
        
    elif option == 2:
        print(View_task())
    
    elif option == 3:
        print(Remove_task())

    elif option == 4:
        break

    else:
        print("invalid No")

