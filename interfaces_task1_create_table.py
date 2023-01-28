import sqlite3
import sys


def main():
    

    print("""
        Select Option:
            1 -Veriify if table exists, its create if not exist (step2)
            2 -Create bbdd with table
            3 -Adding Students MAX 9
            4 -Query a Student for First Name
            5 -Exit
    """)
    choose=int(input("Choose a option: "))
    menu(choose)

def menu(choose):
    if choose == 1:
        verify_table()
    elif choose == 2:
        create_table()
    elif choose == 3:
        add_student()
    elif choose == 4:
        query_register()
    elif choose == 5:
        out_of_app()
    else:
        print("Invalid option")
    # switcher = {    1:verify_table(),
    #                 2:create_table(),
    #                 3:add_student(),
    #                 4:consultar_registro(),
    #                 5:salir_de_app()
    #             }
    

   

    #verify_table()

def out_of_app():
    sys.exit(0)

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
        print("The table is ready, step 1 and step 2 finished")
        
    else:
        print("It already exists")
         
    cursor_obj.close()
    conn.close()

def add_student():
    id=0
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
            # print(query)
            # print("/home/lucato/Documents/Curso_Python/Repositorios/Open_BootCamp/tasks/My_application.db")
            cursor_obj.close()
        else:
            conn.close()    
            conn.commit()


def query_register():
    conn = sqlite3.connect("/home/lucato/Documents/Curso_Python/Repositorios/Open_BootCamp/tasks/My_application.db")
    cursor_obj = conn.cursor()

    First_name = input("Enter a First_name to query: ")
    query =(f"SELECT * FROM Students Where First_name='{First_name}'" )
    rows = cursor_obj.execute(query)
    result=cursor_obj.fetchall()
    print(result)

    conn.commit()
    cursor_obj = conn.close()
    conn.close()




if __name__ == '__main__':
    main()

