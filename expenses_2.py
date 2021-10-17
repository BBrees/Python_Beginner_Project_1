total = 0
expenses = []
num_expenses = int(input("How many expenses do you want to enter?"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("We spent $", round(total, 2), " on eating out this weekend.", sep='')

