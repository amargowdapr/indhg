from matplotlib import pyplot as pi
us=[12,32,16,45]
la=["asus","dell","lenovo","hp"]
e=[0,0,0.03,0.04]
c=["green","cyan","red","Blue"]
pi.pie(us,labels=la,startangle=270,explode=e,colors=c,autopct='%1ef%%')
pi.show()