import mysql.connector as sql

# Connect to the database
conn = sql.connect(host='localhost', user='root', password='root', database='railwaydata')
if conn.is_connected():
    print('Successfully connected')
    c1 = conn.cursor()
    
    while True:
        print() 
        print("RAILWAY RESERVATION MANAGEMENT")    
        print("###############################")   
        print() 
        print("1. Add new Passenger Detail")   
        print("2. Add new Train Detail") 
        print("3. Show PNR NO.")    
        print("4. Reservation of Ticket")   
        print("5. Exit")
        
        ch = int(input("Enter your choice: "))
        
        if ch == 1:
            print("Passenger Details Form")
            name = input("Enter your full name: ")
            age = int(input("Enter your age: "))
            gender = input("Enter your gender: ")
            total = int(input("Enter total number of people: "))
            date = input("Enter your date (yyyy-mm-dd): ")
            
            query = "INSERT INTO passenger (name, age, gender, total, date) VALUES (%s, %s, %s, %s, %s)"
            values = (name, age, gender, total, date)
            c1.execute(query, values)
            conn.commit()
            print("Passenger details added successfully.")
        
        elif ch == 2:
            print("Train Details Form")
            train_name = input("Enter train name: ")
            boogie_type = input("Enter boogie type: ")
            seats_available = int(input("Enter number of seats available: "))
            
            query = "INSERT INTO train (train_name, boogie_type, seats_available) VALUES (%s, %s, %s)"
            values = (train_name, boogie_type, seats_available)
            c1.execute(query, values)
            conn.commit()
            print("Train details added successfully.")
        
        elif ch == 3:
            pnr_no = int(input("Enter your PNR NO: "))
            
            query = "SELECT * FROM reservation WHERE pnr_no = %s"
            c1.execute(query, (pnr_no,))
            result = c1.fetchone()
            
            if result:
                print("PNR NO:", result[0])
                print("Passenger ID:", result[1])
                print("Train ID:", result[2])
                print("Seats:", result[3])
                print("Status:", result[4])
            else:
                print("PNR NO not found.")
        
        elif ch == 4:
            print("Reservation of Ticket")
            passenger_id = int(input("Enter your Passenger ID: "))
            train_id = int(input("Enter Train ID: "))
            seats = int(input("Enter number of seats: "))
            
            query = "SELECT seats_available FROM train WHERE train_id = %s"
            c1.execute(query, (train_id,))
            available_seats = c1.fetchone()[0]
            
            if seats <= available_seats:
                status = "Confirmed"
                available_seats -= seats
                query = "UPDATE train SET seats_available = %s WHERE train_id = %s"
                c1.execute(query, (available_seats, train_id))
            else:
                status = "Waiting List"
            
            query = "INSERT INTO reservation (passenger_id, train_id, seats, status) VALUES (%s, %s, %s, %s)"
            values = (passenger_id, train_id, seats, status)
            c1.execute(query, values)
            conn.commit()
            print("Ticket reservation status:", status)
        
        elif ch == 5:
            print("You have exited")
            print("Visit again soon")
            break
        
        else:
            print("Invalid choice, please try again.")
    
    c1.close()
    conn.close()
else:
    print("Connection failed.")
