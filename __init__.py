'''import openpyxl

wb = openpyxl.load_workbook("posterlognamefileblah.xlsx", "r")
sheet = wb.active
rows = sheet.max_row
col = sheet.max_column

rows = rows+1

# writing previously captured data to excel

'''
from directions import directions
from time import sleep
import log

def start():
    print("**********",
          "\n",
          "Welcome to the OWS Poster Log Automation Tool.",
          "\n",
          "Please select an option from below:",
          "\n",
          " - 1. Directions",
          "\n",
          " - 2. Log Poster",
          "\n" * 2,
          "Enter selection now:"
          )

start()

selection = input()

print("\n" * 3,
      "~~~",
      "\n")

if selection == "1":
    print(str(directions),
          "\n",
          "~~~",
          )
    sleep(1)
    print("Returning to Main Menu:",
          "\n" * 3
          )
    sleep(1)
    start()

elif selection == "2":
    print("Starting Poster Logging Wizard:")
    sleep(1)
    log()

elif selection != "1" or "2":
    print("Please enter (1) or (2)."
          "\n"
          )
    sleep(1)
    print("Returning to Main Menu:"
          "\n" * 3
          )