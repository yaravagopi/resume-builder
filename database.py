import mysql.connector
from mysql.connector import errorcode
import config

# Obtain connection string information from the portal

config = {
    'host': config.host,
    'user': config.user,
    'password': config.password,
    'database': config.database,
    'client_flags': [mysql.connector.ClientFlag.SSL],
    'ssl_ca': config.ssl_ca,
    'ssl_verify_cert': 'true'
}

if __name__ == '__main__':
    try:
        conn = mysql.connector.connect(**config)
        print("Connection established")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("USE ts_sdp4;")
        print("Triggered ts_sdp4 database.")

        # Drop previous table of same name if one exists
        cursor.execute("DROP TABLE IF EXISTS records;")
        print("Finished dropping table (if existed).")

        # Create table
        cursor.execute(
            "CREATE TABLE record(id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, email varchar(255) NOT NULL, phone int not null, period varchar(255) NOT NULL);")
        print("Finished creating table.")

        # Insert some data into table
        # cursor.execute(
        #     "INSERT INTO inventory (name, email, period) VALUES (%s, %s, %s);", ("Abhinav", "pamarthiabhinav12@gmail.com", "1st"))
        # print("Inserted", cursor.rowcount, "row(s) of data.")

        # Cleanup
        conn.commit()
        cursor.close()
        conn.close()
        print("Done.")


def insert_data(name, email, phone, period):
    res = "404"
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO record (name, email, phone, timestamp) VALUES (%s, %s, %s, %s);", (name, email, phone, period))
        conn.commit()
        print("Data inserted successfully")
        res = "200"
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        res = "400"
    finally:
        cursor.close()
        conn.close()
    return res
