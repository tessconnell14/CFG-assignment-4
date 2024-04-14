import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


# Returns a mysql connection to a database with the given name
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

# Return all booking availability for a given date
def get_all_booking_availability(_date):
    availability = []
    try:
        db_name = 'new_schema'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            SELECT *
            FROM availability
            WHERE booking_date = '{}' 
            """.format(_date)

        cur.execute(query)

        availability = cur.fetchall()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")

    return availability

# Insert a booking in our bookings table
def add_booking(_date, morning_or_afternoon, customer_name):
    try:
        db_name = 'new_schema'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = ("""
        UPDATE bookings 
        SET 
            customer_name = '{customer}',
            morning_or_afternoon = 1 
        WHERE booking_date = '{date}';

        UPDATE availability 
        SET 
            morning_booked_tickets = morning_booked_tickets + 1 
        WHERE booking_date = '{date}';
        """.format(customer=customer_name, date=_date, morning_or_afternoon=morning_or_afternoon))

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to update data on DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# Return all booking details
def get_booking_details(booking_id):
    booking_details = []
    try:
        db_name = 'new_schema'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            SELECT *
            FROM bookings
            WHERE booking_id = '{}' 
            """.format(booking_id)

        cur.execute(query)

        booking_details = cur.fetchall()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")

    return booking_details

# Cancel booking
def cancel_booking_details(booking_id):
    booking_details = []
    try:
        db_name = 'new_schema'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            DELETE *
            FROM bookings
            WHERE booking_id = '{}' 
            """.format(booking_id)

        cur.execute(query)

        booking_details = cur.fetchall()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")

    return booking_details

if __name__ == '__main__':
    app.run(debug=True, port=5001)