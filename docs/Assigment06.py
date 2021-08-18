# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# ARonsse,8.16.2021,Modified code to complete assignment 6
# ARonsse, 8.17.2021, updated code to avoid runtime error for nonexistent file
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
add_task = ""  # Captures the user task data
add_priority = ""  # Captures the user priority data
del_task = "" # Captures the user request to delete data
tup_row = "" # Captures function output in a tuple
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
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds To Do items to dictionary row and adds the row to a list

        :param task: (string) with name of task:
        :param priority: (string) with priority value of the task:
        :param list_of_rows: (list) you want filled with task and priority data:
        :return: (list) of dictionary rows
        """
        new_row = {'Task': task, 'Priority': priority}
        list_of_rows.append(new_row)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Looks up dictionary rows by task and deletes the row from a list

        :param task: (string) with name of task:
        :param list_of_rows: (list) from which to delete data:
        :return: (list) of dictionary rows
        """
        for row in list_of_rows:
            if row['Task'] == task:
                list_of_rows.remove(row)
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows into a file

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want to write to file:
        :return: (list) of dictionary rows
        """
        file = open(file_name, 'w')
        for row in list_of_rows:
            file.write(row['Task'] + ',' + row['Priority'] + '\n')
        file.close()
        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Collect new task and priority information from the user

        :param: none
        :return: task, priority
        """
        task = input('Enter a task for your To Do List: ').lower().strip()
        priority = input('Assign a priority to the task entered above: ').lower().strip()
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Collect information about which task to remove from the list from the user

        :param: none
        :return: task
        """
        task = input('Enter the task you wish to remove from your list: ').lower().strip()
        return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
try:
    Processor.read_data_from_file(strFileName, lstTable)  # read file data
except:
    print('Unable to find file. Current ToDo list is empty as shown below:')

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        tup_row = IO.input_new_task_and_priority() # Requests user input and captures function output
        add_task, add_priority = tup_row # Unpack the tuple
        Processor.add_data_to_list(add_task, add_priority, lstTable) # Pass arguments into function parameters
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        del_task = IO.input_task_to_remove() # Requests user input and captures function output
        Processor.remove_data_from_list(del_task, lstTable) # Pass arguments into function parameters
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  #Exit Program
        print("Goodbye!")
        break   # and Exit
