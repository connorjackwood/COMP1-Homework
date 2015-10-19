"""#Strings!

#Question1
name = input ("What is your name? ")
print (len(name))

#Question2
name = input ("What is your name? ")
nameLength = (len(name))
nameInitial = name[0]
print("Hello",name +". Your name has",nameLength," characters and your initial is",nameInitial)

#Question3
phone = input("Please enter your mobile number or home telephone number: ")
phoneFront = "+44"
phoneNumber = phone[1:11]
print(phoneFront + phoneNumber)

#Question4
dob = input("Please enter your date of birth in the format 'DD/MM/YYYY': ")
dobDay = dob[0:2]
dobMonth = dob[3:5]
dobYear = dob[6:10]

ending1 = "st"
ending2 = "rd"
ending3 = "th"
ending4 = "nd"
if dobDay == "01" or dobDay == "21" or dobDay == "31":
    dayDisplay = "You were born on the " + dobDay + ending1
elif dobDay == "02" or dobDay =="22":
    dayDisplay = "You were born on the " + dobDay + ending4
elif dobDay == "03" or dobDay == "23":
    dayDisplay = "You were born on the " + dobDay + ending2
else:
    dayDisplay = "You were born on the " + dobDay + ending3

if dobMonth == "01":
    monthDisplay = "of the " + dobMonth+ending1 + " month" 
elif dobMonth == "02":
    monthDisplay = "of the " + dobMonth+ending4 + " month" 
elif dobMonth == "03":
    monthDisplay = "of the " + dobMonth+ending2 + " month"
else:
    monthDisplay = "of the " + dobMonth+ending3 +  " month"

yearDisplay = "in " + dobYear

print (dayDisplay,monthDisplay,yearDisplay + ".") """

#Question5

dob = input("Please enter your date of birth in the format 'DD/MM/YYYY': ")
dobDay = dob[0:2]
dobMonth = dob[3:5]
dobYear = dob[6:10]

ending1 = "st"
ending2 = "rd"
ending3 = "th"
ending4 = "nd"
if dobDay == "01" or dobDay == "21" or dobDay == "31":
    dayDisplay = "You were born on the " + dobDay + ending1
elif dobDay == "02" or dobDay =="22":
    dayDisplay = "You were born on the " + dobDay + ending4
elif dobDay == "03" or dobDay == "23":
    dayDisplay = "You were born on the " + dobDay + ending2
else:
    dayDisplay = "You were born on the " + dobDay + ending3

if dobMonth == "01":
    monthWord= "January"
elif dobMonth == "02":
    monthWord = "February" 
elif dobMonth == "03":
    monthWord = "March"
elif dobMonth == "04":
    monthWord = "April"
elif dobMonth == "05":
    monthWord = "May"
elif dobMonth == "06":
    monthWord = "June"
elif dobMonth == "07":
    monthWord = "July"
elif dobMonth == "08":
    monthWord = "August"
elif dobMonth == "09":
    monthWord = "September"
elif dobMonth == "10":
    monthWord = "October"
elif dobMonth == "11":
    monthWord = "November"
else:
    monthWord= "December"

monthDisplay = "of " + monthWord

yearDisplay = "in " + dobYear

print (dayDisplay,monthDisplay,yearDisplay + ".")
