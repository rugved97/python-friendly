if __name__ == '__main__':
    annual_salary = float(input('Enter your annual salary: '))
    # portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
    total_cost = 1000000
    semi_annual_raise = 0.07
    portion_down_payment = 0.25 * total_cost
    required_savings_low = portion_down_payment - 100
    required_savings_high = portion_down_payment + 100

    bisection_low = 0
    bisection_high = 10000
    current_savings = 0
    steps = 0
    while True:
        if bisection_low > bisection_high:
            break

        mid_point = (bisection_high - bisection_low) // 2 + bisection_low
        portion_saved = mid_point / 10000
        portion_saved_monthly = portion_saved * annual_salary / 12
        total_months = 0
        current_savings = 0
        while total_months <= 36:
            annual_salary_temp = annual_salary
            monthly_return = current_savings * 0.04 / 12
            current_savings = current_savings + monthly_return + portion_saved_monthly
            if total_months > 0 and total_months % 6 == 0:
                annual_salary_temp = annual_salary_temp + semi_annual_raise * annual_salary_temp
                portion_saved_monthly = portion_saved * annual_salary_temp / 12
            total_months += 1
        steps += 1
        if current_savings < required_savings_low:
            bisection_low = mid_point
        elif current_savings > required_savings_high:
            bisection_high = mid_point
        else:
            print('Percentage', portion_saved)
            print('Steps', steps)

            break
