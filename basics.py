import datetime
print("the date and time is", datetime.datetime.now())

def myname(lis):
    p=(len(lis))
    return p
print(myname([1,2,3,4]))    


marks = [12, 23, 12, 456, 6778]
print(marks[:-1])
print(marks)
x=10
y = '12'
m='haki'
z = 1.2
print(m)
print(y + y)
print(type(z), type(y))


p = list(range(1,10,2))
print(p)


total=sum(marks)
print(total)

length=len(marks)
print(length)
avg = total / length
print(avg) 
maq = marks.count(12)
print(maq)

mask = {"as": 12, "ps": 123, "def": 12}
sdf = len(mask.values())
print(sdf)
print(sdf.count())