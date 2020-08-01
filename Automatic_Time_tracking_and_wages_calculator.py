
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

#Main while loop
#-------------------------------------------------------------------------------------
while allowed_attempts>attempts:
    command= input("""
Enter 'START' or 'STOP' or 'QUIT' to start/stop/quit a session >""").lower()
    attempts += 1
    if command == "start":
        if start:
            print("---------------------------------------------------------------------")
            print('A session is already started, Enter "STOP" when session is ended')
            print("---------------------------------------------------------------------")
        else:
            print("---------------------------------------------------------------------")
            start = True
            start_datetime = datetime.now()
            print("You started this Consultation session at:", start_datetime)
            print("---------------------------------------------------------------------")
    elif command == "stop":
        print("---------------------------------------------------------------------------------")
        if not start:
            print('The previous consultation is already stopped, Enter "START" to begin new session')
            print("---------------------------------------------------------------------------------")
        else:
            start = False
            stop_datetime = datetime.now()
            elapsed_time = abs(stop_datetime - start_datetime).total_seconds() / 3600
            amount_made = round(elapsed_time*5,2)
            calc_summary = [("CALCULATION-SUMMARY: "+ str(start_datetime.date())), ("Start_DateTime:" + str(start_datetime)),
                ("Stop_DateTime:" +str(stop_datetime)), "Amount_made: $" + str(amount_made)]
            print("Consultation start date and time:" +' ' + str(start_datetime))
            print("Consultation stop date and time: " + str(stop_datetime))
            print("Session duration: " + " " + str(round(elapsed_time,3)) + " " + "hours")
            print("---------------------------------------------------------------------")
            print ("Amount of money made: " + " " + "$" + str( amount_made))
            print("---------------------------------------------------------------------")
            #Saving output to .csv file
            #-------------------------------------------------------------------------------------
            csvfile = open('time_tracking_wages_summary.csv',
                           'a', newline='\r\n')
            obj = csv.writer(csvfile, delimiter= " ")
            obj.writerows(calc_summary)
    elif command == "help":
            print("""
    This program computes the total amount made during
    a consultation session, the required user inputs
    are as follows:

    To start a consultation session: Enter 'START'
    To stop a consultation session : Enter 'STOP'
    To quit the program:             Enter 'QUIT'
    To get detailed information:     Enter 'HELP'
            """)
    elif command == "quit":
        print("You quit")
        break
    else:
         print('Too many invalid attempts or wrong user inputs')

#Program End
#-------------------------------------------------------------------------------------
