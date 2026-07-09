class_day_premonth = 12
food_cost_perday = 180
month = 30
wi_fi = 2465
house_rent=input("what is you house rent cost: ")
house = int(house_rent)

def total_cost(house, transport=70):
    cost = house + transport*class_day_premonth + food_cost_perday*month + wi_fi
    return cost
print(f"This is your total monthly cost: {total_cost(house)}.")


