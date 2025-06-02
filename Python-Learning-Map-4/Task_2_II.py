import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host='localhost',
        database='uordb',
        user='root',       # change if needed
        password='newpassword'  # replace with your password
    )

    if conn.is_connected():
        print("Connected to MySQL database")
        cursor = conn.cursor()

        # # CREATE
        # insert_query = "INSERT INTO Users (name, email) VALUES (%s, %s)"
        # cursor.execute(insert_query, ("Nimali Perera", "nimali@gmail.com"))
        # conn.commit()
        # print("User added.")

        # # READ
        # cursor.execute("SELECT * FROM Users")
        # for row in cursor.fetchall():
        #     print(row)

        # UPDATE
        update_query = "UPDATE Users SET name = %s WHERE name = %s"
        cursor.execute(update_query, ("Nimali R Perera", "Nimali Perera"))
        conn.commit()
        print("User name updated.")


        # DELETE
        # delete_query = "DELETE FROM Users WHERE name = %s"
        # cursor.execute(delete_query, ("Nimal T Perera",))
        # conn.commit()
        # print("User deleted.")

except Error as e:
    print("Error:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection closed.")
