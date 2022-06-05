'''###variables

print('a')
a=10
print(a)

a=b=c=10
print(a,b,c)

a,b,c=1,2,3
print(a,b,c)
print('a is',a)
print('b is',b)
print('c is',c)

a=10
user_name='guru'
print(user_name)

a=10
b=20
c=a+b
print(c)

###type conversion
###int to float
a=2
b=float(a)
print(b)
print(type(b))

###float to int
a=2.9
b=int(a)
print(b)
print(type(b))

###int to string
a=20
b=str(a)
print(b)
print(type(b))

###commments
#single line comment
#multiline comment
a=100 #a is a int variable
b=520
print(a+b)

###control statements
##conditional statement[if,else and elif
a=10
b=20
if a==b:
    print('a==b is true')
else:
    print('a==b is false')
##logical operators
a=20
b=30
if a<b and a<b:
    print('true')

else:
    print('false')

a=20
b=30
if a<b or a>b:
    print('true')

else:
    print('false')

###list dat structure

guru=[]
print(guru)

guru=[1,2,3.5,'suvarna',True]
print(len(guru))
print(type(guru))'''

'''#list types
1]append
2]extend
3]remove
4]insert
5]index
6]count'''

'''guru=[1,2,3.5,'suvarna',True]
guru.append(100)
print(guru)
print(type(guru))

guru=[1,2,3.5,'suvarna',True]
guru.extend([22,35,65,88])
print(guru)

guru=[1,2,3.5,'suvarna',True]
guru.insert(1,'python')
print(guru)

guru=[1,2,3.5,'suvarna',True,1,1] ##count was 4 because true is considerer as 1
print(guru.count(1))

guru=[1,2,3.5,'suvarna',True,1,1]
print(len(guru))

guru=[1,2,3.5,'suvarna',True,1,1]
guru.pop(1)
print(guru)

guru=[1,2,3.5,'suvarna',True,1,1]
guru.reverse()
print(guru)

guru=[1,2,3.5,4,8,1,2,102,5,98]
guru.sort()
print(guru)'''

'''##LOOPING STATEMENTS
#FOR LOOP

for i in'guru':
    print(i)

l=[1,2,3,4,5,6]
for i in l:
    print(i)

l=[10,20,30,40,50]
sum=0

for i in l:
    sum=sum+i
    print(sum)


for i in range(1,10,2):
    print(i)

for i in range(0,20,5):
    print(i)

mobiles=['i phone','one plus','mi','real me']
for i in mobiles:
    if i=='i phone':
        print('this is i phone')
    else:
        print('this is not i phone')'''

###while loop
'''while True:
    print('suvarna i love u')'''

'''c=0
while c<3:
    c+=1
    print('c is',c)
else:
    print('completed')'''

'''###tuple

kiran=(1,3.3,'guru')
a=(1,2,3,4)
print(kiran)
print(type(kiran))
print(kiran[2])
print(kiran*2) ##repetations
print(kiran+a) ##concatination
print(2 in a) ##membership
print(6 in a) ##membership

for i in a:
    print(i)  ##iteration

print(min(a))
print(max(a))
print(sum(a))

while True:
    print('hi')
    break'''

'''###break

for val in 'kiran':
    if val=='i':
        break
    print(val)
print('the end')
###continue
for val in 'kiran':
    if val=='i':
        continue
    print(val)
print('the end')'''

'''###STRINGS

s='kiran'
s1="python life"
s2='''
'''this
is
string
'''
'''print(s)
print(s1)
print(s2)
print(type(s))
print(type(s1))
print(type(s2))'''

'''1]replace
2]'''

#1]REPLACE

'''s='kiran'
s1="python life"
s2=
This
is
string
'''
'''h=s2.replace('is','are')
print(h)

h=s2.upper()
print(h)

h=s2.lower()
print(h)

s4='     guru   '

h=s4.strip()
print(h)

h=s4.lstrip()
print(h)

h=s4.rstrip()
print(h)

h=s2.split()
print(h)

h=s.startswith('k')
print(h)

h=s.startswith('i')
print(h)

h=s.endswith('n')
print(h)

h=s.endswith('k')
print(h)

print('my name is {}'.format('kiran'))
print(s2.count('is'))
print(len(s1))'''

'''###set

s={}
print(type(s))

s={1,2,3,'guru'}
print(s)
s.add('python')
print(s)
s.update(['suvarna'])
print(s)
print(len(s))
s.remove('guru')
print(s)

s={1,1,2,2,33,55}
print(s)'''

'''s1={1,2,3,4,5,6}
s2={5,6,7,8,9,100}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))

s1={1,2,3,4,5,6}
s2={5,6,7,8,9,100}
s3=(1,2,3,4)
print(s1.isdisjoint(s2))
print(s1.issubset(s3))'''

###DICTIONARY

dic={}
print(type(dic))

dic={'name':'kiran','age':20}
print(dic)
print(dic['name'])

dic={'name':'kiran',"age":20,'phoneno':[123456779,6465365365,34645455,5454255854]}
print(dic['phoneno'])

###dictionary functions
dic={'name':'kiran',"age":20,'phoneno':[123456779,6465365365,34645455,5454255854]}
dic.pop('name')
print(dic2)

dic.update({'addres':'hyd'})
print(dic)

print(dic.keys())
print(dic.values())

dic.clear()
print(dic)

print('hi')






















