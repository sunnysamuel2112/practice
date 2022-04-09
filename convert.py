# import packages needed
import glob
import tabula

# transform the pdfs into excel files
for filepath in glob.iglob('C:\Users\Sharon Sherly Samuel\AppData\Local\Programs\Python\Python39\basics\practice\4th_sem.pdf'):
    tabula.convert_into(filepath, output_format="xlsx")
