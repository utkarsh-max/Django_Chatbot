'''import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(4000)
'''
i=0
def greet():
    global i
    print(i,"Good morning")
    i=i+1
    if i<400:
        greet()


greet()