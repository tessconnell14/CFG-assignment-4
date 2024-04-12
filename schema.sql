USE new_schema;

ALTER TABLE bookings
ADD COLUMN booking_date DATETIME;

ALTER TABLE bookings
ADD CONSTRAINT fk_booking__date
FOREIGN KEY (booking__date)
REFERENCES availability(booking__date);

SELECT * FROM bookings
