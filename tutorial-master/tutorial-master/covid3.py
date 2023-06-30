import matplotlib.pyplot as plt

x=[50,108,227,437,525,704,896,918,1463,1540,1975,2411,3875,4213,5242,6088,7466,8380,9971]

y=['20mar','23mar','30mar','1apr','4apr','6apr','10apr','12apr','14apr','20apr','26apr','2may','5may','11may',
   '18may','22may','29may','31may','7jun']

plt.title("New Corona Cases In INDIA")

plt.grid()
plt.fill()
plt.plot(y,x)








plt.show()