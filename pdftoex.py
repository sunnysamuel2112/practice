# Import the required Module
import tabula
#import re
import pandas as pd
#pattern = re.compile(r'/d/d.*/d/d')
# Read a PDF File
#df = tabula.read_pdf("4th_sem.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("anjali.pdf", "anjali.json",
                    output_format="JSON", pages='all')  # print(df)
#resultdict = dict()
#df = pd.read_csv('amith.csv')
""" for index, row in df.iterrows():
    if row['Subject'] == 'NaN':
        pass
    else:
        print(row[['Subject', 'Total', 'Result']]) """
