expenses = [2200, 2350, 2600, 2130, 2190];


# 1. In Feb, how many dollars you spent extra compare to January?
def how_much_more_in_feb_jan():
    return expenses[1] - expenses[0]


# 2. Find out your total expense in first quarter (first three months) of the year.
def total_expenses_three_months():
    return expenses[0] + expenses[1] + expenses[2]


# 3. Find out if you spent exactly 2000 dollars in any month
def spent_exactly_two_thousand():
    # GOOD SOLUTION : return 2000 in expenses
    for expense in expenses:
        if expense == 2000:
            return True;
    return False


# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
def add_expense_for_june():
    expenses.append(1980)
    return expenses


# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
def refund_200_from_april():
    expenses[3] -= 200
    return expenses


print('print(how_much_more_in_feb_jan())', how_much_more_in_feb_jan())
print('total_expenses_three_months', total_expenses_three_months())
print('spent_exactly_two_thousand', spent_exactly_two_thousand())
print('add_expense_for_june', add_expense_for_june())
print('refund_200_from_april', refund_200_from_april())
