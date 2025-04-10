import random
import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",         # Change if you have a different username
    password="root123",         # Add your MySQL password
    database="bus_booking"
)
cursor = db.cursor()

def ticket_booking():
    # 1. Enter User Details
    name = input("Enter Your Name: ")
    phno = input("Enter Your Phone Number: ")

    # 2. Select Travel Place
    places = ["Chennai - Pune", "Chennai - Madurai", "Chennai - Trichy", "Chennai - Salem", "Chennai - Hyderabad"]
    for i, place in enumerate(places, 1):
        print(f"{i}. {place}")
    place = places[int(input("Enter your Travel Place (1-5): ")) - 1]

    # 3. Select Bus Name
    buses = ["Kumaran Tours and Travels", "Praveen Travels", "RSR Tours and Travels", "ICR Tourism", "Cassio Go Green"]
    for i, bus in enumerate(buses, 1):
        print(f"{i}. {bus}")
    bus = buses[int(input("Enter Your Travel Bus (1-5): ")) - 1]

    # 4. Select Travel Timing
    times = ["6AM - 9AM", "9AM - 12PM", "12PM - 3PM", "3PM - 6PM", "6PM - 9PM"]
    for i, time in enumerate(times, 1):
        print(f"{i}. {time}")
    time = times[int(input("Enter Your Travel Timing (1-5): ")) - 1]

    # 5. Select Pickup Point
    pickup_points = ["Koyambedu", "Tambaram", "Egmore", "Porur", "Perungalathur"]
    for i, pick in enumerate(pickup_points, 1):
        print(f"{i}. {pick}")
    pick = pickup_points[int(input("Enter Your Pickup Point (1-5): ")) - 1]

    # 6. Select Drop Point
    drop_points = ["Swargate", "Mattuthavani", "Gunaseelam", "Kulithalai", "Ameerpet"]
    for i, drop in enumerate(drop_points, 1):
        print(f"{i}. {drop}")
    drop = drop_points[int(input("Enter Your Dropping Point (1-5): ")) - 1]

    # 7. Select Seat Booking
    seats = ["One Person", "Two Persons", "Three Persons"]
    for i, seat in enumerate(seats, 1):
        print(f"{i}. {seat}")
    seat_count = int(input("Enter Your Seat Booking (1-3): "))

    # 8. Select Seat Numbers
    seat_options = ["A1 A2", "B1 B2", "C1 C2", "D1 D2", "E1 E2"]
    for i, seat in enumerate(seat_options, 1):
        print(f"{i}. {seat}")
    seat_numbers = seat_options[int(input("Enter Your Seat Number (1-5): ")) - 1]

    # 9. Generate OTP
    otp = random.randint(1000, 9999)
    print(f"\nOTP sent to your mobile: {otp}")

    # 10. OTP Verification
    while True:
        user_otp = int(input("Enter The OTP: "))
        if user_otp == otp:
            print("\nOTP Verified Successfully!")
            break
        else:
            print("Incorrect OTP... Please try again.")

    # 11. Store Booking in MySQL
    sql = "INSERT INTO bookings (name, phone_number, travel_place, bus_name, travel_time, pickup_point, drop_point, seat_count, seat_numbers, otp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (name, phno, place, bus, time, pick, drop, seat_count, seat_numbers, otp)
    cursor.execute(sql, values)
    db.commit()

    print("\n Booking Successful!!! ")
    print("Ticket Details:")
    print("---------------------------")
    print(f"Name         : {name}")
    print(f"Phone No     : {phno}")
    print(f"Travel Place : {place}")
    print(f"Bus Name     : {bus}")
    print(f"Travel Time  : {time}")
    print(f"Pickup Point : {pick}")
    print(f"Drop Point   : {drop}")
    print(f"Seat Count   : {seat_count}")
    print(f"Seat Number  : {seat_numbers}")

# Run Booking Function
ticket_booking()

# Close the connection
cursor.close()
db.close()
