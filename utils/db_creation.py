import pymysql as ms
def create_database():
    conn=ms.connect(
        host="localhost",
        user="root",
        password="system",
    )
    cursor=conn.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS daily_habit_tracker")
        print("database created")
        cursor.execute("USE daily_habit_tracker")
        cursor.execute("""CREATE TABLE IF NOT EXISTS daily_logs(
               id INT auto_increment primary key,
               date DATE NOT NULL,
               mood INT CHECK (mood BETWEEN 1 AND 10),
               study_hours INT CHECK(study_hours >=0),
               sleep_hours INT CHECK(sleep_hours >=0),
               entertainment_hours INT CHECK(entertainment_hours >=0),
               topic VARCHAR(250) NOT NULL)""")      
        print("Table created") 
    except:
        print("Error creating Database and table")
    finally:
        conn.close()
        cursor.close()

