if __name__ == '__main__':
    annual_salary = float(input('Enter your annual salary: '))
    portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
    total_cost = float(input('Enter the cost of your dream home: '))
    portion_down_payment = 0.25 * total_cost
    current_savings = 0
    portion_saved_monthly = portion_saved * annual_salary / 12
    total_months = 0
    while current_savings < portion_down_payment:
        monthly_return = current_savings * 0.04 / 12
        current_savings = current_savings + monthly_return + portion_saved_monthly
        total_months += 1

    print('Number of months: ', total_months)
