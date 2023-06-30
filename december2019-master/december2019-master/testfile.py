f=open("ram.txt","r")
print(f)
#print(f.read())
#print(f.readline(44))
#print(f.readlines())

for data in f:
    print(data,end="")
f.close()
f2=open("abc.txt","w")

l=[1,"\n",2,"\n",3,"\n",4,"\n",5]
l2=["a","\n","b","\n","c"]
f4=open("abc1.txt","a")
f4.writelines("ram")
f4.writelines("roha ")
f4.writelines(l2)


'''f2.write("ram \n")
f2.write("rohan")'''
f2.close()

f3=open("abc.txt","r")
print(f3.read())


f5=open("mohan.txt","w")
f7=open("ram.txt","r")
for data1 in f7:
    f5.write(data1)


ph=open("L.gif","rb")
ph2=open("h.gif","wb")
for x in ph:
    print(x)
    ph2.write(x)

