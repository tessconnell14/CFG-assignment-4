from flask import Flask, jsonify, request
from db_utils import get_all_booking_availability, add_booking, check_availability, cancel_booking_details

app = Flask(__name__)


# Endpoint 1: Check Availability for a Specific Date
@app.route('/availability', methods=["GET"])
def check_availability():
    res = get_all_booking_availability()
    return jsonify(res)

# Endpoint 2: Book Tickets
@app.route('/booking', methods=['PUT'])
def book_tickets():
    booking = request.get_json()
    add_booking(
        customer=booking["customer_name"],
        chosen_date=booking["date"],
        chosen_slot=booking['morning_or_afternoon'],
    )

    return jsonify(booking)


# Endpoint 3: Check availability for a specific date and time slot
@app.route('/availability/<date>', methods=['GET'])
def specific_availability(chosen_date, chosen_slot):
    available = check_availability(chosen_date, chosen_slot)
    return jsonify(available)

# Endpoint 4: Cancel Booking
@app.route('/bookings/<int:name_id>', methods=['DELETE'])
def cancel_booking(name_id):
    deleted = cancel_booking_details(name_id)
    return jsonify(deleted)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
