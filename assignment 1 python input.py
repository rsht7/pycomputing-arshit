# QUESTION 1

number1=int(input( 'please enter the first number :' ))
number2=int(input( 'please enter the second number :' ))
number3=int(input( 'please enter the third number :' ))
average=number1+number2+number3
print( ' The average of the three numbers is :' , average/3)
print('thank you')
print()
print()

# QUESTION 2

Gincome=int(input('please enter the gross income to the nearest penny : $' ))
depend=int(input('please enter the number of dependents :' ))
tincome=Gincome-10000-depend*3000
tax=tincome*20/100
print('your income tax : $',tax) 
print('thank you')
print()
print()

# QUESTION 3

sid=int(input('SID:' ,))
name=input('Name:' ,)
gender=input('Gender:' ,)
course=input('Course Name:' ,)
cgpa=float(input('CGPA:' ,))
Student=[sid ,name ,gender ,course ,cgpa ]
print('Student:' ,Student)
print()
print()

# QUESTION 4

stdn1=int(input('Student 1 marks:' ,))
stdn2=int(input('Student 2 marks:' ,))
stdn3=int(input('Student 3 marks:' ,))
stdn4=int(input('Student 4 marks:' ,))
stdn5=int(input('Student 4 marks:' ,))
marks=[stdn1,stdn2,stdn3,stdn4,stdn5]
marks.sort()
print(marks)
print()
print()

# QUESTION 5

color=['Red','Green','White','Black','Pink','Yellow']
print(color)
print()
del color[3]
print('New list', color)
print()
color=['Red','Green','White','Black','Pink','Yellow']
color[3]='Purple'
del color[4]
print('After replacement', color)


