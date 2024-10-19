import mysql.connector
from mysql.connector import Error

def create_database():
    try:


        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nour@2002",
            database="alx_book_store"
        )
        if connection.is_connected():
                    cursor = connection.cursor()
                    # Create database if it does not exist
                    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                    print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

if __name__ == '__main__':
    create_database()
