import mysql.connector


def get_data():
    mydb = mysql.connector.connect(host= "localhost" ,user="mannumiaulmaria", password="grockjesus08#",database="testdb")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM employee")
    result = mycursor.fetchmany()                        
    mydb.close()
    return result