# Author CCG 10/12/21

amount = input("What is the investment amount?")
rate = input("What is the annual intrest rate as a percent?")
years = input("How many years is the money in the account?")

value = int(amount) * (1 + float(rate) / 12) ** (float(years) * 12)

print("Your account now has " + str(value) + " USD")