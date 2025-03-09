print("Welcome to the tip Calculator!")
Total_bill= float(input("What was the Total Bill? "))
tip= int(input("How much tip would you like to give? 10,12 or 15? "))
people=int(input("How many peeple to split the bill? "))

final_bill= (Total_bill/100) * tip
final_bill1= final_bill + Total_bill
final_pay = final_bill1/people
final= round(final_pay,2)

print(f"Each person should Pay: ${final}")


