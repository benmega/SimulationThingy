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
            print("Launching Monty Hall Simulation...")
            import MontyHall
        elif choice == "2":
            print("Launching Coin Toss Simulation...")
            import CoinToss
        elif choice == "3":
            print("Launching Fork Bomb Simulation...")
            import ForkBomb
        elif choice == "4":
            print("Launching Bread Fall simulation...")
            from BreadFall import main
            main()
        elif choice == "5":
            print("Launching Ball Throw simulation...")
            from BallThrow import main
            main()
        elif choice == "0":
            print("Goodbye! Thanks for using the Simulation Center.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# import importlib
# import sys
#
# class SimulationSelector(GridLayout):
#     def __init__(self, **kwargs):
#         super(SimulationSelector, self).__init__(**kwargs)
#         self.cols = 1
#         self.padding = 20
#         self.spacing = 20
#
#         self.add_widget(Label(text="🎮 Simulation Selector", font_size=32, size_hint=(1, 0.2)))
#
#         button_grid = GridLayout(cols=3, spacing=10, size_hint=(1, 0.6))
#
#         # Add buttons 1 to 5
#         for i in range(1, 6):
#             button_grid.add_widget(Button(text=f"{i}", font_size=24, on_press=self.run_simulation))
#
#         # Close button
#         close_btn = Button(text="Close", font_size=24, on_press=self.close_app)
#         button_grid.add_widget(close_btn)
#
#         self.add_widget(button_grid)
#
#     def run_simulation(self, instance):
#         sim_number = instance.text
#         print(f"Launching Simulation {sim_number}...")
#         try:
#             sim_number = int(sim_number)
#             if sim_number == 1:
#                 importlib.import_module("MontyHall")
#             elif sim_number == 2:
#                 importlib.import_module("CoinToss")
#             elif sim_number == 3:
#                 importlib.import_module("ForkBomb")
#             elif sim_number == 4:
#                 mod = importlib.import_module("BreadFall")
#                 if hasattr(mod, "main"):
#                     mod.main()
#             elif sim_number == 5:
#                 print("Launching Custom Simulation 5...")
#             else:
#                 print("Invalid selection.")
#         except Exception as e:
#             print(f"Error: {e}")
#
#     def close_app(self, instance):
#         App.get_running_app().stop()
#         sys.exit()
#
# class SimulationApp(App):
#     def build(self):
#         return SimulationSelector()
#
# if __name__ == "__main__":
#     SimulationApp().run()

