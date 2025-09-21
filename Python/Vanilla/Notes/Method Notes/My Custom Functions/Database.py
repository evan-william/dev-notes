import time
import mysql.connector
import sys

# 1. Create DB After Connected
def create_database_and_table(hostInput, userInput, passwordInput):
        try:
            conn = mysql.connector.connect(
                host=hostInput,
                user=userInput,
                password=passwordInput
            )
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS QuotesGen")
            cursor.execute("USE QuotesGen")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Quotes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    quotes VARCHAR(255) NOT NULL,
                    author VARCHAR(255) NOT NULL
                )
            """)
            conn.commit()
            cursor.close()
            conn.close()

            print("\nConnected Succesfully!")
            time.sleep(1)
            for i in range(4):
                dots = "." * i
                print(f"\rOpening Main Menu{dots}   ", end='', flush=True)
                time.sleep(0.5)
            time.sleep(0.5)
            
        except mysql.connector.errors.DatabaseError:
             print("\nDatabase connection failed!")
             time.sleep(1)
             for i in range(4):
                dots = "." * i
                print(f"\rExiting{dots}   ", end='', flush=True)
                time.sleep(0.5)

             print()  
             sys.exit(0)

# 2. Authentication Ask
def authentication():
    # clear_screen()
    # print(auth_menu())
    hostInput = input("Host (default: localhost): ").strip() or "localhost"
    userInput = input("User (default: root): ").strip() or "root"
    passwordInput = input("Password (default: empty): ").strip() or ""
    return hostInput, userInput, passwordInput

# 3. Load Query 
def load_queries(file_path):
    with open(file_path, "r") as file:
        content = file.read().split("-- name:")
        queries = {}
        for each in content:
            if each.strip(): 
                name, sql = each.strip().split("\n", 1) 
                queries[name.strip()] = sql.strip()
        return queries
    
# 4. Instance for Above
def initiate_query_runner():
    queries = load_queries(r"D:\College\Programming Files\Codes\Projects\Github Projects\Learning Projects\Beginner\Quote Generator API + DB\queries.sql")
    return queries
