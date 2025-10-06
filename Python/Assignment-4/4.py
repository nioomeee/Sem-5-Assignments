# Create a DatabaseConnection class where the constructor simulates
# connecting to a database and the destructor automatically closes the connection
# and logs the closing time in a file.

import datetime

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

        print(f"\n Connecting to database: {db_name}")

    def __del__(self):
        print(f"\n Disconnecting from database '{self.db_name}'...")

        # get current time
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H-%M-%S")

        log_message = (f"\n Connection to '{self.db_name}' closed at {timestamp}")

        with open("db_log.txt", "a") as log_file:
            log_file.write(log_message)

def manage_session():
    print(" ------- Starting DB session ------- ")
    db_conn = DatabaseConnection("production_db")
    print("\n ... Performing Database Operations ...")
    print("\n --- Ending DB session ---")

print("\n Program starting -------\n")
manage_session()
print("\n Program finished -------")
