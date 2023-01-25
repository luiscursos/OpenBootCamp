import sqlite3



def main():
    verify_table()


def create_table():
    conn = sqlite3.connect("/home/lucato/Documents/Curso_Python/Repositorios/Open_BootCamp/tasks/My_application.db")
    cursor_obj = conn.cursor()
    table = """
            CREATE TABLE IF NOT EXISTS Students(
                id INT NOT NULL PRIMARY KEY,
                First_Name TEXT NOT NULL,
                Last_Name TEXT NOT NULL
            );"""
    cursor_obj.execute(table)
    conn.commit()
    cursor_obj.close()
    conn.close()


    
    # Check if table exists
def verify_table ():
    conn = sqlite3.connect("/home/lucato/Documents/Curso_Python/Repositorios/Open_BootCamp/tasks/My_application.db")
    cursor_obj = conn.cursor()

    list_of_tables = cursor_obj.execute(
  """SELECT name FROM sqlite_master WHERE type='table'
  AND name='Students'; """).fetchall()
    if list_of_tables == []:
        print("Table no found!")
        create_table()
        print("The table is ready")
        add_student()
    else:
        print("It already exists")
        add_student()   
    cursor_obj.close()
    conn.close()

def add_student():
    for id in range(1,9):
        if id < 9:
            First_name = input("Enter a First Name: ")
            Last_name = input("Enter a Last Name: ")
            Student = f"The student '{First_name}','{Last_name}' has Id {id}"
            id+=1
            conn = sqlite3.connect("/home/lucato/Documents/Curso_Python/Repositorios/Open_BootCamp/tasks/My_application.db")
            cursor_obj=conn.cursor()
            query = f"INSERT INTO Students(Id, First_name, Last_name) VALUES ({id}, '{First_name}', '{Last_name}')"
            add= cursor_obj.execute(query)
            conn.commit()
            print(query)
            print("/home/lucato/Documents/Curso_Python/Repositorios/Open_BootCamp/tasks/My_application.db")
            cursor_obj.close()
        else:
            conn.close()    
            conn.commit()
        

if __name__ == '__main__':
    main()

