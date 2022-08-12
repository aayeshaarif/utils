
import mysql.connector
from config import *
from mysql.connector import Error



def sql_fetch(query):
    """ Function executes query and returns all fetched data. 
        Returns int 0 if connection is not established"""
    try:
        cnx = mysql.connector.connect(user = user, password= password,
                                    host= host,
                                    database = database)
        if cnx.is_connected():
            cursor = cnx.cursor()

            cursor.execute(query)
            data =  cursor.fetchall()

    except Error as e:
        print("Error while connecting to MySQL", e)
        data = 0
    
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("MySQL connection is closed")
    
    return data

def sql_insert(query):
    """ Function executes query and returns all fetched data. 
        Returns int 0 if connection is not established"""
    try:
        cnx = mysql.connector.connect(user = user, password= password,
                                    host= host,
                                    database = database)
        if cnx.is_connected():
            cursor = cnx.cursor()
            cursor.execute(query)
            cursor.execute('COMMIT')



    except Error as e:
        print("Error while connecting to MySQL", e)
        
    
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("MySQL connection is closed")


