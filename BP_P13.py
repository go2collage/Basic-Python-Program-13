# Basic Python Program

# marks of Subejct & display grade

math = int(input("Enter Math subject marks:"))
science = int(input("Enter Science subject marks:"))
english = int(input("Enter English subject marks:"))
history = int(input("Enter History  subject marks:"))
hindi = int(input("Enter Hindi subject marks:"))

total = math + science + english + history + hindi

avg = total / 5

if avg<=99 and avg>=80:
    print("A grade with percentage is: ", avg)

elif avg<=80 and avg>=60:
    print("B grade with percentage is: ", avg)

elif avg<=60 and avg>=40:
    print("C grade with percentage is: ", avg)

else:
    print("Fail or ATKT pass.")


