def safe_fork_bomb_simulation(level=0, max_depth=5):
    print(f"Fork level {level}")
    if level >= max_depth:
        return
    # Simulate forking by calling itself twice
    safe_fork_bomb_simulation(level + 1, max_depth)
    safe_fork_bomb_simulation(level + 1, max_depth)

safe_fork_bomb_simulation()
