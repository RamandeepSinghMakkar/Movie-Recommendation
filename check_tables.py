import mysql.connector

def get_mysql_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", #insert your password here
        database="movie_recommendations"
    )

def check_recommendations():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    
    query = "SELECT * FROM recommendations;"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)  # Display the rows returned from the query
    
    cursor.close()
    connection.close()

# Call the function to check the recommendations table
check_recommendations()
