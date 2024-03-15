import os
from datetime import date
import subprocess

# relative directory that we will store entries in
entries_dir = "Entries"
# text that will displayed when we create a new entry
default_text = "#Nama Penulis Pertama:\n - \n - \n - "
# application that we will open the file in
application = "notepad.exe"

def main() :
    global entries_dir, default_text, application

    entries_absolute_path = get_extries_absolute_path()
    target_dir = get_target_dir (entries_absolute_path)
    go_to_dir(target_dir)
    create_new_entry()


# return the absolute path to the entries directory
def get_extries_absolute_path():
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, entries_dir)
    

def get_target_dir(entries_absolute_path):
        year = date.today().strftime("%Y") #2024
        month = date.today().strftime("%B") #Maret
        target_dir = os.path.join(entries_absolute_path, year, month)
        return target_dir 
    

def go_to_dir(target_dir):
        try:
            os.makedirs(target_dir)
        except:
            pass
        os.chdir(target_dir)


def create_new_entry():
    # Get the filename
    month = date.today().strftime("%B")
    day = date.today().strftime("%d")
    filename = f"{month} {day}.txt"


    #Create the file IF it does not exist
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(default_text)


    # Open the file
    subprocess.Popen([application, filename])


if __name__== "__main__":
    main()
