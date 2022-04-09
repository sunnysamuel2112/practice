
# Import Module

import pdftables_api


# API KEY VERIFICATION

conversion = pdftables_api.Client('API KEY')


# PDf to Excel
# (Hello.pdf, Hello)

conversion.xlsx("C:\Users\Sharon Sherly Samuel\AppData\Local\Programs\Python\Python39\basics\django\practice", "C:\Users\Sharon Sherly Samuel\AppData\Local\Programs\Python\Python39\basics\django\practice")
