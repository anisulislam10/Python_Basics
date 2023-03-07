# a = int(input("Enter Number to check even or odd :"))
# if a % 2 == 0:
#     print("you entered even number")
# else:
#     print("you entered odd number")
studentMarks=float(input("Enter Python final exam Marks: "))
if studentMarks <=49:
    print("So Sad! You Fail the Exam....")
if studentMarks >= 50 and studentMarks <= 60:
    print("you Got D Grade.")
elif studentMarks >=61 and studentMarks<=70:
            print("You Got C Grade")
elif studentMarks>=71 and studentMarks<=80:
            print("You Got B Grade")
elif studentMarks >=81 and studentMarks<=100:
       print("Congrats! Your Got A Grade")
elif studentMarks >100:
    print("Marks Can't be greater then 100...")
else:
 print("Invalid Format!")