import os
todo_file="todo.txt"
def load_tasks():
    if not os.path.exists(todo_file):
        return []
    with open(todo_file,"r") as file:
        tasks=[line.strip() for line in file.readlines()]
    return tasks 
def save_tasks(tasks):
    with open(todo_file,"w") as file :
        for task in tasks:
            file.write(task+'\n')

def show_tasks(tasks):
    if not tasks:
        print("you have no tasks")
    else :
        print("\nyour tasks are!")
        for i,task in enumerate(tasks,start=1):
            print(f"{i}.{task}")
    print()

def add_task(tasks):
    task=input("enter the new task\n").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
    else:
        print("empty tasks cannot be added\n")
    
def remove_task(tasks):

    show_tasks(tasks)
    if not tasks:
        print("No taks to remove\n")
    while True:
        user_inp=input("enter task index to remove(or enter 'q' to exit)\n")
        if user_inp.lower() =='q':
            print("cancelled task removal\n")
            return
    
        try :
            index=int(user_inp)
            if 1<=index<len(tasks):
                removed=tasks.pop(index-1)
                print(f"task {index} is removed\n")
            else :
                print("enter valid task number\n")
        except ValueError:
            print("enter valid number\n")

def main():
    print("welcome to the todo app\n")
    tasks=load_tasks()
    while(True):
        print("here aare your options\n")
        print("choose 1:show_tasks\n")
        print("choose 2:add tasks\n")
        print("choose 3:remove tasks\n")
        print("choose 4:exit\n")
        choice=input("enter your choice")
        if(choice=="1"):
            show_tasks(tasks)
        elif(choice=="2"):
            add_task(tasks)
        elif(choice=="3"):
            remove_task(tasks)
        elif(choice=="4"):
            print("\nexiting goodbye!!")
            break
        else:
            print("\nchoose valid option")
        

if __name__=="__main__":
    main()
    

    