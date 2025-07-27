# Using List
players = ["Rohit", "Virat", "Gill", "Surya"]

# Dictionary to store runs scored by each player in 3 matches
player_stats = {}

# Input runs for each player using for and while loops
for player in players:
    print(f"\nEnter runs for {player} in 3 matches:")
    match_runs = []
    i = 1
    while i <= 3:
        run = int(input(f"  Match {i} runs: "))
        match_runs.append(run)
        i += 1
    player_stats[player] = match_runs

# Display stats and total
print("\n--- Player Stats ---")
for player in players:
    runs = player_stats[player]
    total = sum(runs)
    avg = total / 3
    print(f"{player}: Runs = {runs}, Total = {total}, Average = {avg:.2f}")

# Simple visualization with stars (1 star = 10 runs)
print("\n--- Run Visualization (1 star = 10 runs) ---")
for player in players:
    total = sum(player_stats[player])
    stars = total // 10
    print(f"{player:6}: {'*' * stars}")
