#from math import *
num=float(input("Enter your weight in kilogram"))
num1=float(input("Enter your height in meter"))
print("Your weight = " ,num ,"KG","And Height = ",num1 ,"m")
bmi=num/(num1*num1)
#bmi=fabs(bmi)
if bmi<=15:
    print("Your BMI is ",bmi," And you are in Starvation")
elif (bmi>=15.1) and (bmi<=17.5):
    print("Your BMI is ",bmi," And you are in Anorexic")
elif (bmi>=17.6) and (bmi<=18.5):
    print("Your BMI is ",bmi," And you are in Underweight")
elif (bmi>=18.6) and (bmi<=24.9):
    print("Your BMI is ",bmi," And you are in Ideal")
elif (bmi>=25) and (bmi<=25.9):
    print("Your BMI is ",bmi," And you are in Overweight")
elif (bmi>=26) and (bmi<=30.9):
    print("Your BMI is ",bmi," And you are in Obese")
else:
    print("Your BMI is ",bmi," And you are in Morbidly Obese")