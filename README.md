xlsx_to_csv
===========

Exporting an .xlsx into a .csv.

In case your xlsx has multiple sheets, this works too, and creates multiple .csv files!

This code doesn't work with Python 2, at least Python 3 required.


```
Usage: python xlsx_to_csv.py "/var/www/Secret Document.xlsx"
```

Small warning: If you have dates inside your excel spreadsheets, it will convert it into a number which is the number of days since January 1st 1900.
