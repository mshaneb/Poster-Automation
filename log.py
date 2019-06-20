import openpyxl

#access poster requst XL
'''
fields:
Order #	
FY	
Request Date	
Due Date	
Requestor	
Office	
Phone #	
Project Title	
Qty.	
Orientation	
Trim Size	
Color	
Paper	
Mounted	
Approved By	
Completed By	
Date 
Completed	
Notes
'''

oma_excel = r"S:\Office of Management and Analytics (OMA)",
\OMA Operations\Business Services\Graphics\Current\OWS Poster Printing Services\Forms"
openpyxl = openpyxl.load_workbook()
#open Poster request log