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
#          2.18.2021 Continued inputting
#          2.19.2021 Troubleshooting
#          2.20.2021 Troubleshooting and debugging
#          2.21.2021 TroubleShooting, completed
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants

file_name = "ToDoFile.txt"  # "C:\_PythonClass\Assignment06\ToDoList.txt"
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
list_of_rows = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

                :param file_name: (string) with name of file:
                :param list_of_rows: (list) you want filled with file data:
                :return: (list) of dictionary rows
                """
        file = open(file_name, "r")
        for row in file:
            task,priority= row.split(",")
            dicRow = {"Task": task.strip(), "Priority":priority.strip()}
            list_of_rows.append(dicRow)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        dicRow = {"Task": task, "Priority": priority}
        list_of_rows.append(dicRow)
        return list_of_rows, 'Success'


    @staticmethod
    def remove_data_from_list(task_to_remove, list_of_rows):
        for dicRow in list_of_rows:
            if task_to_remove.lower() == dicRow["Task"].lower():
                list_of_rows.remove(dicRow)
                print("{", task_to_remove, "} has been deleted")
            else:
                continue
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        objFile = open(file_name, "w")
        for i in list_of_rows:
            objFile.write(i['Task']+ "," + i['Priority'] + '\n')
        objFile.close()
        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """display menu of choices"""
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
        """ Gets the menu choice from a user

                :return: string
                """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print("\n")
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

               :param list_of_rows: (list) of rows you want to display
               :return: nothing
               """
        print("******* The current Tasks ToDo are: *******")
        for dicRow in list_of_rows:
            print(dicRow["Task"] + " (" + dicRow["Priority"] + ")")
        print("*******************************************")
        print("\n")  # Added an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

               :return: string
               """
        response = None
        while response not in ("yes", "no"):
            response = input(message)
        return response.strip().lower()


    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

                :param optional_message:  An optional message you want to display
                :return: nothing
                """
        print(optional_message)
        input('Press the [Enter] key to continue.')
        #return

    @staticmethod
    def input_new_task_and_priority():
        task = str(input("Enter a Task: "))
        priority = str(input("Enter a priority: "))
        Processor.add_data_to_list(task, priority, list_of_rows)
        return

    @staticmethod
    def input_task_to_remove():
        task_to_remove = input("Select a task to remove...Be Specific: ")
        Processor.remove_data_from_list(task_to_remove, list_of_rows)
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

    elif strChoice == '3':  # Save Data to File   #
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
        if strChoice.lower() == "yes":
            Processor.read_data_from_file(file_name, list_of_rows)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  #
    elif strChoice == '5':
        print("Goodbye!")
        break  # and exit