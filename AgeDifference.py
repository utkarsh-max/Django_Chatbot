ram = int(input("Enter Age of Ram :"));
shyam = int(input("Enter Age of Shyam :"));
ajay = int(input("Enter Age of Ajay :"));

if(ram > shyam):
    if(ram > ajay):
        print("Ram is Greatest")
    elif(ajay > ram):
        print("Ajay is Greatest")
elif(ram < shyam):
    if(shyam > ajay):
        print("Shyam is Greatest")
    else:
        print("Ajay is Greatest")