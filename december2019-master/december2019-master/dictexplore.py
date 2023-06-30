test={}
test['ram']=66
test['mohan']=67
print(test)

phonelist={'ram':'lg','rohan':'samsung'}
print(phonelist)

print(phonelist.keys())

print(phonelist.items())

print(phonelist.values())

print(phonelist['ram'])


s=dict()
print(type(s))
print(s)
#copy one dict to another
s=dict(phonelist)
print(s)

print(len(s))

print('ram' in test)
del (s['rohan'])
print(s)