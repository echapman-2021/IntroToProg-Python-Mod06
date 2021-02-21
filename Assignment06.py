# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# EChapman,2.17.2021 Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
#strFileName = "ToDoFile.txt"
file_name = "ToDOList.txt"
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
#lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions
list_of_rows = []
task = ""
priority = ""
task_to_remove = ""

#PROBLEMS tasks do not get uploaded, IO does not get linked in Processing
# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        file_name = "C:\_PythonClass\Assignment06\ToDoList.txt"
        file = open(file_name, "r")
        for row in file:
            data = row.split(",")
            dicRow = {"Task": data[0].strip(), "Priority": data[1].strip()}
            list_of_rows.append(dicRow)
        file.close()


    #file_name = "ToDo.txt"

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        NewRow = {"Task": task, "Priority": priority}
        list_of_rows.append(NewRow)
        return


    @staticmethod
    def remove_data_from_list(task_to_remove, list_of_rows):
        for dicRow in list_of_rows:
            if task_to_remove.lower() == dicRow["Task"].lower():
                list_of_rows.remove(dicRow)
                print("{", task_to_remove, "} has been deleted")
            else:
                continue
        return

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        file_name = "C:\_PythonClass\Assignment06\ToDoList.txt"
        objFile = open(file_name, "w+")
        for i in list_of_rows:
            objFile.write('%s\n' % list_of_rows)
        objFile.close()
        return


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():  # display menu of choices
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File
        4) Reload Data from File
        5) Exit Program
        ''')
        return "\n"

    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print("\n")
        return choice  #DO NOT REMOVE

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows"""
        print("******* The current Tasks ToDo are: *******")
        for dicRow in list_of_rows:
            print(dicRow["Task"] + " (" + dicRow["Priority"] + ")")
        print("*******************************************")
        print("\n")  # Added an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):  #DO NOT CHANGE
        response = None
        while response not in ("yes", "no"):
            response = input(message).lower()
        return response.strip()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        optional_message = input('Press the [Enter] key to continue.')
        return  # optional message removed

    @staticmethod
    def input_new_task_and_priority():
        task = str(input("Enter a Task: "))
        priority = str(input("Enter a priority: "))
        Processor.add_data_to_list(task, priority, list_of_rows) #worked
        return

    @staticmethod
    def input_task_to_remove():
        task_to_remove = input("Select a task to remove...Be Specific: ")
        Processor.remove_data_from_list(task_to_remove, list_of_rows)   #ATTEMPT
        return


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name, list_of_rows)
# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(list_of_rows)  # changed from lstTable # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    if strChoice.strip() == '1':  # Add a new Task
        IO.input_new_task_and_priority()
        #Processor.add_data_to_list(task, priority, list_of_rows)
        IO.print_current_Tasks_in_list(list_of_rows)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        IO.print_current_Tasks_in_list(list_of_rows)
        IO.input_task_to_remove()
        IO.print_current_Tasks_in_list(list_of_rows)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File   #NOT ACTUALLY SAVING DATA TO FILE
        IO.print_current_Tasks_in_list(list_of_rows)
        strChoice = IO.input_yes_no_choice("Save this data to file? (yes/no) - ")
        if strChoice.lower() == "yes":
            print("Data is being saved to file")
            Processor.write_data_to_file(file_name, list_of_rows)
            IO.input_press_to_continue(strStatus)
            print()
        elif strChoice.lower() == "no":
            IO.input_press_to_continue("Save Cancelled!")
        else:
            continue
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (yes/no) -  ")
        if strChoice.lower() == "yes":   #WORKING HERE 4:17
            Processor.read_data_from_file(file_name, list_of_rows)  # WHAT DOES RELOAD MEAN
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  #
    elif strChoice == '5':
        print("Goodbye!")
        break  # and exit