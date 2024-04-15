from flask import Flask, jsonify, request
from db_utils import get_all_booking_availability, add_booking, check_availability, update_availability, cancel_booking_details

app = Flask(__name__)

# Endpoint 1: Check Availability for All Dates
@app.route('/availability', methods=["GET"])
def get_availability():
    res = get_all_booking_availability()
    return jsonify(res)

# Endpoint 2: Book Tickets
@app.route('/booking', methods=['POST'])
def book_tickets():
    booking = request.get_json()
    customer_name = booking["customer_name"]
    chosen_date = booking["chosen_date"]
    chosen_slot = booking['chosen_slot']

    availability_results = check_availability(chosen_date, chosen_slot)
    if availability_results:
        booked_tickets = availability_results[0][0]
        max_tickets = availability_results[0][1]
        if booked_tickets < max_tickets:
            add_booking(chosen_date, chosen_slot, customer_name)
            update_availability(chosen_date, chosen_slot)
            return jsonify({"message": "Booking successful"})
        else:
            return jsonify({"error": "No tickets available for the chosen date and slot"}), 400
    else:
        return jsonify({"error": "Invalid date or slot"}), 400

# Endpoint 3: Check availability for a specific date and time slot
@app.route('/availability/<date>', methods=['GET'])
def specific_availability(date):
    chosen_slot = request.args.get('slot')
    available = check_availability(date, chosen_slot)
    return jsonify(available)

# Endpoint 4: Cancel Booking
@app.route('/bookings/<int:name_id>', methods=['DELETE'])
def cancel_booking(name_id):
    deleted = cancel_booking_details(name_id)
    # You can return something here if needed
    return jsonify({"message": "Booking cancelled"})

if __name__ == '__main__':
    app.run(debug=True, port=5002)

