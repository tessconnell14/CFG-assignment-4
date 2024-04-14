from flask import Flask, jsonify, request
from db_utils import get_all_booking_availability, add_booking, get_booking_details, cancel_booking_details

app = Flask(__name__)


# Endpoint 1: Check Availability for a Specific Date
@app.route('/availability/<date>', methods=["GET"])
def check_availability(date):
    res = get_all_booking_availability(date)
    return jsonify(res)

# Endpoint 2: Book Tickets
@app.route('/booking', methods=['PUT'])
def book_tickets():
    booking = request.get_json()
    add_booking(
        _date=booking['date'],
        morning_or_afternoon=booking['morning_or_afternoon'],
        customer_name=booking['customer_name']
    )

    return jsonify(booking)

# Endpoint 3: Retrieve Booking Details
@app.route('/bookings/<int:booking_id>', methods=['GET'])
def booking_details(booking_id):
    reservation = get_booking_details(booking_id)
    return jsonify(reservation)

# Endpoint 4: Cancel Booking
@app.route('/bookings/<int:booking_id>', methods=['DELETE'])
def cancel_booking(booking_id):
    deleted = cancel_booking_details(booking_id)
    return jsonify(deleted)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
