f=open("Ram.txt","r")
# to read all data from file
#print(f.read())

# to read character
#print(f.readline(5))

# gives output in the form of list
#print(f.readlines())

#f.write("fsdfsdf")

'''for i in range(5):
    a=input("Enter your name")
    f.writeline(a)
 '''
####    ########################
'''f2=open("copy.txt","a")
for data in f:
    print(data,end="")
    f2.write(data)


f.close()
f2.close()

f3=open("test.gif","rb")
f4=open("fest.gif","wb")
for data in f3:
    print(data)
    f4.write(data)
'''
p=f.readlines()
print(p)
l=[1,"\n",2,"\n",3,"\n",4,"\n",5]
l2=["a","\n","b","\n","c"]
f4=open("abc1.txt","a")
f4.writelines("ram")
f4.writelines("rohan ")
f4.writelines(l2)
f4.write("ram \n")
f4.write("rohan")
f4.writelines(p)