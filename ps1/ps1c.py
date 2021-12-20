annual_salary_real = float(input("Enter the starting salary: "))

semi_annual_raise = 0.07
annual_invest = 0.04
down_payment = 0.25
cost_of_house = 1000000
months = 36
epsilon = 100
low = 0.0
high = 1.0
guess = (high + low) / 2.0
current_savings = 0
steps_in_bisection_search = 0
portion_down_payment = down_payment * cost_of_house
not_possible = False
while abs(current_savings - portion_down_payment) > epsilon:
    if guess == 1.0:
        not_possible = True
        break

    annual_salary = annual_salary_real
    current_savings = 0
    month = 0

    for month in range(36):
        if month % 6 == 0 and month != 0:
            annual_salary += annual_salary * semi_annual_raise
        current_savings += (current_savings * annual_invest / 12 ) + (annual_salary * guess / 12)
    
    if portion_down_payment > current_savings:
        low = guess
    else:
        high = guess

    guess = (high + low) / 2
    steps_in_bisection_search += 1
if not_possible:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate:", guess)
    print("Steps in bisection search:", steps_in_bisection_search)
