#!/usr/bin/env python
# coding: utf-8

# In[1]:


def check_single_sack():
    while True:
        try:
            content = input("Enter the contents of the sack (C for cement, G for gravel, S for sand): ").upper()
            weight = float(input("Enter the weight of the sack in kilograms: "))

            # Check contents
            if content not in ['C', 'G', 'S']:
                raise ValueError("Incorrect contents")

            # Check weight
            if (content == 'C' and not (24.9 < weight < 25.1)) or                ((content == 'G' or content == 'S') and not (49.9 < weight < 50.1)):
                raise ValueError("Incorrect weight")

            print(f"Accepted: Contents - {content}, Weight - {weight} kg")
            return

        except ValueError as e:
            print(f"Rejected: {e}")

# Main program
check_single_sack()


# In[8]:


def check_single_sack():
    while True:
        try:
            content = input("Enter the contents of the sack (C for cement, G for gravel, S for sand): ").upper()
            weight = float(input("Enter the weight of the sack in kilograms: "))

            # Check contents
            if content not in ['C', 'G', 'S']:
                raise ValueError("Incorrect contents")

            # Check weight
            if (content == 'C' and not (24.9 < weight < 25.1)) or                ((content == 'G' or content == 'S') and not (49.9 < weight < 50.1)):
                raise ValueError("Incorrect weight")

            print(f"Accepted: Contents - {content}, Weight - {weight} kg")
            return content, weight

        except ValueError as e:
            print(f"Rejected: {e}")

def check_customer_order():
    total_weight = 0
    sacks_rejected = 0

    num_cement = int(input("Enter the number of cement sacks: "))
    num_gravel = int(input("Enter the number of gravel sacks: "))
    num_sand = int(input("Enter the number of sand sacks: "))

    for _ in range(num_cement):
        content, weight = check_single_sack()
        total_weight += weight
    
    for _ in range(num_gravel):
        content, weight = check_single_sack()
        total_weight += weight
    
    for _ in range(num_sand):
        content, weight = check_single_sack()
        total_weight += weight

    print(f"Total weight of the order: {total_weight} kg")
    print(f"Number of sacks rejected from the order: {sacks_rejected}")

# Main program
check_customer_order()


# In[9]:


def check_single_sack():
    while True:
        try:
            content = input("Enter the contents of the sack (C for cement, G for gravel, S for sand): ").upper()
            weight = float(input("Enter the weight of the sack in kilograms: "))

            # Check contents
            if content not in ['C', 'G', 'S']:
                raise ValueError("Incorrect contents")

            # Check weight
            if (content == 'C' and not (24.9 < weight < 25.1)) or                ((content == 'G' or content == 'S') and not (49.9 < weight < 50.1)):
                raise ValueError("Incorrect weight")

            print(f"Accepted: Contents - {content}, Weight - {weight} kg")
            return content, weight

        except ValueError as e:
            print(f"Rejected: {e}")

def check_customer_order():
    total_weight = 0
    sacks_rejected = 0

    num_cement = int(input("Enter the number of cement sacks: "))
    num_gravel = int(input("Enter the number of gravel sacks: "))
    num_sand = int(input("Enter the number of sand sacks: "))

    for _ in range(num_cement):
        content, weight = check_single_sack()
        total_weight += weight
    
    for _ in range(num_gravel):
        content, weight = check_single_sack()
        total_weight += weight
    
    for _ in range(num_sand):
        content, weight = check_single_sack()
        total_weight += weight

    return total_weight, num_cement, num_gravel, num_sand

def calculate_order_price(total_weight, num_cement, num_gravel, num_sand):
    COST_CEMENT = 3
    COST_GRAVEL = 2
    COST_SAND = 2
    DISCOUNT_PACK = {'cement': 1, 'gravel': 2, 'sand': 2, 'price': 10}

    regular_price = COST_CEMENT * num_cement + COST_GRAVEL * num_gravel + COST_SAND * num_sand

    # Check for discount packs
    num_discount_packs = min(num_cement, num_gravel // 2, num_sand // 2)
    discount_price = num_discount_packs * DISCOUNT_PACK['price']

    final_price = regular_price - discount_price

    print(f"\nRegular price for the order: ${regular_price}")
    print(f"Discount price for special packs: ${discount_price}")
    print(f"Final price for the order: ${final_price}")
    print(f"Amount saved: ${regular_price - final_price}")

# Main program
total_weight, num_cement, num_gravel, num_sand = check_customer_order()
calculate_order_price(total_weight, num_cement, num_gravel, num_sand)


# In[ ]:




