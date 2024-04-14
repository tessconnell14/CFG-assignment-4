import mysql.connector
from config import USER, PASSWORD, HOST
import random


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


# Map our database schedule to a readable user-friendly schedule
def _map_values(schedule):
    mapped = []
    for item in schedule:
        mapped.append({
            'date': item[0],
            'booked_tickets_morning': item[1],
            'tickets_available_morning': item[2],
            'booked_tickets_evening': item[3],
            'tickets_available_evening': item[4]
        })
    return mapped


# Return all booking availability for a given date
def get_all_booking_availability():
    availability = []
    try:
        db_name = 'new_schema'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            SELECT *
            FROM availability
            """

        cur.execute(query)

        result = cur.fetchall()
        availability = _map_values(result)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed")

    return availability


# Insert a booking in our bookings table
def add_booking(chosen_date, chosen_slot, customer):
    try:
        db_name = 'new_schema'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        name_id = random.randint(1, 1000)

        query = """
            INSERT INTO bookings (name_ID, customer_name, booking_date, morning_or_evening)
            VALUES (
                '{name_id}', 
                '{customer}', 
                '{chosen_date}',
                '{chosen_slot}')
        """.format(name_id=name_id, chosen_slot=chosen_slot, customer=customer, chosen_date=chosen_date)

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to update data on DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Update the availability table
def update_availability(chosen_date, chosen_slot):
    try:
        db_name = 'new_schema'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        name_id = random.randint(1, 1000)

        query = """
            UPDATE availability 
            SET {chosen_slot}_booked_tickets = {chosen_slot}_booked_tickets + 1
            WHERE booking_date = '{chosen_date}'
        """.format(chosen_slot=chosen_slot, chosen_date=chosen_date)

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to update data on DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Check availability for a specific date and timeslot
def check_availability(chosen_date, chosen_slot):
    try:
        db_name = 'new_schema'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            SELECT {chosen_slot}_booked_tickets, {chosen_slot}_max_tickets
            FROM availability
            WHERE booking_date = '{chosen_date}'
        """.format(chosen_slot=chosen_slot, chosen_date=chosen_date)

        cur.execute(query)
        result = cur.fetchall()
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to update data on DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return result


# Delete a booking
def cancel_booking_details(name_id):
    try:
        db_name = 'new_schema'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """DELETE FROM bookings WHERE name_ID = '{}'""".format(name_id=name_id)

        cur.execute(query)
        result = cur.fetchall()
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to update data on DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return result


if __name__ == '__main__':
    app.run(debug=True, port=5001)
