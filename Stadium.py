## price per ticket from each category
studentPrice = 9.00
seniorPrice = 12.00
generalPrice = 15.00


print("WELCOME TO THE BROWARD COLLEGE STADIUM!")
print("\n")
## get number of tickets sold from each category
stuTicket = int(input("Enter the number of student tickets sold: "))
print("Student tickets sold: ", stuTicket)
senTicket = int(input("Enter the number of senior tickets sold: "))
print("Senior tickets sold: ", senTicket)
genTicket = int(input("Enter the number of general tickets sold: "))
print("General tickets sold: ", genTicket)
## total number of tickets sold
totalTicket = stuTicket + senTicket + genTicket
print("Total number of tickets sold: ", totalTicket)

## get the revenue of ticket sales from each category
stuRevenue = stuTicket * studentPrice
senRevenue = senTicket * seniorPrice
genRevenue = genTicket * generalPrice
print("\n")
print("Revenue Generated: ")
print("Student Tickets: $","%.2f" %stuRevenue)
print("Senior Tickets: $","%.2f" %senRevenue)
print("General Tickets: $","%.2f" %genRevenue)
totalRevenue = stuRevenue + senRevenue + genRevenue
## total revenue
print("Total Revenue: $", "%.2f" % totalRevenue)
input("Press ENTER to exit")
