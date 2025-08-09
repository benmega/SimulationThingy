import matplotlib.pyplot as plt
import random
import time

# Enable interactive mode
plt.ion()

# Ask user for number of tosses (default: 1000)
try:
    num_tosses = int(input("Enter number of tosses (default 1000): ") or 1000)
except ValueError:
    num_tosses = 1000

# Ask user for delay speed (default: 0.01 seconds)
try:
    delay = float(input("Enter delay between tosses in seconds (default 0.01): ") or 0.01)
except ValueError:
    delay = 0.01

# Initialize results
results = {'Heads': 0, 'Tails': 0}
labels = list(results.keys())

# Set up plot
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(labels, [0, 0], color=['skyblue', 'salmon'])
ax.set_ylim(0, num_tosses)
ax.set_title('Live Coin Toss Results')
ax.set_xlabel('Outcome')
ax.set_ylabel('Count')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Simulate and update live
for _ in range(num_tosses):
    toss = random.choice(['Heads', 'Tails'])
    results[toss] += 1

    for i, label in enumerate(labels):
        bars[i].set_height(results[label])

    plt.pause(delay)  # Faster updates

# Finalize
plt.ioff()
plt.show()
