import MySQLdb
from datetime import datetime

ip,account,passowrd,database = "127.0.0.1","admin","197700","plate"

current_date = datetime.now().strftime('%Y-%m-%d')
time = datetime.now().strftime('%Y-%m-%d-%X')


def check_plate():
    # Step 1: Connect to MySQL server
    connection = MySQLdb.connect(ip,account,passowrd)
    cursor = connection.cursor()

    # Step 2: Check if the 'plate' database exists
    cursor.execute("SHOW DATABASES LIKE 'plate';")
    result = cursor.fetchone()

    # Step 3: Create the 'plate' database if it doesn't exist
    if not result:
        cursor.execute("CREATE DATABASE plate;")
        print("Database 'plate' created!")
    # else:
    #     print("Database 'plate' already exists.")
    cursor.close()
    connection.close()

def create_sheet(result_str):
    db = MySQLdb.connect(ip,account,passowrd,database)
    cursor = db.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS `licence plate` (
            id INT AUTO_INCREMENT PRIMARY KEY,
            time DATETIME,
            plate VARCHAR(255)
        );
        """# %(current_date)
    cursor.execute(create_table_query)
    insert_data_query = """
        INSERT INTO `licence plate` (time, plate)
        VALUES (%s, %s);
        """
    cursor.execute(insert_data_query, (time, result_str))
    db.commit()

def record(result_str):
    check_plate()
    create_sheet(result_str)