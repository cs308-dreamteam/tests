import mysql.connector
from mysql.connector import errorcode

from dotenv import load_dotenv
import os

load_dotenv()

db_pw = os.environ.get("DB_PW")


def create_connection():
    try:
        cnx = mysql.connector.connect(user="root", password=db_pw, database="db")
        print("Connection established with the database")
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
    else:
        cnx.close()
        return None
