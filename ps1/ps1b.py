annual_salary = int(input("Enter the annual salary: "))
portion_saved = float(input("Enter the percent of salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = total_cost * 0.25

num_of_months = 0
current_savings = 0
invest = 0.04
while current_savings < portion_down_payment:
    current_savings += (annual_salary * portion_saved / 12) + (current_savings * invest / 12)
    num_of_months += 1
    if num_of_months % 6 == 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)

print("Number of months:",num_of_months)