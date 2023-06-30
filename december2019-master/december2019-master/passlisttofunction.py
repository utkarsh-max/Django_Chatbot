def count(l):
    even_sum=0
    odd_sum=0
    for i in l:
        if i%2==0:
            even_sum=even_sum+i
        else:
            odd_sum=odd_sum+i
    return even_sum,odd_sum



l=[2,4,5,33,77,46,33,41]
even,odd=count(l)
print("Even=",even,"Odd=",odd)
print("Even:{}  and odd:{}".format(even,odd))