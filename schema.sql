-- Database for London Attractions CFG group project - London Eye
-- Purpose: to book tickets to attraction

CREATE DATABASE new_schema;
USE new_schema;

-- Create table for booking availability
CREATE TABLE availability
	(booking_date DATETIME NOT NULL PRIMARY KEY,
    morning_booked_tickets INT,
    morning_max_tickets INT,
    afternoon_booked_tickets INT,
    afternoon_max_tickets INT
    );

-- Create table for bookings created
CREATE TABLE bookings
	(name_ID INTEGER auto_increment PRIMARY KEY,
	customer_name VARCHAR(50) NOT NULL,
    booking_date DATETIME,
	morning_or_afternoon INT,
    FOREIGN KEY (booking_date) REFERENCES availability(booking_date)
	);

-- Populate availability table with data
INSERT INTO availability
    (booking_date, morning_max_tickets, afternoon_max_tickets)
    VALUES
    ('2024-04-15', 10, 10),
    ('2024-04-16', 10, 10),
    ('2024-04-17', 10, 10),
    ('2024-04-18', 10, 10),
    ('2024-04-19', 10, 10),
    ('2024-04-20', 10, 10),
    ('2024-04-21', 10, 10);
    
SELECT * FROM bookings
