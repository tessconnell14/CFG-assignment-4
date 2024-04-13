from flask import Flask, jsonify, request
from db_utils import get_all_booking_availability

app = Flask(__name__)


# GET - information about availability

@app.route('/availability')
def get_bookings():
    res = get_all_booking_availability()
    return jsonify(res)


# PUT - Add a booking
#
# @app.route('/booking', methods=['PUT'])
# def book_attraction():
#     booking = request.get_json()
#     add_booking(
#         _date=booking['date'],
#         london_attraction=booking['londonAttraction'],
#         time=booking['time'],
#         customer=booking['customer']
#     )
#
#     return jsonify(booking)


# DELETE - Deleting a booking that has been made
# PATCH - Updating part of the booking

if __name__ == '__main__':
    app.run(debug=True, port=5002)
