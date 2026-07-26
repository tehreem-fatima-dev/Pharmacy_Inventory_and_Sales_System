 
# Pharmacy Inventory and Sales System v1.0

def get_medicine_name():
    medicine_name = input("Enter medicine name: ")
    return medicine_name
def get_medicine_price():
    price_per_unit = float(input("Enter medicine price per unit: "))
    while price_per_unit < 20:
        print("Invalid Price!")
        price_per_unit =  float(input("Please enter valid price per unit: "))
    return price_per_unit

def get_stock_quantity():
    stock_quantity = int(input("Enter medicine stock quantity: "))
    while stock_quantity < 0:
        print("Invalid Input!")
        stock_quantity = int(input("Please enter valid input: "))
    return stock_quantity

def stock_status(stock_quantity):
    if 0 < stock_quantity <= 15:
        status = "Only "  + str(stock_quantity) + " left in stock!" 
    elif stock_quantity == 0:
        status = "Out Of Stock!"
    else:
        status = "Enough medicine is in stock!"
    return status

def pharmacy_summary():
    print("=" * 36)
    print("         PHARMACY SUMMARY         ")
    print("=" * 36)
    print()
    print("Total Medicines Processed      =", num)
    print("Total Stock Quantity           =", total_stock)
    print("Total Price                    =", total_price)
    print()
    print("Most Expensive Medicine Name   =", maximum_price_medicine)
    print("Most Expensive Medicine Price  =", maximum_price)
    print()
    print("Most Cheapest Medicine Name    =", minimum_price_medicine)
    print("Most Cheapest Medicine Price   =", minimum_price)
    print()
    print("Out Of Stock Medicines         =", out_of_stock_medicines)
    print("=" * 36)

    # MAIN BODY

total_stock = 0
total_price = 0
prices = []
names = []
out_of_stock_medicines = []
num = int(input("how many medicines do you want to process? "))
while num <= 0:
    print("Invalid Input!")
    num = int(input("Please enter valid number of medicines: "))
for i in range(num):
    name = get_medicine_name()
    names.append(name)
    price_per_unit = get_medicine_price()
    stock_quantity = get_stock_quantity()
    status = stock_status(stock_quantity)
    print(status)
    prices.append(price_per_unit)
    if status == "Out Of Stock!":
       out_of_stock_medicines.append(name)
    total_stock += stock_quantity
    total_price += (price_per_unit * stock_quantity)

    # finding maximum and minimum

maximum_price = prices[0]
minimum_price = maximum_price
maximum_price_medicine = names[0]
minimum_price_medicine = maximum_price_medicine
for i in range(len(names)):
    if prices[i] > maximum_price:
        maximum_price = prices[i]
        maximum_price_medicine = names[i]
    if prices[i] < minimum_price:
        minimum_price = prices[i]
        minimum_price_medicine = names[i]
    
pharmacy_summary()