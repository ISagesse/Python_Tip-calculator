
print("Welcome to the tip calculator.");

totalBill = float(input("What was the total bill? "));

people = int(input("How many people that will split the bill? "));

tipPercentage = int(input("What percentage of tip would you be given? 10%, 12%, or 15%? "));

percent = (100 + tipPercentage) / 100

totalAmount = (totalBill / people) * percent

rounded = str(round(totalAmount, 2));

print("Each person should pay $" + rounded)