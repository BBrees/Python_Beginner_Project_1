total = 0
expenses = []
for i in range(7):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("We spent $", round(total, 3), " on eating out this weekend.", sep='')
