#Strings!

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
if dobDay == "01" or "21" or "31":
    dayDisplay = "You were born on the",dobDay + ending1
elif dobDay == "02" or "22":
    dayDisplay = "You were born on the",dobDay + ending4
elif dobDay == "03" or "23":
    dayDisplay = "You were born on the",dobDay + ending3
else:
    dayDisplay = "You were born on the",dobDay + ending2