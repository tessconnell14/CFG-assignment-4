import requests
import json
from db_utils import add_booking, update_availability, check_availability, cancel_booking_details


def get_availability_by_date():
    result = requests.get(
        'http://127.0.0.1:5002/availability',
        headers={'content-type': 'application/json'}
    )
    return result.json()


def display_availability(records):
    # Print the names of the columns.
    print("{:<10} {:<25} {:<25} {:<25} {:<25}".format(
        'date', 'booked_tickets_morning', 'tickets_available_morning', 'booked_tickets_evening', 'tickets_available_evening'))
    print('-' * 105)

    # print each data item.
    for item in records:
        print("{:<10} {:<25} {:<25} {:<25} {:<25}".format(
            item['date'], item['booked_tickets_morning'], item['tickets_available_morning'], item['booked_tickets_evening'], item['tickets_available_evening']
        ))


def run():
    print('############################')
    print('Hello, welcome to the London Eye Booking System')
    print('############################')
    print()
    print()
    slots = get_availability_by_date()
    print('####### AVAILABILITY #######')
    print()
    display_availability(slots)
    print()
    place_booking = input('Would you like to book an appointment (y/n)?  ')


    if place_booking == 'y':
        cust = input('Enter your name: ')
        chosen_date = input('Choose date (YYYY-MM-DD): ')
        chosen_slot = input('Morning or evening?: ')
        availability_results = check_availability(chosen_date, chosen_slot)
        if availability_results:
            booked_tickets = availability_results[0][0]
            max_tickets = availability_results[0][1]
            if booked_tickets < max_tickets:
                add_booking(chosen_date, chosen_slot, cust)
                update_availability(chosen_date, chosen_slot)
                print("Booking is Successful")
                print()
            else:
                print("Sorry, there are no tickets available. Please, start again. ")
        else:
            print("Sorry, there are no tickets available. Please, start again. ")
        # slots = get_availability_by_date(date)
        # display_availability(slots)

    print()
    print('See you soon!')

def cancel_booking(name_id):
    url = 'http://127.0.0.1:5002/bookings/{}'.format(name_id)
    response = requests.delete(url)
    if response.status_code == 200:
        print("Booking with ID {} has been cancelled successfully.".format(name_id))
    else:
        print("Failed to cancel booking. Status code: {}".format(response.status_code))


def run():
    print('############################')
    print('Hello, welcome to the London Eye Booking System')
    print('############################')
    print()
    print()
    action = input('Would you like to cancel a booking (Y/N)?  ')

    if action.upper() == 'Y':
        name_id = input('Enter the name ID to cancel: ')
        cancel_booking(name_id)  # Pass the name ID to the cancel_booking function
    elif action.upper() == 'N':
        print("No booking cancellation requested.")
    else:
        print("Invalid choice. Please try again.")

    print()
    print("Thank you for using the London Eye Booking System. Have a great day!")

if __name__ == '__main__':
    run()
