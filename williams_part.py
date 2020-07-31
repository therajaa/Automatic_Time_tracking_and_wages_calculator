
#importation of relevant modules
#-------------------------------------------------------------------------------------
from datetime import datetime
import csv

# Program initialization Display
#-------------------------------------------------------------------------------------
print("""
    Welcome to time tracking and wages calculator!!!

    To start a consultation session: Enter 'START' 
    To stop a consultation session : Enter 'STOP' 
    To quit the program:             Enter 'QUIT'
    To get detailed information:      Enter 'HELP'
    **********************************************""")

#Program variables declaration
#-------------------------------------------------------------------------------------
command =""
start =False
attempts = 0
calc_summary = []
allowed_attempts = 4