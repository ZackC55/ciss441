"""
Author: Zack Cochran
Date: 02/08/2020
Goal: To take historical electoral college data from a CSV to a SQLite Database.
"""


import csv                  # import csv python module
import sqlite3

DB_FILE = 'electoral_college.db'
conn = sqlite3.connect(DB_FILE)


def create_electoral_college_table():
    """
    This method will create the electoral college table if it doesn't already exist.
    """
    cur = conn.cursor()
    str_sql = """
        CREATE TABLE if not exists electoral_college (
            ID integer primary key autoincrement,
            Year int,
            State text,
            Votes int
        );
        """
    cur.execute(str_sql)
    conn.commit


def open_csv_insert_into_db():
    cur = conn.cursor()
    row_count = 0               # count variable for if logic & to show row number on print screen
    # open csv file so that it can be referenced from csvfile
    with open('ec.csv', 'r') as csvfile:
        # use the csv.DictReader command to convert to a reader object
        reader = csv.DictReader(csvfile)
        # loop over the reader object
        for ec_row_dic in reader:
            row_count += 1
            # Extract each variable from the dictionary
            t_ID = ec_row_dic['ID']
            t_Year = ec_row_dic['Year']
            t_State = ec_row_dic['State']
            t_Votes = ec_row_dic['Votes']
            # SQL String, Data Tuple, Execute & Commit
            sql_str_insert_with_param = """
                INSERT INTO electoral_college
                    (ID, Year, State, Votes)
                VALUES
                    (?, ?, ?, ?);
            """
            data_tuple = (t_ID, t_Year, t_State, t_Votes)
            cur.execute(sql_str_insert_with_param, data_tuple)
            conn.commit
            # Print data to the user so they know where they are in processing
            if row_count <= 102:
                print('processing!!! {0:>3}  ID: {1:<5}   Year: {2:<5}    State: {3:<15}   Votes: {4}'.format(
                    row_count, t_ID, t_Year, t_State, t_Votes))      
    cur.close()


def get_electoral_college_by_Year(Year=None):
    print('\n ELECTORAL COLLEGE REPORT by Year: ' + Year)
    cur = conn.cursor()
    str_sql = """
        select ID, Year, State, Votes
        from electoral_college
        where Year = ?;
        """
    data_tuple = (Year, )
    cur.execute(str_sql, data_tuple)
    records = cur.fetchall()
    for row in records:
            t_ID, t_Year, t_State, t_Votes = row
            print('Year: {1:<5}   State: {2:<15}  Votes: {3:<5} '.format(
                t_ID, t_Year, t_State, t_Votes))
    cur.close()


def main():
   create_electoral_college_table()
   open_csv_insert_into_db()
   get_electoral_college_by_Year('2016')
   get_electoral_college_by_Year('2020')
   conn.close()


if __name__ == "__main__":
    main()
