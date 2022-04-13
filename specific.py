import tabula

#taking filename
filename = input("enter the filename with extension: ")

i = 0

#selecting the right dataframe
df = tabula.read_pdf(filename, pages="all")[i]
if df.columns[0] == 'University Seat Number':
    i = i+1
    df = tabula.read_pdf(filename, pages="all")[i]

#create a dataframe list
dataframe = []


#appending Nan-less rows into the list
for index, row in df.iterrows():
    if(row['Total'] >= 0):
        dataframe.append(row)

#specifically fetch "Subject","Total","Result"
marks = []

#append each element of the Nan-less dataframe into marks
for j in range(len(dataframe)):
    marks.append(dataframe[j][['Subject', 'Total', 'Result']])

#printing out the values appended to marks
for subs, tots,result in marks:
    print(subs, tots, result)
