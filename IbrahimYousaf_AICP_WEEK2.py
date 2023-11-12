#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[36]:


# Initializing the data
num_journeys = 4
num_coaches = 6
seats_per_coach = 80
ticket_price = 25
departure_times = ["09:00", "11:00", "13:00", "15:00"]
return_times = ["10:00", "12:00", "14:00", "16:00"]
total_passengers_up = [0] * num_journeys
total_money_up = [0] * num_journeys
total_passengers_down = [0] * num_journeys
total_money_down = [0] * num_journeys
available_tickets_up = [[seats_per_coach] * num_coaches for _ in range(num_journeys)]
available_tickets_down = [[seats_per_coach] * num_coaches for _ in range(num_journeys)]

# Storing the data in the form of a dataframe using a dictionary
def display_data():
    data = {
        'Journey': list(range(1, num_journeys + 1)),
        'Departure Time': departure_times,
        'Return Time': return_times,
        'Up Passengers': total_passengers_up,
        'Down Passengers': total_passengers_down,
        'Money Collected Up': total_money_up,
        'Money Collected Down': total_money_down,
    }
    df = pd.DataFrame(data)
    print("\nAfter Booking Tickets:")
    print(df.to_string(index=False))

# Display all the data at the start of the day
display_data()

# Function to book tickets and check for discount and update the price accordingly
def book_tickets(direction, journey_number, num_passengers):
    global total_passengers_up, total_money_up, total_passengers_down, total_money_down, available_tickets_up, available_tickets_down
    if direction == "up":
        for coach in available_tickets_up[journey_number]:
            if num_passengers <= coach:
                coach -= num_passengers
                total_passengers_up[journey_number] += num_passengers
                total_money_up[journey_number] += num_passengers * ticket_price
                if total_passengers_up[journey_number] % 10 == 0:
                    free_tickets = num_passengers // 10
                    total_money_up[journey_number] -= free_tickets * ticket_price
                display_data()
                return True
        else:
            print("Journey", journey_number + 1, "Up is Closed. No available seats.")
            return False
    elif direction == "down":
        for coach in available_tickets_down[journey_number]:
            if num_passengers <= coach:
                coach -= num_passengers
                total_passengers_down[journey_number] += num_passengers
                total_money_down[journey_number] += num_passengers * ticket_price
                if total_passengers_down[journey_number] % 10 == 0:
                    free_tickets = num_passengers // 10
                    total_money_down[journey_number] -= free_tickets * ticket_price
                display_data()
                return True
        else:
            print("Journey", journey_number + 1, "Down is Closed. No available seats.")
            return False

# Function to display the total money collected, total passengers, and the journey with the most passengers
def display_totals():
    total_passengers_day = sum(total_passengers_up) + sum(total_passengers_down)
    total_money_day = sum(total_money_up) + sum(total_money_down)
    print("\nTotal Passengers for the Day:", total_passengers_day)
    print("Total Money Collected for the Day: $", total_money_day)
    most_passengers_journey = max(range(num_journeys), key=lambda i: total_passengers_up[i] + total_passengers_down[i])
    most_passengers = total_passengers_up[most_passengers_journey] + total_passengers_down[most_passengers_journey]
    print("\nJourney with the Most Passengers:")
    print(f"Journey {most_passengers_journey + 1}: {most_passengers} passengers")

# Sample code to book tickets for the trip
book_tickets("up", 0, 80)
book_tickets("up", 1, 70)
book_tickets("up", 2, 60)
book_tickets("up", 3, 50)
book_tickets("down", 0, 40)
book_tickets("down", 1, 30)
book_tickets("down", 2, 80)
book_tickets("down", 3, 80)
display_totals()


# In[ ]:




