"""
ATM Access Program

This lets user enter their account pin 3 times.
"""
entries = 1
while entries < 4:
    pin = input("Please enter your 4 digit pin code: ")
    if pin == "1234":
        print("Welcome.  Your account balance is 1 bajillion dollars!!!")
        exit()
    else:
        print("Your entry is incorrect.")
        entries += 1
print("Thief!!! Stay where you are and put your arms over your head!!!")
