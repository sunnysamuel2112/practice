# Import Module
import os
import tabula
import pandas as pd

# Read PDF File (enter the pdf name and extension)
pdfname = input("enter the pdf name and extension: ")
i = 0
df = tabula.read_pdf(pdfname, pages='all')[i]
if df.columns[0] == 'University Seat Number':
    df = tabula.read_pdf(pdfname, pages='all')[i+1]


# Convert into Excel File
filename = 'excelfile.xlsx'
df.to_excel(filename)

# Reading Excel File
df = pd.read_excel(filename)

# Selecting only Subject,Total,Result
subs = df.loc[df['Total'] >= 0]


# print(subs)
specific_subs = subs[['Subject', 'Total', 'Result']]
print(specific_subs)

# print(description)
description = specific_subs.describe()
print(description)


# delete the excel files created
os.remove(filename)
