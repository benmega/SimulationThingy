import matplotlib.pyplot as plt
import random

def run_coin_toss_simulation(num_tosses=1000, delay=0.01):
    """Run a live coin toss simulation with matplotlib."""
    # Initialize results
    results = {'Heads': 0, 'Tails': 0}
    labels = list(results.keys())

    # Set up plot
    plt.ion()
    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(labels, [0, 0], color=['skyblue', 'salmon'])
    ax.set_ylim(0, num_tosses)
    ax.set_title('Live Coin Toss Results')
    ax.set_xlabel('Outcome')
    ax.set_ylabel('Count')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Simulation loop
    for _ in range(num_tosses):
        toss = random.choice(['Heads', 'Tails'])
        results[toss] += 1

        # Update bars
        for i, label in enumerate(labels):
            bars[i].set_height(results[label])

        plt.pause(delay)

    # Finalize
    plt.ioff()
    plt.show()
    return results


def main():
    try:
        num_tosses = int(input("Enter number of tosses (default 1000): ") or 1000)
    except ValueError:
        num_tosses = 1000

    try:
        delay = float(input("Enter delay between tosses in seconds (default 0.01): ") or 0.01)
    except ValueError:
        delay = 0.01

    run_coin_toss_simulation(num_tosses, delay)


if __name__ == "__main__":
    main()
