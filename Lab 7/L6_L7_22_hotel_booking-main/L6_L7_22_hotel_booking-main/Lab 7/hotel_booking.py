def nights_stayed(days):
    if not isinstance(days, str):
        return None

    parts = days.split("-")
    if len(parts) != 2 or not all(part.strip().isdigit() for part in parts):
        return None

    check_in, check_out = (int(part.strip()) for part in parts)
    if check_out < check_in:
        return None
    return check_out - check_in

def room_floor(room_code):
    if not isinstance(room_code, str):
        return None

    parts = room_code.split("-")
    if len(parts) != 2 or not parts[0].strip() or not parts[1].strip().isdigit():
        return None
    return int(parts[1].strip()[0])

def booking_label(names_csv):
    if not isinstance(names_csv, str):
        return None

    names = [name.strip() for name in names_csv.split(",") if name.strip()]
    if not names:
        return None
    lead = names[0]
    return lead[0].upper() + lead[1:] + " +" + str(len(names) - 1)

def main():
    print("==== Running nights_stayed ====")
    user_input = input("Enter check-in and check-out day (e.g. 12-15): ")
    result = nights_stayed(user_input)
    print("Nights:", result)

    print("\n==== Running room_floor ====")
    user_input = input("Enter a room code (e.g. D-305): ")
    result = room_floor(user_input)
    print("Floor:", result)

    print("\n==== Running booking_label ====")
    user_input = input("Enter guest names as CSV (e.g. ravi, priya): ")
    result = booking_label(user_input)
    print("Booking Label:", result)

if __name__ == "__main__":
    main()
