import os, mysql.connector

def main():
    con = mysql.connector.connect(
        user = os.environ['DBUSER'],
        password = os.environ['DBPASS'],
        host = os.environ['DBHOST'],
        database = os.environ['DBNAME']
    )
    cursor = con.cursor()

    print("Welcome to the Thesaurus. Type !q to quit.")

    while True:
        query = input("Enter a phrase: ")

        if query in ["!q", "!quit", "!exit"]:
            break

        cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % query)
        result = cursor.fetchall()

        if result:
            print("Result for %s:" % query)
            for r in result:
                print(r[1])
        else:
            print("No result found.")

if __name__ == "__main__":
    main()