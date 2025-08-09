import math

def calculate_fall_time(height_meters):
    if height_meters < 0:
        raise ValueError("Height cannot be negative.")
    gravity = 9.81  # m/s²
    time = math.sqrt((2 * height_meters) / gravity)
    return time

def main():
    while True:
        try:
            height_input = float(input("Enter height in meters: "))
            time_to_fall = calculate_fall_time(height_input)
            print(f"\nTime for the bread to fall from {height_input} meters is {time_to_fall:.2f} seconds.")
        except ValueError as e:
            print(f"Error: {e}")
            continue  # Ask again if input is invalid

        choice = input("\nDo you want to calculate another fall time? (Y/N): ").strip().lower()
        if choice != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
