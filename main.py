from MontyHall import main as monty_main
from CoinToss import main as coin_main
from ForkBomb import main as fork_main
from BreadFall import main as bread_main
from BallThrow import main as ball_main

def main_menu():
    while True:
        print("\n🎮 Welcome to the Simulation Center!")
        print("Choose your simulation:")
        print("1. Monty Hall")
        print("2. Coin Toss")
        print("3. Fork Bomb")
        print("4. Bread Fall")
        print("5. Ball Throw")
        print("0. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            monty_main()
        elif choice == "2":
            coin_main()
        elif choice == "3":
            fork_main()
        elif choice == "4":
            bread_main()
        elif choice == "5":
            ball_main()
        elif choice == "0":
            print("Goodbye! Thanks for using the Simulation Center.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
