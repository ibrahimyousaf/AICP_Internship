#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np


# In[25]:


ComputerShop= {      #Initializing a dictionary that has headings as keys and the rest of the corresponding data as values of the respective keys 
'Category': ['Case', 'Case', 'RAM', 'RAM', 'RAM', 'Main Hard Disk Drive', 'Main Hard Disk Drive', 'Main Hard Disk Drive',
                 'Solid State Drive', 'Solid State Drive', 'Second Hard Disk Drive', 'Second Hard Disk Drive', 'Second Hard Disk Drive', 
                 'Optical Drive', 'Optical Drive', 'Operating System', 'Operating System'],
'Item code': ['A1', 'A2', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'E1', 'E2', 'E3', 'F1', 'F2', 'G1', 'G2'],
'Description': ['Compact', 'Tower', '8 GB', '16 GB', '32 GB', '1 TB HDD', '2 TB HDD', '4 TB HDD', '240 GB SSD', '480 GB SSD',
                    '1 TB HDD', '2 TB HDD', '4 TB HDD', 'DVD/Blu-Ray Player', 'DVD/Blu-Ray Re-writer', 'Standard Version',
                    'Professional Version'],
'Price ($)': [75.00, 150.00, 79.99, 149.99, 299.99, 49.99, 89.99, 129.99, 59.99, 119.99, 49.99, 89.99, 129.99, 50.00, 100.00,
                  100.00, 175.00]
}

ComputerShop_df = pd.DataFrame(ComputerShop) #Initializing a dataframe that takes the dictionary declared above as input


# In[26]:


ComputerShop_df


# # TASK 1

# In[27]:


item_code_array = ComputerShop_df['Item code'].to_numpy()
description_array = ComputerShop_df['Description'].to_numpy()
price_array = ComputerShop_df['Price ($)'].to_numpy()
print("Item Code Array:", item_code_array)
print("Description Array:", description_array)
print("Price Array:", price_array)


# In[28]:


# Initializing a list to store all the choices of the customers
chosen_items = {'Case': None, 'RAM': None, 'Main Hard Disk Drive': None}

# Function that takes the Item code as input and verifies if correct input is given by the user
def choose_item(category):
    while True:
        print(f"Choose a {category}:")
        category_df = ComputerShop_df[ComputerShop_df['Category'] == category]
        print(category_df[['Item code', 'Description', 'Price ($)']])
        item_choice = input("Enter the item code: ")
        if item_choice in category_df['Item code'].values:
            return item_choice
        else:
            print("Invalid item code. Please choose a valid item.")

# Loop to allow the user to pick a Case, RAM, and Hard Disk Drive as mentioned in the question
for category in chosen_items.keys():
    chosen_items[category] = choose_item(category)

# Calculating the total price of the computer
total_price = 200  # initialized the price to 200$ as it is mentioned that the basic components cost 200$
total_price += sum(ComputerShop_df[ComputerShop_df['Item code'].isin(chosen_items.values())]['Price ($)'])

# Prompt the user for the Operating System choice
while True:
    os_choice = input("Do you want an Operating System (Y/N)? ").strip().lower()
    if os_choice in ['y', 'n']:
        break
    else:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

os_price = 0.0
os_item_code = None

if os_choice == 'y':
    os_item_code = choose_item('Operating System')
    os_price = ComputerShop_df[ComputerShop_df['Item code'] == os_item_code]['Price ($)'].values[0]
    total_price += os_price

# Output the chosen items and the total price
print("\nChosen Items:")
for category, item_code in chosen_items.items():
    description = ComputerShop_df[ComputerShop_df['Item code'] == item_code]['Description'].values[0]
    price = ComputerShop_df[ComputerShop_df['Item code'] == item_code]['Price ($)'].values[0]
    print(f"{category}: {description} (Item Code: {item_code}), Price: ${price}")

if os_price > 0:
    os_description = ComputerShop_df[ComputerShop_df['Category'] == 'Operating System']['Description'].values[0]
    print(f"Operating System: {os_description} (Item Code: {os_item_code}), Price: ${os_price}")
print ("The Price of the Basic Components is:  $200")
print(f"Total Price of the Computer: ${total_price}")


# # TASK 2

# In[33]:


# Initializing a list to store all the choices of the customers
chosen_items = {'Case': None, 'RAM': None, 'Main Hard Disk Drive': None}
additional_items = {}  # Initialize a dictionary to store additional items chosen by the customer

