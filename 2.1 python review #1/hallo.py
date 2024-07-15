import random

# Generate random temperatures for each day of the week
temperatures = []
for _ in range(7):
    temperatures.append(random.randint(26, 40))

# Days of the week list
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Shelly's Good Days
even_temps_days = []
good_days_count = 0

for i in range(7):
    if temperatures[i] % 2 == 0:
        even_temps_days.append(days_of_the_week[i])
        good_days_count += 1

# Hot and Cold Days
highest_temp = max(temperatures)
lowest_temp = min(temperatures)

highest_temp_day = days_of_the_week[temperatures.index(highest_temp)]
lowest_temp_day = days_of_the_week[temperatures.index(lowest_temp)]

# Above Average Temperatures
average_temp = sum(temperatures) / len(temperatures)
above_avg = [temp for temp in temperatures if temp > average_temp]

# Print the Report
print("Weekly Weather Report:")
print("----------------------")
print("Temperatures for the week:", temperatures)
print("Good days for Shelly (even temperatures):", even_temps_days)
print("Highest temperature:", highest_temp, "on", highest_temp_day)
print("Lowest temperature:", lowest_temp, "on", lowest_temp_day)
print("Average temperature:", average_temp)
print("Days with temperatures above average:", above_avg)
