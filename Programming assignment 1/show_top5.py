# Open the scores.txt
file = open("scores.txt", "r")
lines = file.readlines()

#create a dictionary to track the wins
user_stats = {}

#for loop to count all lines
for line in lines:
    parts = line.strip().split(",")

    #find player stats
    username = parts[0]
    time = parts[1]
    user_score = int(parts[2])
    pc_score = int(parts[3])

    #is player stats are not in the disctonary then add them
    if username not in user_stats:
        user_stats[username] = {"wins": 0}

    #win counter for each person
    if user_score > pc_score:
        user_stats[username]["wins"] += 1

#convert the dict to a sorted list
sorted_users = sorted(user_stats.items(),key=lambda x: x[1]["wins"],reverse=True)

#display the top 5 players in a good looking way
print("--- THE TOP 5 PLAYERS ARE!! ---")
print(f"{'RANK:':<5}{'USERNAME:':<15}{'WINS:':<10}")

for rank, (username, stats) in enumerate(sorted_users[:5], start=1):
    print(f"{rank:<5}{username:<15}{stats['wins']:<10}")
