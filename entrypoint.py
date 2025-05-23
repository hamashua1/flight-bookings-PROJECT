# Function to book a seat

def book_seat(passengers, name, seat):
    if not (1 <= seat <= 10):
        return "Seat number must be between 1 and 10."
    if any(passenger['seat'] == seat for passenger in passengers):
        return f"Seat {seat} is already taken."
    passengers.append({"name": name, "seat": seat})
    return f"Seat {seat} assigned to {name}"

# Function to get the sorted manifest
def get_manifest(passengers):
    return sorted(passengers, key=lambda x: x['seat'])

# Interactive CLI remains for manual use
def assign_flight_seat():
    passengers = []
    while True:
        name = input("Enter passenger name: ")
        try:
            desired_seat = int(input("Enter desired seat number: "))
            result = book_seat(passengers, name, desired_seat)
            print(result)
            if result.startswith("Seat") and "assigned" in result and len(passengers) >= 10:
                print("Flight is now full!")
                break
            if result.startswith("Seat") and "assigned" in result:
                continue_booking = input("Book another seat? (yes/no): ").lower()
                if continue_booking != 'yes':
                    break
        except ValueError:
            print("Please enter a valid seat number!")
            continue
    print("\nFlight Manifest:")
    for passenger in get_manifest(passengers):
        print(f"Seat {passenger['seat']}: {passenger['name']}")

if __name__ == "__main__":
    assign_flight_seat()

