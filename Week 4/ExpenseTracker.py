print("Welcome to the allowance and expense tracker!")
userAllowance = float(input("Enter your allowance: $"))
savingsGoal = float(input("Set your savings goal: $"))
expenseNum = int(input("How many different expenses do you want to enter? (Enter Number): "))
expenseTotal = 0
MostExpensiveExpense = ""
MostExpensiveExpenseAmount = 0

for i in range (expenseNum):
    expenseVar = input(f"\nExpense {i+1} Name: ")
    expenseAmount = float(input(f"Expense {i+1} Amount: $"))
    expenseTotal += expenseAmount
    if expenseAmount > MostExpensiveExpenseAmount:
        MostExpensiveExpense = expenseVar
        MostExpensiveExpenseAmount = expenseAmount
print(f"\nHere are the total expenses: ${expenseTotal}")

if expenseTotal < userAllowance:
    print("You still have money left over!")
    print(f"You have saved ${userAllowance - expenseTotal}")
    print(f"You are {(userAllowance - expenseTotal)*100/savingsGoal}% of the way to your savings goal!")
elif expenseTotal == userAllowance:
    print("You don't have any money left over!")
    print("You are 0% of the way to your savings goal, trying saving more next time.")
else:
    print("You don't have any money left over!")
    print("Spend less next time!")
    print(f"You owe ${userAllowance - expenseTotal}")
print(f"The most expensive expense was {MostExpensiveExpense} at ${MostExpensiveExpenseAmount}")