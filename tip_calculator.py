print("welcome to the tip calculator.")
bill_amount = input("what was the total bill $")
tip_percentage = input("what percent tip would you like to give? 10,12 or 15? ")
total_members = int(input("how many people to split the bill? "))
tip_percentage = (float(tip_percentage)/100) * float(bill_amount)
bill_amount = float(tip_percentage) + float(bill_amount)
total_bill = (bill_amount/total_members)
print(type(total_bill))
result = round(total_bill, 2)
result = f"each person should pay {result}"
# result = str(round(result, 2))
print(result)
# print(str(round(result,2)))
