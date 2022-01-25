# Question 1..using string related functions

print("1st Question \n ")
line="Python is a case sensitive language"
print(line)
#a:
print("\na:Length of the string is", len(line))
#b:
print("\nb:String in reverse order :", line[::-1])
#c:
cut_line=line[10:27]
print("\nc:",cut_line)
#d:
replcd_line=line.replace("a case sensitive", "object oriented")
print("\nd:After replacing part of string:", replcd_line)
#e:
print("\ne:Index of a is",line.index("a"))
#f:
print("\nf:",line.replace(" ",""))

# Question 2..using String formatting

print("\n2nd Question \n")
Name="Hey, {name} here!".format(name="Arshit")
Sid="My SID is {sid}".format(sid=21104051)
About="I am from {depart} department and my CGPA is {cgpa}".format(depart="Electrical", cgpa=float(9.9))
print(Name)
print(Sid)
print(About)

# Question 3..using bitwise operators

print("\n3rd Question \n")
a=56
b=10
print("a=", a)
print("b=", b)
print("\n")

print("a&b:", a&b)

print("a|b:", a|b)

print("a^b:", a^b)

print("Now left shifting both a and b with 2 bits:", a<<2, b<<2)

print("Now right shifting a with 2 bits and b with 4 bits:", a>>2, b>>4)

# Question 4..finding user given largest no.

print("\n4th Question \n")
numb1=int(input("Enter the first number:"))
numb2=int(input("Enter the second number:"))
numb3=int(input("Enter the third number:"))
if(numb1>numb2 and numb1>numb3):
    print("First number is the greatest:", numb1)
elif(numb2>numb1 and numb2>numb3):
        print("Second number is the greatest:", numb2)
else:
    print("Third number is the greatest:", numb3)

# Question 5..checking word in string

print("\n5th Question \n")
string=str(input("Enter a string:"))
if "name" in string:
    print("Yes")
else:
    print("No")

# Question 6..triangle possibility

print("\n6th Question \n")
len1=int(input("Length of 1st side:", ))
len2=int(input("Length of 2nd side:", ))
len3=int(input("Length of 3rd side:", ))
if len1==0 or len2==0 or len3==0 :#as 0 cant be any side
    print("No")
elif len2+len3>len1 and len1+len3>len2 and len1+len2>len3 :#condition required for a triangle
    print("Yes")
else:
    print("No")


