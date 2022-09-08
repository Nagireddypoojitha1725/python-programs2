#calculate the grade of a student
mark1=int(input("enter the first mark"))
mark2=int(input("enter the second mark"))
mark3=int(input("enter the third mark"))
mark4=int(input("enter the fourth mark"))
mark5=int(input("enter the fifth mark"))
total=mark1+mark2+mark3+mark4+mark5
avg=total/5
if avg>=91 and avg<=100:
                print("your grade is A1")
elif avg>=81 and avg<=90:
                print("your grade is A2")
elif avg>=71 and avg<=80:
                print("your grade is B1")
elif avg>=61 and avg<=70:
                print("your grade is B2")
elif avg>=51 and avg<=60:
                print("your grade is C1")
elif avg>=41 and avg<=50:
                print("your grade is C2")
elif avg>=0 and avg<=50:
                print("your grade is D")
else:
    print("invalid input")
