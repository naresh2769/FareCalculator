
vehicle_rates = {
    "Economy": 10,
    "Premium": 18,
    "SUV": 25
}

surge_multiplier = 1.5
peak_start_hour = 17
peak_end_hour = 20

def is_peak_hour(hour):
    return peak_start_hour <= hour <= peak_end_hour

def calculate_fare(distance, vehicle_type, hour):

    if vehicle_type not in vehicle_rates:
        raise ValueError("Service Not Available for selected vehicle type.")

    rate_per_km = vehicle_rates[vehicle_type]
    total_fare = distance * rate_per_km

    if is_peak_hour(hour):
        total_fare = total_fare * surge_multiplier

    return total_fare

def print_receipt(distance, vehicle_type, hour, fare):

    print("\n========== CityCab Ride Receipt ==========")
    print("Vehicle Type :", vehicle_type)
    print("Distance     :", distance, "km")
    print("Travel Hour  :", hour)

    if is_peak_hour(hour):
        print("Surge Pricing: Applied (1.5x)")

    print("Total Fare   :", round(fare, 2))
    print("=========================================")

def get_numeric_input(message, data_type=float):

    while True:
        try:
            value = data_type(input(message))
            return value
        except ValueError:
            print("Invalid input. Please enter a correct number.")

def FareCalc():

    print("====== CityCab Fare Calculator ======")

    while True:

        distance = get_numeric_input("Enter travel distance (in km): ")
        hour = get_numeric_input("Enter travel hour (0–23): ", int)
        vehicle_type = input("Enter vehicle type (Economy / Premium / SUV): ")

        try:
            final_fare = calculate_fare(distance, vehicle_type, hour)

            print_receipt(distance, vehicle_type, hour, final_fare)

        except ValueError as error:
            print(error)


if __name__ == "__main__":
    FareCalc()