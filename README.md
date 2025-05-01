# sujana_task7
Tools used- MySQL workbench and Jupyter notebook
We first created a table named sales_tab1 in MySQL workbench and then used the following code to connect it to Jupyter notebook.
import pymysql
import pandas as pd
db_name = "testdb"
db_host = "localhost"
db_username = "root"
db_password = "type_your_password"

try:
    conn = pymysql.connect(host = db_host,
                           port = int(3306),
                           user = "root",
                           password = db_password,
                           db = db_name)
except e:
    print (e)
if conn:
    print ("connection successful")
else:
        print ("error")

We then write the code the following syntax:
df=pd.read_sql_query("Type your sql code here",conn)
And the output is produced.
