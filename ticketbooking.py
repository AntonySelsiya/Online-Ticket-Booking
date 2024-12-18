import random
def ticket_booking():
    #1. Enter User Name & Phone no
    name = input("Enter Your Name : ")
    phno = int(input("Enter the Phone Number : "))

    #2. List Of Places
    print("List Of Places ")
    print("-------------- ")
    print("1.Chennai - Coimbatore")
    print("2.Chennai - Virudhunagar")
    print("3.Chennai - Trichy")
    print("4.Chennai - Madurai")
    print("5.Chennai - Bangalore")
    while True:
        place_choice = int(input("\nEnter your Travel Place : "))
        if(place_choice == 1):
            place = "Chennai - Coimbatore"
            break
        elif(place_choice == 2):
            place = "Chennai - Virudhunagar"
            break
        elif(place_choice == 3):
            place = "Chennai - Trichy"
            break
        elif(place_choice == 4):
            place = "Chennai - Madurai"
            break
        elif(place_choice == 5):
            place = "Chennai - Bangalore"
            break
        else:
            print("Invaild Choice... Please enter a valid Number...")
      
        
    #3. List Of Trains
    print("List Of Trains Names ")
    print("-------------------- ")
    print("1.West Coast Exp")
    print("2.Cheran SF Exp")
    print("3.Tejas Exp")
    print("4.CDG MDU SF Exp")
    print("5.Vaigai SF Exp")
    while True:
        train_choice = int(input("\nEnter Your Train Name : "))
        if(train_choice == 1):
            train = "West Coast Exp"
            break
        elif(train_choice == 2):
            train = "Cheran SF Exp"
            break
        elif(train_choice == 3):
            train = "Tejas Exp"
            break
        elif(train_choice == 4):
            train = "CDG MDU SF Exp"
            break
        elif(train_choice == 5):
            train = "Vaigai SF Exp"
            break
        else:
            print("Invaild Choice... Please enter a valid Number...")

    #4. List of Timings
    print("List of Timings ")
    print("--------------- ")
    print("1.6Am - 9Am")
    print("2.9Am - 12Pm")
    print("3.12Pm - 3Pm")
    print("4.3Pm - 6Pm")
    print("5.6Pm - 9Pm")
    while True:
        time_choice = int(input("\nEnter Your Train Timing :"))
        if(time_choice == 1):
            time = "6Am - 9Am"
            break
        elif(time_choice == 2):
            time = "9Am - 12Pm"
            break
        elif(time_choice == 3):
            time = "12Pm - 3Pm"
            break
        elif(time_choice == 4):
            time = "3Pm - 6Pm"
            break
        elif(time_choice == 5):
            time = "6Pm - 9Pm"
            break
        else:
            print("Invaild Choice... Please enter a valid Number...")    

    #5. List of Pick Up Point
    print("List of Pick Up Point ")
    print("--------------------- ")
    print("1.MGR Central")
    print("2.MGR Central")
    print("3.Egmore")
    print("4.MGR Central")
    print("5.Egmore")
    while True:
        pickup_choice = int(input("\nEnter Your pick Up Point : "))
        if(pickup_choice == 1):
            pick = "MGR Central"
            break
        elif(pickup_choice == 2):
            pick = "MGR Central"
            break
        elif(pickup_choice == 3):
            pick = "Egmore"
            break
        elif(pickup_choice == 4):
            pick = "MGR Central"
            break
        elif(pickup_choice == 5):
            pick = "Egmore"
            break
        else:
            print("Invaild Choice... Please enter a valid Number...")  

    
    #6. List of drop Point
    print("List of drop Point ")
    print("------------------ ")
    print("1.Coimbatore Jun")
    print("2.Virudhunagar Jun")
    print("3.Trichy Jun")
    print("4.Madurai Jun")
    print("5.Bangalore Jun")
    while True:
        drop_choice = int(input("\nEnter Your Dropping Point : "))
        if(drop_choice == 1):
            dropping = "Coimbatore Jun"
            break
        elif(drop_choice == 2):
            dropping = "Virudhunagar Jun"
            break
        elif(drop_choice == 3):
            dropping = "Trichy Jun"
            break
        elif(drop_choice == 4):
            dropping = "Madurai Jun"
            break
        elif(drop_choice == 5):
            dropping = "Bangalore Jun"
            break
        else:
            print("Invaild Choice... Please enter a valid Number...")  


    #7. List of Seat Booking
    print("List of Seat Booking ")
    print("-------------------- ")
    print("1.One Person")
    print("2.Two Persons")
    print("3.Three Persons")
    while True:
        seat_choice = int(input("\nEnter Your Seat Booking :"))
        if(seat_choice == 1):
            seat = "One Person"
            break
        elif(seat_choice == 2):
            seat = "Two Persons"
            break
        elif(seat_choice == 3):
            seat = "Three Persons"
            break
        else:
            print("Invaild Choice... Please enter a valid Number...")
    for i in range(seat_choice):
        print(f"Person {i+1} :")
        a = input("\nEnter Your Name  : ")
        b = int(input("Enter Your Age : "))
        c = input("Enter Your Gender  : ")
        d = int(input("Enter Your Mobile Number : "))
        print(f"\nPerson Information ")
        print("--------------------- ")
        print(f"Name          : {a}")
        print(f"Age           : {b}")
        print(f"Gender        : {c}")
        print(f"Mobile Number : {d}")
        
    #8. List of Seat Number
    print("\nList of Seat Number ")
    print("--------------------- ")
    print("1.A1 A2")
    print("2.B1 B2")
    print("3.C1 C2")
    print("4.D1 D2")
    print("5.E1 E2")
    while True:
        seatno_choice = int(input("\nEnter Your Seat Number :"))
        if(seatno_choice == 1):
            seatnos = "A1 A2"
            break
        elif(seatno_choice == 2):
            seatnos = "B1 B2"
            break
        elif(seatno_choice == 3):
            seatnos = "C1 C2"
            break
        elif(seatno_choice == 4):
            seatnos = "D1 D2"
            break
        elif(seatno_choice == 5):
            seatnos = "E1 E2"
            break
        else:
            print("Invaild Choice... Please enter a valid Number...")
        
    #9.Generate OTP
    otp = random.randint(1000,9999)
    print(f"\nOTP sent to your mobile: {otp}")

    #Enter the OTP
    while True:
        user_otp = int(input("Enter The OTP : "))
        if user_otp == otp:
            print("\nOTP Verification Successfully..!!")
            print("\nYour Booking is Successfully..!!")
            print("\nTicket Booking ")
            print("---------------- ")
            print(f"\nName         : {name}")
            print(f"Mobile No      : {phno}")
            print(f"Place          : {place}")
            print(f"Train Name     : {train}")
            print(f"Travel Time    : {time}")
            print(f"Pick Up Point  : {pick}")
            print(f"Dropping Point : {dropping}")
            print(f"Seat Booking   : {seat}")
            print(f"Seat Number    : {seatnos}")
            break
        else:
            print("Incorrect OTP...Please try again...")

#Call the Function
ticket_booking()
