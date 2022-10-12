#list
'''
data=[1,2,3,5,2,3,1,5]
data1=["ramau","banana"]
print(type(data))
print(type(data1))
print(dir(data1))
#index
print(data.index(5))
print(data.index(1))
#index=data1.index('r')
#print(index)
#count
count=data.count(5)
print(count)
#sort
data1.sort()
print(data1)
data.sort()
print(data)
#copy
data3=data1.copy()
print(data3)
#string
data4="rama is very high"
print(data4.lower())
print(data4.upper())
print(data4.title())
print(data4.rstrip())
print(data4.encode())
print(data4.rsplit())
print(data4.replace("very","good"))
#set
data={"rama","apple"}
print(type(data))
print(dir(data))
print(data.clear())
data.clear()
print(data)
data.add("banana")
print(data)
data.update("rama","sree")
print(data)
#a=data.remove("apple")
#print(data)

data={"name":"rama","code":"python","id_num":2626,"fruites":["apple","banana"]}
print(type(data))
print(dir(data))
print(data.keys())
print(data.values())
print(data.popitem())
'''

'''
#loop
#for #while #nestedloop
data="rama is very good boy"
for i in data:
    print(i)
for i in enumerate(range(1,200)):
    print(i)
data=("rama","puneth")
for index,letter in enumerate(data):
    print(index,letter)
data=[1,2,3,4,5,6,67,7,8,9,8]
for j in (data):
    print(j)
#while
index=0
while index<5:
    index=index+1
    print("rama")
a=[1,3,4,5,6,7,8,9,4]
while a:
    print(a.pop())
    print(a)
a=[1,2,3,4,5,4,6,5,6,8]
#while a:
    #print(a.remove(6)) get aoutput but it was a display error
    #print(a)
#nestedloop

car_name=["tata","motor"]
car_color=["read","blue"]
car_sped=["1234","120120"]
for car_name in car_name:
    for car_color in car_color :
        for car_sped in car_sped:
            print(car_name,car_color,car_sped)


for i in range(1,70):
    for j in range(1,i):
        if (i&j)==2:
            pass
        else:
            print(str(i)+"is primeri number")


for i in range(10):
    if i==15:
        print("if condition",i)
    elif i==3:
                print("elif condition  2",i)
    else:
        print(i)
'''

'''
special_symbol=['@','#','$','%','&','%']
password=input("enter the number password")
values=True
if len(password)<6:
    print("should be atleast ",6)
    val=False
if len(password)<20:
    print("must not be",20)
    val=False
if not any(char.isdigit() for char in password):
    print("shouild be atleast one number")
    val=False
if not any(char.islower() for char in password):
    print("should be atleast one lowercasue")
    val=False
if not any(char.isupper() for char in password):
    print("should be atleast one upper cause")
    val=False
if not any(char in special_symbol for char in password):
    print("should be atleast one special_symbol")
    val=False
if val:
    val=val
    print(val)


data="my first programing"
print(data)


special_symbol=['@']
password=input("enter the emailid")
values=True
if len(password)<6:
    print("should be atleast ",6)
    val=False
if len(password)<20:
    print("must not be",20)
    val=False
if not any(char.isdigit() for char in password):
    print("shouild be atleast one number")
    val=False
if not any(char.islower() for char in password):
    print("should be atleast one lowercasue")
    val=False
if not any(char.isupper() for char in password):
    print("should be atleast one upper cause")
    val=False
if not any(char in special_symbol for char in password):
    print("should be atleast one special_symbol")
    val=False
if val:
    val=val
    print(val)




mobile_number=[1,2,3,4,5,6,7,8,9]
number=input("enter the number")
val=True
if len(number)<10:
    print("should be atleastnumber",10)
    val=False
if val:
    val=val
    print(val)






#function
#arequired
def sum_number(a,b):
    print(a+b)
sum_number(10,12)
sum_number(10,20)
#default
def get_detals(name:"rama",copany:"tata",age:142):
    print(name,copany,age)
get_detals("sree","motor",45)
get_detals("pooja","bike",142)
#keyword
def august_batch(name,id,company):
    print(name,"this is working",id,company)
august_batch(name="rama",company="tata",id=565)
#*argument
def mach_batch(company,*name):  #it was a get tuple
    print(company,name)
    print(type(name))
mach_batch("rama","tata","pooja")
mach_batch("rama","tata","pooja")
mach_batch("rama","tata","pooja","raga","pati")
#**argument
def get_inf(**details):
    print(details)
    print(type(details))
get_inf(name="rama",company="tata",id=23,emailid="rama1@gmai.com")

#lambda
number=[1,2,2,5,4,8,6]
print(list(map(lambda n:n*n,number)))
print(tuple(map(lambda n:n*n,number)))

#filter
number=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda n:n%2!=0,number)))
print(list(filter(lambda n:n%2==1,number)))

import functools
numa=[1,2,3,4,5,6,7,8,9]
print(functools.reduce(lambda a,b:a+b,numa))

#single line concept
#iter
a=["rama","hi","bool"]
print(a)
old=iter(a)
print(next(old))
#zip
num=[1,2,3]
squre=[1,4,9,16]
name=("rama","ranga","raju")
print(list(zip(num,squre,name)))

#genarator
def get_sqnum(n):
    for i in range(1,n+1):
        yield i*i
a=get_sqnum(5)
print("this is squre number1,2,3,----are:")
print(next(a))
print(next(a))
print(next(a))

#list
print([i for i in range(1,50) if i%2==0])
print([i for i in range(1,50) if i%2!=0])
#dict
data=[1,2,3,4,6]
print({v:v*v for v in data})
print({v:v/v for v in range(1,100)})





#file handling
#open methods
#write
file=open("data.txt","w")
file.write("hello brother")
file.close()
#with open methods
with open("data1.txt","w") as file_obj:
    file_obj.write("write the programing")
#read
file=open("data.txt","r")
print(file.readline())
file.close()

with open("data.txt","r") as file_obj:
    print(file_obj.readline())
    file.close()
#append
file=open("data.txt","a")
file.write("\nhi how are yu\n yes iam fine")
file.close()

'''
#regular experssion
#seachr
#match
#findall
#sub
#search
import re
#data="hello ramais fin from 5864,2,method"
#res=re.search(r'.+',data)
#res=re.search(r'\d.',data)
#res=re.search(r'\w+',data)
#res=re.search(r'\w*',data)
#res=re.search(r'\w* \d+',data)
#res=re.search(r'\D',data)
#res=re.search(r'\w+',data)
#res=re.search(r'\w.*',data)
#print(res.group())
#stra= '45871,548755,5894'
#ram=re.search(r'(\d[4])',stra)
ram=re.search(r'(\d{5})',stra)
#ram=re.search(r'(\d{7})',stra)
#print(ram.group(1))
#print(ram.group(2))
#rint(ram.group(0))
mobile=input('enter mobile number')
result=re.match(r'\d[1:9]',mobile)
#print(result.group())
