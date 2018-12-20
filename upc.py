##UPC barcode checker - [2018-12-17] Challenge #370 [Easy] UPC check digits - /r/dailyprogrammer
## Tom Smith - 2018
##Sum the digits at odd-numbered positions (1st, 3rd, 5th, ..., 11th). If you use 0-based indexing, this is the even-numbered positions (0th, 2nd, 4th, ... 10th).
#Multiply the result from step 1 by 3.
#Take the sum of digits at even-numbered positions (2nd, 4th, 6th, ..., 10th) in the original number, and add this sum to the result from step 2.
#Find the result from step 3 modulo 10 (i.e. the remainder, when divided by 10) and call it M.
#If M is 0, then the check digit is 0; otherwise the check digit is 10 - M.


#Firstly take the input of the UPC number and check that it is an 11 digit string. The while loop will check if it is anything other and if so will ask user to enter again
while True:
    upc = input("Please enter a UPC number and the checksum will be calculated ")
    if len(upc) != 11:
        print("Please enter an 11 digit UPC number ")
    else:
        break

#Main body of program. This will take the users input and perform the necessary arithmetical steps to create the checksum
#Firstly this will convert the input to a list by using the list function(converting to a string first with the str function)
upclist = list(str(upc))
#Secondly this will sum the odd numbered digits in the 11 digit string. Reminder - this uses 0 based indexing so the first character in the list will be 0
sumtotal1 = int(upclist[0]) + int(upclist[2]) + int(upclist[4]) + int(upclist[6]) + int(upclist[8]) + int(upclist[10])
#Thirdly this will multiply the sumtotal1 variable by 3 and output this value to sumtotal2
sumtotal2 = sumtotal1 * 3
#Next, this will sum the even numbered digits in the 11 digit string. Reminder - this uses 0 based indexing so the first character in the list will be 0
sumtotal3 = int(upclist[1]) + int(upclist[3]) + int(upclist[5]) + int(upclist[7]) + int(upclist[9])
#Add the two totals together
sumtotal4 = sumtotal2 + sumtotal3
#Find the modulo or remainder when divided by 10 of the previous figure and store as M
M = sumtotal4 % 10

#Simple if statement that checks to see if M = 0 and if so to use that as the checksum else it will use 10 - M value
if M == 0:
    upclist.append(0)
else:
    upclist.append(10 - M)

#This will take the list and combine it together into one long string and then output this to the user
string = ''.join(map(str, upclist))
print(string)
