# Import Module
import os
import tabula
import pandas as pd

# Read PDF File (enter the pdf name and extension)
pdfname = input("enter the pdf and extension: ")

marks_list = []

df = tabula.read_pdf(pdfname, pages='all')

try:
    i = 0

    if df[i].columns[i] == 'University Seat Number':
        df[i] = tabula.read_pdf(pdfname, pages='all')[i+1]
    # Convert into Excel File
    filename = 'excelfile.xlsx'
    df[i].to_excel(filename)
    # Reading Excel File
    df[i] = pd.read_excel(filename)
    # Selecting only Subject,Total,Result
    subs = df[i].loc[df[i]['Total'] >= 0]
    # print(subs)
    specific_subs = subs[['Subject', 'Total', 'Result']]
    print(specific_subs)

    for row in specific_subs.iterrows():
        marks_list.append(row)

    # print(description)
    #description = specific_subs.describe()
    # print(description)

    # delete the excel files created
    os.remove(filename)
    # for prev_sem

except:
    print("Failed to fetch details.")
    os.remove(filename)


#print("saved in list: \n"+ str(marks_list))
