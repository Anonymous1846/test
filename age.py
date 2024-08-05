from datetime import date

print(f"Welcome to age verify [{date.today()}]")
age = int(input("Enter the age:"))
if age>17:
	print("You're a adult")
else:
	print("Not")
