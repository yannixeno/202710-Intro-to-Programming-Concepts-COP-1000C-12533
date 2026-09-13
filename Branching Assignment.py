# Electric Charges
# Calculates the total electric bill based on kilowatt hours used.

kw_hours = int(input("Enter the KW hours used: "))

if kw_hours <= 1000:
    amount_owed = kw_hours * 0.07633
else:
    amount_owed = (1000 * 0.07633) + ((kw_hours - 1000) * 0.09259)

amount_owed = round(amount_owed, 5)
print("Amount owed is $" + str(amount_owed))