# Function that takes the Item code as input and verifies if correct input is given by the user
def choose_item(category):
    while True:
        print(f"Choose a {category}:")
        category_df = ComputerShop_df[ComputerShop_df['Category'] == category]
        print(category_df[['Item code', 'Description', 'Price ($)']])
        item_choice = input("Enter the item code (or 'N' to skip): ")
        
        if item_choice == 'N':
            return None  # Customer chose not to purchase this category
        elif item_choice in category_df['Item code'].values:
            return item_choice
        else:
            print("Invalid item code. Please choose a valid item or 'N' to skip.")

# Loop to allow the user to pick a Case, RAM, and Hard Disk Drive as mentioned in the question
for category in chosen_items.keys():
    chosen_items[category] = choose_item(category)

# Prompt the user to purchase additional items from other categories
while True:
    additional_choice = input("Do you want to purchase items from other categories (Y/N)? ").strip().lower()
    if additional_choice == 'n':
        break
    elif additional_choice != 'y':
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        continue

    category = input("Enter the category (or 'N' to skip): ").strip()
    if category == 'N':
        continue
    elif category not in ComputerShop['Category']:
        print("Invalid category. Please choose a valid category or 'N' to skip.")
        continue

    item_code = choose_item(category)
    if item_code:
        additional_items[category] = item_code

# Calculating the total price of the computer
total_price = 200  # initialized the price to 200$ as it is mentioned that the basic components cost 200$

# Calculate the price of the chosen items
chosen_item_codes = list(chosen_items.values())
total_price += sum(ComputerShop_df[ComputerShop_df['Item code'].isin(chosen_item_codes)]['Price ($)'])

# Calculate the price of additional items
additional_item_codes = list(additional_items.values())
total_price += sum(ComputerShop_df[ComputerShop_df['Item code'].isin(additional_item_codes)]['Price ($)'])

# Output the chosen and additional items and the new total price of the computer
print("\nChosen Items:")
for category, item_code in chosen_items.items():
    if item_code:
        description = ComputerShop_df[ComputerShop_df['Item code'] == item_code]['Description'].values[0]
        price = ComputerShop_df[ComputerShop_df['Item code'] == item_code]['Price ($)'].values[0]
        print(f"{category}: {description} (Item Code: {item_code}), Price: ${price}")

print("\nAdditional Items:")
for category, item_code in additional_items.items():
    description = ComputerShop_df[ComputerShop_df['Item code'] == item_code]['Description'].values[0]
    price = ComputerShop_df[ComputerShop_df['Item code'] == item_code]['Price ($)'].values[0]
    print(f"{category}: {description} (Item Code: {item_code}), Price: ${price}")
print ("The Price of the Basic Components is:  $200")
print(f"New Total Price of the Computer: ${total_price}")


# # TASK 3

# In[34]:


num_additional_items = len(additional_items)
# Apply a discount based on the number of additional items purchased
discount = 0  # Initialize discount to 0%
if num_additional_items == 1:
    discount = 5
elif num_additional_items >= 2:
    discount = 10
# Calculate the amount saved and the new price after the discount
amount_saved = (discount / 100) * total_price
discounted_price = total_price - amount_saved

# Output the chosen and additional items, the original total price, the discount, amount saved, and the new total price
print("\nChosen Items:")
for category, item_code in chosen_items.items():
    if item_code:
        description = ComputerShop_df[ComputerShop_df['Item code'] == item_code]['Description'].values[0]
        price = ComputerShop_df[ComputerShop_df['Item code'] == item_code]['Price ($)'].values[0]
        print(f"{category}: {description} (Item Code: {item_code}), Price: ${price}")

print("\nAdditional Items:")
for category, item_code in additional_items.items():
    description = ComputerShop_df[ComputerShop_df['Item code'] == item_code]['Description'].values[0]
    price = ComputerShop_df[ComputerShop_df['Item code'] == item_code]['Price ($)'].values[0]
    print(f"{category}: {description} (Item Code: {item_code}), Price: ${price}")

print(f"Original Total Price of the Computer: ${total_price}")
print(f"Discount Applied: {discount}%")
print(f"Amount Saved: ${amount_saved}")
print(f"New Total Price of the Computer after Discount: ${discounted_price}")


# In[ ]:




