def view_tasks(todo_list):
    """ Display all the tasks in the ToDo list
    
    Args:
        todo_list (list): A list containing tasks and their priorities as sublists.
    
    Returns:
        None
    """
    index = 1
    for x in range(len(todo_list)):
        if "High" in todo_list[x]:
            print(index,todo_list[x][0],"Priority:", todo_list[x][1])
            index+=1
    for x in range(len(todo_list)):
        if "Medium" in todo_list[x]:
            print(index,todo_list[x][0],"Priority:", todo_list[x][1])
            index+=1
    for x in range(len(todo_list)):
        if "Low" in todo_list[x]:
            print(index,todo_list[x][0],"Priority:", todo_list[x][1])
            index+=1


def search_tasks(todo_list):
    """ Search and display tasks containing a specific keyword
    
    Args:
        todo_list (list): A list containing tasks and their priorities as sublists.
    
    Returns:
        vowels='aeiou'
    my_array=[]
    for letter in word.lower():
        if letter not in vowels:
            my_array.append(letter)
    return my_array

        None
    """
    e=input("Enter keyword to search: ")
    for e in todo_list:
        if e in todo_list:
            print(e)
        else:
            print("Invalid input")

def add_task(todo_list):
    """ Add a task to the ToDo list
    
    Args:
        todo_list (list): A list containing tasks and their priorities as sublists.
    
    Returns:
        list: Updated ToDo list
    """
   
    while True:
        b=input("What is your task description: " )
        c=input("Set task priroty: ")
        if c=="Low":
            todo_list.append([b,c])
            return c
        elif c=="Medium":
            todo_list.append([b,c])
            return c
        elif c=="High":
            todo_list.append([b,c])
            return c
        else :
            print("Invalid choice. Please select a valid option")

def remove_task(todo_list):
    """ Remove a task from the ToDo list
    
    Args:
        todo_list (list): A list containing tasks and their priorities as sublists.
    
    Returns:
        list: Updated ToDo list
    """
    for x in range(len(todo_list)):
        print (x,todo_list[x],"\n")
    
    while True:
        d=int(input("Enter the index number of the task to remove: "))
        if d in range(len(todo_list)):
            todo_list.pop(d)
            return todo_list
        else:
            print("Invalid index")




def display_menu():
    """ Display the menu for the ToDo list software
    
    Returns:
        int: User's choice corresponding to the operations they want to perform.
    """
    print("Welcome to the ToDo list Manager!  \n -----------------------\n 1. Add Task\n 2. Remove Task \n 3. View task\n 4. Search Task\n 5 Exit\n -----------------------")
  
    while True:
        a=int(input("Enter your choice: "))
        if a==1:
            return a
        elif a==2:
            return a
        elif a==3:
            return a
        elif a==4:
            return a
        elif a==5:
            return a
        else :
            print("Invalid choice. Please select a valid option")


def main():
    todo_list = [['Eat bread','High'],['Drink Milk','Low'],['Run 5K','Medium']] #initialize empty todolist
    while True: # main software loop
        b= display_menu()
        if b==1:
            add_task(todo_list)
        elif b==2:
            remove_task(todo_list)
        elif b==3:
            view_tasks(todo_list)
        elif b==4:
            search_tasks(todo_list)
        elif b==5:
            break
        else :
            print("Invalid choice. Please select a valid option")

if __name__ == "__main__": # Run the main!
    main()