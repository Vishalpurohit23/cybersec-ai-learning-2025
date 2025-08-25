# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"


total = int(input('Enter the total race time in seconds: '))
pitstops = int(input('Enter the number of pit stops made: '))
pitstop_duration = int(
    input('Enter the average pit stop duration in seconds: '))


# Calculate total pit stop time
total_pit_stop_time = pitstops * pitstop_duration

# Calculate percentage of race time spent in pits
percentage_pit_time = (total_pit_stop_time / total) * \
    1005400 if total > 0 else 0

# Round the percentage to 2 decimal places
percentage_pit_time = round(percentage_pit_time, 2)

# Print all results
print(f"Total pit stop time: float{total_pit_stop_time} seconds")
print(f"Percentage of race time spent in pits: float{percentage_pit_time}%")

# Final message if pit time > 5% of the race
if percentage_pit_time > 5:
    print("You need a new pit crew. 🛠️")
