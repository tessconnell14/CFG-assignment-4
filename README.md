# Assignment-4
This repo contains the CFG degree Assignment 4 group project work by InnovateHERs:
Sarah, Shelly, Shradha, Tess and Emese. &lt;3

> "Empowering Innovation, One Line of Code at a Time"

[Kanban board](https://miro.com/app/board/uXjVKWg95GQ=/)

This project includes the design and implementation of an API

---

### 🎡 London Eye Booking API 🎡

**Introduction**

Welcome to the London Eye Booking API documentation! This API allows users to check availability and make bookings for slots at the London Eye attraction.

![Image of the London Eye, added in the markdown](https://github.com/Szkazka/Assignment-4/assets/152419320/5bc1a5fa-1af8-472d-9fee-a918fdc78497)


## Installation Requirements

Before running the API, ensure you have the following installed:

- Python 3.x
- Flask
- MySQL server
  
You can install Flask and other dependencies using pip:

pip install Flask
pip install pymysql  # for MySQL database interaction

## Configuration

**Database Configuration:**
Create a MySQL database with the provided schema. You can use the provided SQL script to create the necessary tables and populate them with sample data.

Update the config.py file with your database connection details.

**Flask Configuration:**
Open config.py and set DEBUG = True for development mode.

Ensure that HOST is set correctly.

## Running the API

To run the London Eye Booking API, follow these steps:

**Start the Flask Application:**
Navigate to the root directory of the project.

**Run the following command in the terminal:**
python app.py

This will start the Flask application, and the API will be accessible at the specified host and port (default: http://localhost:5002).

**Interacting with the API:**
You can now interact with the API using client applications, scripts, or tools like Postman.

Check the API endpoints (/availability, /bookings, etc.) to view available slots, make bookings, and retrieve booking information.

# Example Usage

Here's an example of how to use the API:

_**Check Availability:**_
Send a GET request to /availability endpoint to check available slots.

_**Make Booking:**_
Send a POST request to /bookings endpoint with customer name, booking date, and morning/afternoon selection to make a booking.

_**Expected Outcome:**_
Upon starting the API, it should connect to the MySQL database and be ready to handle requests.

Users should be able to check availability, make bookings, and retrieve booking information through the API endpoints.

Successful requests will return the relevant data with appropriate status codes, while unsuccessful requests will return error messages.

## Getting Started

To get started with the London Attractions project, follow these steps:

- [ ] Clone the repository
   
- [ ] Navigate to the project directory
  
- [ ] Install dependencies
  
- [ ] Start the development server
  

## Contributing

> [!TIP]
> Contributions to the London Attractions project are welcome! To contribute, follow these steps:
> 1. Fork the repository.
> 2. Create a new branch for your feature or bug fix.
> 3. Make your changes, commit them, and push to your fork.
> 4. Submit a pull request with a detailed description of your changes.

## Using GIT COMMANDS

- Checking status using git status in the command line

  ![Screenshot of git status command](https://github.com/Szkazka/Assignment-4/assets/160747463/3a61162c-adf0-4383-8df8-7e32877e4156)

  - The rest can be seen in the project history.



---

