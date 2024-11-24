def assign_flight_seat():
    passengers = []
    while True:
        name = input("Enter passenger name: ")
        
        try:
            desired_seat = int(input("Enter desired seat number: "))
            if desired_seat > 10:
                print("Sorry, flight capacity is small. We only have seats 1-10.")
                continue
            
            # Check if seat is already taken
            if any(passenger['seat'] == desired_seat for passenger in passengers):
                print(f"Seat {desired_seat} is already taken. Please choose another seat.")
                continue
                
            passengers.append({"name": name, "seat": desired_seat})
            print(f"Seat {desired_seat} assigned to {name}")
            
            if len(passengers) >= 10:
                print("Flight is now full!")
                break
            
            continue_booking = input("Book another seat? (yes/no): ").lower()
            if continue_booking != 'yes':
                break
                
        except ValueError:
            print("Please enter a valid seat number!")
            continue
    
    print("\nFlight Manifest:")
    for passenger in sorted(passengers, key=lambda x: x['seat']):
        print(f"Seat {passenger['seat']}: {passenger['name']}")

if __name__ == "__main__":
    assign_flight_seat()

