import pathlib
import sqlite3
import pandas as pd


path = pathlib.Path().cwd()

def create_db(db_name, filename, table_name):
    file_path = path/filename                                   # create a path to the data file
    
    con = sqlite3.connect(db_name)                              # create a connection to the database
    cursor = con.cursor()                                          # create a cursor

    health = pd.read_csv(file_path)                                           # read in the data 
    health.to_sql(table_name, con, index=False, if_exists='replace')        # insert the data into the       
                                                                                 #specified table
    results = cursor.execute(f"SELECT *FROM {table_name}").fetchall()         # execute a select statement
                                                                           # as f- string and print results 
                                                                           #to verifiy insertion
    print(results)
    con.commit()                                                      # commit the changes to the database
    con.close()                                                       # close the connection
    
if __name__=="__main__":
    db_name = "health_insurrance.db"
    filename = "health_insurrance.csv"
    table_name = "health"
    create_db(db_name, filename, table_name)