import matplotlib.pyplot as plt
import random

# Enable interactive plotting
plt.ion()

# Get user input
try:
    num_trials = int(input("Enter number of simulations (default 1000): ") or 1000)
except ValueError:
    num_trials = 1000

try:
    delay = float(input("Enter delay between trials in seconds (default 0.01): ") or 0.01)
except ValueError:
    delay = 0.01

# Initialize results
results = {'Switch Wins': 0, 'Stay Wins': 0}
labels = list(results.keys())

# Set up plot
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(labels, [0, 0], color=['green', 'orange'])
ax.set_ylim(0, num_trials)
ax.set_title('Monty Hall Problem Simulation')
ax.set_xlabel('Strategy')
ax.set_ylabel('Wins')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Simulation loop
for _ in range(num_trials):
    # Randomly place the car and make a player choice
    doors = [0, 1, 2]
    car = random.choice(doors)
    player_choice = random.choice(doors)

    # Host opens a goat door
    possible_doors = [door for door in doors if door != player_choice and door != car]
    host_opens = random.choice(possible_doors)

    # Determine switch door
    remaining_doors = [door for door in doors if door != player_choice and door != host_opens]
    switch_choice = remaining_doors[0]

    # Update results
    if switch_choice == car:
        results['Switch Wins'] += 1
    if player_choice == car:
        results['Stay Wins'] += 1

    # Update bars
    for i, label in enumerate(labels):
        bars[i].set_height(results[label])
    plt.pause(delay)

# Finish
plt.ioff()
plt.show()

