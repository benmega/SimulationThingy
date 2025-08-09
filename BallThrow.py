def simulate_throw(wind_speed):
    """
    Simulate the final speed of a ball thrown by a professional,
    where wind is blowing *toward* the thrower (headwind).

    Parameters:
    wind_speed (float): Wind speed in m/s, always against the throw (headwind).

    Returns:
    final_speed (float): Resulting speed of the ball in m/s.
    """
    # Professional throw speed (e.g. baseball pitch)
    initial_speed = 40.0  # m/s

    # Since wind opposes the throw, it subtracts from the initial speed
    final_speed = initial_speed - wind_speed

    return final_speed



def main():
    print("Ball Throw Simulation (Wind Blowing Toward Thrower)")
    while True:
        try:
            wind = float(input("Enter wind speed (m/s), wind is always against throw direction: "))
            result = simulate_throw(wind)
            print(f"Final speed of the ball: {result:.2f} m/s")
        except ValueError:
            print("Please enter a valid number.")
            continue  # Go back to input

        # Ask if the user wants to continue
        again = input("Would you like to calculate again? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting simulation. Goodbye!")
            break

# Example interactive usage
if __name__ == "__main__":
    main()
