annual_salary = (float)(input("Enter your annual salary: "))
portion_saved = (float)(input("Enter the portion you want to save, as a decimal: "))
total_cost = (float)(input("Enter the cost of your dream home: "))
"""Portion of Down Payment is 25%"""
portion_down_payment =(float)(0.25 * total_cost)
current_savings=0
months=0
monthly_salary=(float)(annual_salary/12.0)

"""To calculate number of months required"""
while current_savings < portion_down_payment:
    current_savings +=  (current_savings * 0.04 )/ 12  #Monthly interest
    current_savings += portion_saved*monthly_salary  #Monthly savings
    months += 1
    
print("No of months: {}".format(months))