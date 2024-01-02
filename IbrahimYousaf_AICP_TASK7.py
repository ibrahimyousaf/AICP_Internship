#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def setup_charities():
    charities = []
    for i in range(3):
        charity_name = input(f"Enter the name of charity {i + 1}: ")
        charities.append({"name": charity_name, "total": 0})
    return charities

def display_charities(charities):
    print("Choose a charity:")
    for i, charity in enumerate(charities, start=1):
        print(f"{i}. {charity['name']}")

def record_and_total_donation(charities):
    while True:
        try:
            choice = int(input("Enter the number of the chosen charity (1, 2, or 3, -1 to show totals): "))
            
            if choice == -1:
                show_totals(charities)
                continue

            if choice not in [1, 2, 3]:
                raise ValueError("Invalid choice. Please enter 1, 2, 3, or -1.")

            bill_amount = float(input("Enter the value of the customer's shopping bill: "))
            donation = calculate_donation(bill_amount)
            
            charities[choice - 1]['total'] += donation
            print(f"Donation of ${donation} recorded for {charities[choice - 1]['name']}.")

        except ValueError as e:
            print(f"Error: {e}")

def calculate_donation(bill_amount):
    return 0.1 * bill_amount  # 10% of the shopping bill is donated

def show_totals(charities):
    sorted_charities = sorted(charities, key=lambda x: x['total'], reverse=True)
    grand_total = sum(charity['total'] for charity in charities)

    print("\nTotals so far:")
    for charity in sorted_charities:
        print(f"{charity['name']}: ${charity['total']}")

    print(f"\nGRAND TOTAL DONATED TO CHARITY: ${grand_total}")

# Main program
charities = setup_charities()

while True:
    display_charities(charities)
    record_and_total_donation(charities)


# In[ ]:




