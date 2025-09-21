import mysql.connector

# STEP 1: Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",       # Replace with your MySQL username
    password="",   # Replace with your MySQL password
    database= "myprivateworld"        # This DB must already exist
)
cursor = conn.cursor() # SORTA LIKE AN INSTANCE

# STEP 2: Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL
)
""")

# STEP 3: Function to add a book
def add_book(title):
    sql = "INSERT INTO books (title) VALUES (%s)" # The Place holder %s, will be changed by val
    val = (title,)
    cursor.execute(sql, val) 
    conn.commit() # TO SAY YES, I WANT TO CHANGE THE DB
    print(f"Book '{title}' added successfully.")

# STEP 4: Function to remove a book by title
def remove_book(title):
    sql = "DELETE FROM books WHERE title = %s"
    val = (title,)
    cursor.execute(sql, val)
    conn.commit()
    if cursor.rowcount > 0: # TO CHECK IF ITS EXIST
        print(f"Book '{title}' removed successfully.")
    else:
        print(f"No book found with the title '{title}'.")

# STEP 5: Function to list all books
def list_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    print("\nCurrent Books in Library:")
    if not books:
        print("  (No books found)")
    for book in books:
        print(f"  ID: {book[0]} | Title: {book[1]}")
    print()

# STEP 6: Simple menu loop
while True:
    print("=== Book Manager ===")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. List Books")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        title = input("Enter book title to add: ")
        add_book(title)
    elif choice == '2':
        title = input("Enter book title to remove: ")
        remove_book(title)
    elif choice == '3':
        list_books()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Try again.")

# STEP 7: Close connection when done
cursor.close()
conn.close()


""" BASIC EXPLANATION
mysql.connector.connect(...) -> Establishes a connection to your MySQL server. You must provide your MySQL credentials and a database that already exists (e.g., librarydb).
CREATE TABLE IF NOT EXISTS -> 	Ensures the books table is available with an id (auto-incremented primary key) and title column.
add_book(title)	-> Inserts a book title into the books table.
remove_book(title)	-> Deletes a book row from the table where the title matches.
list_books() -> Retrieves and displays all books currently stored in the database.
Menu loop -> A basic command-line menu to interact with the database.
conn.commit() -> Saves changes to the database after INSERT or DELETE.
cursor.close() & conn.close() -> Cleanly closes the database connection.
"""

""" SYNTAX EXPLANATION
mysql.connector.connect()	Connect to MySQL database
conn.cursor()	Create cursor to execute SQL
cursor.execute(SQL)	Run SQL command
cursor.fetchall()	Get results of SELECT
conn.commit()	Save changes (INSERT/DELETE)
cursor.rowcount	Number of affected rows
cursor.close()	Close the cursor
conn.close()	Close the connection
(%s) + tuple	Safe way to insert values (avoids SQL injection)
"""

