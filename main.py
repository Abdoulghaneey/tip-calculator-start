#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip Calculator!")
total_amount = float(input('What was the total amount? Naira '))
tip = float(input('How much you like to give? 12 24 50 75 '))
friends = int(input('How many friends to split?  '))
total_with_tip = tip / 100 * total_amount + total_amount
print(total_with_tip)
