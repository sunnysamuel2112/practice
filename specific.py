import tabula

filename = input("enter the filename with extension: ")

i = 0

df = tabula.read_pdf(filename, pages="all")[i]
if df.columns[0] == 'University Seat Number':
    i = i+1
    df = tabula.read_pdf(filename, pages="all")[i]

dataframe = []

for index, row in df.iterrows():
    if(row['Total'] >= 0):
        dataframe.append(row)

marks = []
for j in range(len(dataframe)):
    marks.append(dataframe[j][['Subject', 'Total', 'Result']])


for subs, tots,result in marks:
    print(subs, tots, result)
