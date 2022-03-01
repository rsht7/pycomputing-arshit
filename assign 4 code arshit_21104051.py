#Python assignment 4 , Arshit Verma , 21104051 , EE

#ques1 (recursive fn for TOH with 3 disks)

print('Ques 1 \n')

def hanoi(n, fro, to, aux):
    if n == 0:
        return
    
    hanoi(n-1, fro, aux, to)
    print(f'Move Disk {n} from {fro} to {to}')
    hanoi(n-1, aux, to, fro)

#calling our function for 3 disks
hanoi(3, 'rod_1', 'rod_3', 'rod_2')
print('\n')


#ques2 (pascal's triangle)

print('Ques 2 \n ')
n = int(input("Please enter the number of rows to be in Pascal's Triangle: "))

#1)using method of recursions
print('\nUsing recursions:\n')
def pascal(n, real_n=n):
    if n == 0:
        return
    
    pascal(n-1,real_n)

    #printing the spaces
    print('  '*(real_n-n), end='')

    #first number is always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

#2)using loops/iterative procedures
print('\nUsing loops,(iterations):\n')
for line in range(1, n+1):

    #everything else same as recursion
    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()
print('\n')


#ques3 (doing work on 2 input integers)

print('\nQues 3\n')
a=int(input('Enter the first integer: '))
b=int(input('Enter the second integer: '))
rem=a%b
quotient=a//b
print('The remainder is : ', rem)
print('The quotient is : ',quotient)

#a)checking if rem and quotient are callable or not
print('a) Checking if the quotient and remainder is a callable value or not.')
print(callable(quotient))
print(callable(rem))

#b)checking the values for zeroes
print('\nb) Checking for zeroes')
if(rem!=0):
    if (quotient!=0):
        print('Both the values are non zero')
    else:
        print('One value is zero')
else:
    if (quotient!=0):
        print('One value is zero')
    else:
        print('Both the values are zero')
        
#c),d)
print('\nc) and d)')
set1=set()
for i in range (4,7):
    x=rem+i
    y=quotient+i
    if(x>4):
        set1.add(x)
        print(set1)
    if(y>4):
        set1.add(y)
        print(set1)

print(set1)
#e)
print('\ne)')
set2=frozenset(set1)
print('Immutable set: ', frozenset(set1))
#f)
print('\nf)')
print('Largest value in the set: ', max(set2))
max_value=max(set2)
print('Hash value: ', hash(max_value))
print('\n')


#ques4 

print('\nQues 4\n')
class Student:
    def __init__(self, std_name, sid):
        self.name = std_name
        self.rollnumber = sid
    
    def __del__(self):
        print('Object destroyed')

stud1 = Student('Arshit', 21104051)
print('Object created')

#printing the assigned values
print(f'The name of the student is {stud1.name} and roll number is {stud1.rollnumber}.')

#destroying the created object
del stud1
print('\n')


#ques5 (storing and updating details)

print('\nQues 5\n ')
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f'Employee {self.name} record deleted')

#creating records of the employees
employee1 = Employee('Mehak', 40000)
employee2 = Employee('Ashok', 50000)
employee3 = Employee('Viren', 60000)

#a) updating employee1's salary
employee1.salary = 70000
print(f'Part a) The updated salary of the employee {employee1.name} is {employee1.salary}')

#b) deleting the record of an employee
print("Part b) Viren's record has been deleted ", end='')
del employee3
print('\n')


#ques6 (friendship test using functions and dictionary)

print('\nQues 6\n ')
frnd1_word = input('Hey 1st friend, you may enter a word: ')

new_word = input('\nDear 2nd friend, now you shall enter a new meaningful word using only the letters of previously entered word to test your friendship: ')

#defining dictionary
def count_in_dict(frnd1_word):
    count = {}
    word_list = list(frnd1_word)
    
    n = len(word_list)
    for i in range(n):
        if word_list[i] in count:
            count[word_list[i]] += 1
        else:
            count[word_list[i]] = 1
    return count

#now we test the letters of the new word entered 
if count_in_dict(frnd1_word) != count_in_dict(new_word):
    print("The letters entered are not exact, hence, the friendship is fake !")

#shopkeepers verfication
def sk_input():
    ans = input('\nDoes the word make sense?(y or n)\n')

    if ans == 'y':
        print('The friends have passed the friendship test !\n\n')
    elif ans == 'n':
        print("This word has no meaning, hence , the friendship is fake !\n\n")
    else:
        print('Invalid input, please try again')
        sk_input()
sk_input()
print('')
print('\nThank You')

      


