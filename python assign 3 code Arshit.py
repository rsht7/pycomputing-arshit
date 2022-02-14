#Assignment 3 , Arshit Verma , 21104051


#question 1  (Program to tell occurence of words/character)
print('Question 1')
string=input('Enter a string :', )
if ' ' in string :  #space in the string implies sentence containing more than 1 word
    stringlist=string.split()  #turning to list
    word=input('Enter the word you want to count :', )
    print(stringlist.count(word))
else:
    letter=input('Enter the letter you want to count :', )
    print(string.count(letter))
print('\n')


#question 2  (Program to tell the next date of input)
print('Question 2')
day=int(input('enter the day :', ))
month=int(input('enter month :', ))
year=int(input('enter the year :', ))
if 1<=month<=12 and 1<=day<=31 and 1800<=year<=2025  :
    if month in [1,3,5,7,8,10] :  #for months with 31 days leaving december
        if day<=30:
            day=day+1
        elif day==31:
             day=1
             month=month+1
    elif month==2 and year%4 !=0 :  #for feb month of non leap year
        if day<=27:
            day=day+1
        elif day==28:
            day=1
            month=month+1
        elif day>28:
            print('invalid date, this year is not a leap year')
            day='invalid'
            month=' '
            year=' '
    elif month==2 and year%4==0 and 1<=day<=29 :  #for feb month of a leap year
        if day<28 :
            day=day+1
        elif day==28 and year%100==0 :
            if year%400==0 :  #as for year divisible by 4,100 ,it should also be divisible by 400 to be leap year
               day=29
            elif year%400 !=0:
                day=1
                month=3
        elif day==29 :
            if year%100 !=0:
                day=1
                month=3
            elif year%100==0 :
                if year%400==0:
                    day=1
                    month=3
                elif year%400 !=0:
                    print('invalid date, this year is not a leap year')
                    day='invalid'
                    month=' '
                    year=' '
    elif month in [4,6,9,11]: #for months with 30 days
        if day<=29 :
            day=day+1
        elif day==30:
            day=1
            month=month+1
    elif month==12: #for december
        if day<=30:
            day=day+1
        elif day==31: #last day of the year
            day=1
            month=1
            year+=1
            
print(f'The next date is {day}/{month}/{year} .')    #used string formatting        
print('\n')        
        
    
#question 3  (Program to create list of tuples of no. and its square)
print('Question 3')
numbers=input('Enter the number(s) separated by a comma(,): ')
list1=numbers.split(',')
list2=[]
for i in list1:
    tupps=(int(i),int(i)**2) #making a tuple with number and its square
    list2.append(tupps)
print(list1)
print(list2)
print('\n')

#question 4  (Program to tell grade and performance based on input)
print('Question 4')
grade=int(input('Enter your grade :', ))
perfo=''  #creating empty strings
lgrade=''
if 4<=grade<=10:
    if grade==4:
        perfo='Poor'
        lgrade='D'
    elif grade==5:
        perfo='Below average'
        lgrade='C'
    elif grade==6:
        perfo='Average'
        lgrade='C+'
    elif grade==7:
        perfo='Good'
        lgrade='B'
    elif grade==8:
        perfo='Very good'
        lgrade=='B+'
    elif grade==9:
        perfo='Excellent'
        lgrade='A'
    elif grade==10:
        perfo='Outstanding'
        lgrade='A+'
    print(f'Your Grade is {lgrade} and {perfo} Performance')  #using string formatting
else :
    print('Error! , Enter a valid grade')
print('\n')


#question 5  (Program to print the given pattern)
print('Question 5')
string='ABCDEFGHIJK'
print(string)
n=' '
m=0
while len(string)>1:
    string=string[:-2]
    m+=1
    print(n*m+string)  #multiplying the space with increasing value of m
print('\n')    


#question 6  (Script to repeatedly ask user to enter name and SID of students and perform some operations)
print('Question 6')
sid = int(input('Enter the SID: '))
name = input('Enter the name: ')
student={sid:name}
while True:
    reply=input("Do you wish to add another student's details ?(Y or N): ")  #asking repeatedely using while function
    if reply== 'Y':
        sid =int(input('Enter SID: '))
        name =input('Enter Name: ')
        student[sid] = name
    elif reply== 'N':
        break
    else:
     print('Reply is invalid')

#a
print('\na)')
print(student)

#b
print('\nb)')
print({k:v for k,v in sorted(student.items(), key= lambda x:x[1])})

#c
print('\nc)')
print({k:v for k,v in sorted(student.items())})

#d
print('\nd)')
find_student= int(input("Enter the student's SID you want to look for: " ))
print('The student is : ', student[find_student])
print('\n')



#question 7  (Program to print Fibonacci sequence and avg of resl. series)
print('Question 7')
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
terms=int(input('Enter the number of terms to be in the series :', ))
if terms>0 :
   print('Resultant Fibonacci sequence is : ')
   sum=0
   for i in range(terms):
       print(fibo(i))
       sum=sum+fibo(i)
else:
    print(' Error! Enter positive no. of terms') #as negative no. of terms is not possible
avg=float(sum/terms)
print('Average of the resultant Fibonacci Series = ',avg)
print('\n')




#question 8  (Program using set functions)
print('Question 8')
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
print('The given Set1 is', Set1)
print('The given Set2 is', Set2)
print('The given Set3 is', Set3)
print('\n')
#Now the following are the parts of the question
#a)
print('a)')
print('Set of elements in Set 1 and 2 but not both')
condition1 = (Set1|Set2)-(Set1&Set2)
print(condition1)
print('\n')

#b)
print('b)')
print('Set of elements unique to only one of the 3 sets')
condition2 = (Set1|Set2|Set3) - ((Set1&Set2)|(Set2&Set3)|(Set3&Set1))
print(condition2)
print('\n')

#c)
print('c)')
print('New set of elements that are exactly two of the sets Set1, Set2 and Set3')
condition3= ((Set1&Set2)|(Set1&Set3)|(Set3&Set2))-(Set1&Set2&Set3)
print(condition3)
print('\n')

#d)
print('d)')
print('Set of all integers in the range 1 to 10 that are not in Set1.')
cond4= set()
for i in range(1, 11):
    if i not in Set1:
        cond4.add(i)
print(cond4)
print('\n')

#e)
print('e)')
print('Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3')
cond5= set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        cond5.add(i)
print(cond5)
print('\n Thank You')

    
