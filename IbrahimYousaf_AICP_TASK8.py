#!/usr/bin/env python
# coding: utf-8

# In[7]:


class RowingBoat:
    def __init__(self, rate_hour, rate_half_hour):
        self.rate_hour = rate_hour
        self.rate_half_hour = rate_half_hour
        self.start_time = 10  # 10:00 AM
        self.end_time = 17  # 5:00 PM
        self.money_taken = 0
        self.total_hours_hired = 0
        self.return_time = None

    def hire_boat(self, hours):
        current_time = 12  # Hardcoded to 12:00 PM for the example

        if self.start_time <= current_time <= self.end_time:
            if hours % 0.5 == 0 and 0 < hours <= 8:
                cost = self.calculate_cost(hours)
                self.money_taken += cost
                self.total_hours_hired += hours
                self.return_time = self.calculate_return_time()
                print(f"Boat hired for {hours} hours. Cost: ${cost}")
            else:
                print("Invalid hours. Please hire in 0.5-hour increments, up to a maximum of 8 hours.")
        else:
            print("Boat cannot be hired at this time. Operating hours: 10:00 to 17:00")

    def calculate_cost(self, hours):
        if hours >= 1:
            return self.rate_hour * hours
        else:
            return self.rate_half_hour * hours

    def calculate_return_time(self):
        current_time = 12  # Hardcoded to 12:00 PM for the example
        return current_time + self.total_hours_hired

    def display_daily_totals(self):
        print(f"\nDaily Totals for the Boat:")
        print(f"Money taken: ${self.money_taken}")
        print(f"Total hours hired: {self.total_hours_hired} hours")
        if self.return_time:
            print(f"Boat must be returned by: {self.return_time}")
        else:
            print("No boat hired today.")

# Main program
boat = RowingBoat(rate_hour=20, rate_half_hour=12)

# Attempt to hire the boat outside operating hours
boat.hire_boat(2)

# Display daily totals
boat.display_daily_totals()


# In[8]:


class RowingBoat:
    def __init__(self, boat_id, rate_hour, rate_half_hour, start_time, end_time):
        self.boat_id = boat_id
        self.rate_hour = rate_hour
        self.rate_half_hour = rate_half_hour
        self.start_time = start_time
        self.end_time = end_time
        self.money_taken = 0
        self.total_hours_hired = 0
        self.return_time = None

    def hire_boat(self, hours):
        current_time = 12  # Hardcoded to 12:00 PM for the example

        if self.start_time <= current_time <= self.end_time:
            if hours % 0.5 == 0 and 0 < hours <= 8:
                cost = self.calculate_cost(hours)
                self.money_taken += cost
                self.total_hours_hired += hours
                self.return_time = self.calculate_return_time()
                print(f"Boat {self.boat_id} hired for {hours} hours. Cost: ${cost}")
            else:
                print(f"Boat {self.boat_id}: Invalid hours. Please hire in 0.5-hour increments, up to a maximum of 8 hours.")
        else:
            print(f"Boat {self.boat_id}: Cannot be hired at this time. Operating hours: {self.start_time} to {self.end_time}")

    def calculate_cost(self, hours):
        if hours >= 1:
            return self.rate_hour * hours
        else:
            return self.rate_half_hour * hours

    def calculate_return_time(self):
        current_time = 12  # Hardcoded to 12:00 PM for the example
        return current_time + self.total_hours_hired

    def display_daily_totals(self):
        print(f"\nDaily Totals for Boat {self.boat_id}:")
        print(f"Money taken: ${self.money_taken}")
        print(f"Total hours hired: {self.total_hours_hired} hours")
        if self.return_time:
            print(f"Boat must be returned by: {self.return_time}")
        else:
            print("No boat hired today.")

def find_next_available_boats(boats):
    current_time = 12  # Hardcoded to 12:00 PM for the example
    available_boats = [boat for boat in boats if boat.start_time <= current_time <= boat.end_time]

    if available_boats:
        print(f"Available boats: {[boat.boat_id for boat in available_boats]}")
    else:
        earliest_return_time = min([boat.calculate_return_time() for boat in boats])
        print(f"No boats available. Next available boat will be at {earliest_return_time}.")

# Main program
boats = [
    RowingBoat(1, rate_hour=20, rate_half_hour=12, start_time=10, end_time=17),
    RowingBoat(2, rate_hour=20, rate_half_hour=12, start_time=10, end_time=17),
    # Add more boats as needed
]

# Attempt to hire the first boat for 2 hours
boats[0].hire_boat(2)

# Display next available boats
find_next_available_boats(boats)

# Display daily totals for all boats
for boat in boats:
    boat.display_daily_totals()


# In[9]:


class RowingBoat:
    def __init__(self, boat_id, rate_hour, rate_half_hour, start_time, end_time):
        self.boat_id = boat_id
        self.rate_hour = rate_hour
        self.rate_half_hour = rate_half_hour
        self.start_time = start_time
        self.end_time = end_time
        self.money_taken = 0
        self.total_hours_hired = 0
        self.return_time = None

    def hire_boat(self, hours):
        current_time = 12  # Hardcoded to 12:00 PM for the example

        if self.start_time <= current_time <= self.end_time:
            if hours % 0.5 == 0 and 0 < hours <= 8:
                cost = self.calculate_cost(hours)
                self.money_taken += cost
                self.total_hours_hired += hours
                self.return_time = self.calculate_return_time()
                print(f"Boat {self.boat_id} hired for {hours} hours. Cost: ${cost}")
            else:
                print(f"Boat {self.boat_id}: Invalid hours. Please hire in 0.5-hour increments, up to a maximum of 8 hours.")
        else:
            print(f"Boat {self.boat_id}: Cannot be hired at this time. Operating hours: {self.start_time} to {self.end_time}")

    def calculate_cost(self, hours):
        if hours >= 1:
            return self.rate_hour * hours
        else:
            return self.rate_half_hour * hours

    def calculate_return_time(self):
        current_time = 12  # Hardcoded to 12:00 PM for the example
        return current_time + self.total_hours_hired

    def display_daily_totals(self):
        print(f"\nDaily Totals for Boat {self.boat_id}:")
        print(f"Money taken: ${self.money_taken}")
        print(f"Total hours hired: {self.total_hours_hired} hours")
        if self.return_time:
            print(f"Boat must be returned by: {self.return_time}")
        else:
            print("No boat hired today.")

def generate_daily_report(boats):
    total_money_taken = sum(boat.money_taken for boat in boats)
    total_hours_hired = sum(boat.total_hours_hired for boat in boats)
    unused_boats = [boat.boat_id for boat in boats if boat.total_hours_hired == 0]
    most_used_boat = max(boats, key=lambda x: x.total_hours_hired)

    print("\nDaily Report:")
    print(f"Total money taken for all boats: ${total_money_taken}")
    print(f"Total hours hired for all boats: {total_hours_hired} hours")
    print(f"Number of boats not used today: {len(unused_boats)}")
    print(f"Boat {most_used_boat.boat_id} was used the most, with {most_used_boat.total_hours_hired} hours.")

# Main program
boats = [
    RowingBoat(1, rate_hour=20, rate_half_hour=12, start_time=10, end_time=17),
    RowingBoat(2, rate_hour=20, rate_half_hour=12, start_time=10, end_time=17),
    # Add more boats as needed
]

# Attempt to hire the first boat for 2 hours
boats[0].hire_boat(2)

# Attempt to hire the second boat for 4 hours
boats[1].hire_boat(4)

# Generate daily report
generate_daily_report(boats)


# In[ ]:




