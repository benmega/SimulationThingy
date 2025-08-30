def safe_fork_bomb_simulation(level=0, max_depth=5):
    """Recursively simulate a safe fork bomb without overwhelming the system."""
    print(f"Fork level {level}")
    if level >= max_depth:
        return
    # Simulate forking by calling itself twice
    safe_fork_bomb_simulation(level + 1, max_depth)
    safe_fork_bomb_simulation(level + 1, max_depth)


def main():
    try:
        max_depth = int(input("Enter maximum fork depth (default 5): ") or 5)
    except ValueError:
        max_depth = 5

    safe_fork_bomb_simulation(max_depth=max_depth)


if __name__ == "__main__":
    main()
