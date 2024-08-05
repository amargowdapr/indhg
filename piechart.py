from matplotlib import pyplot as pi
us=[12,34,16,45]
la=["Asus","Dell","Lenove","HP"]
e=[0,0,0,0.04]
c=["g","c","#8B0000","#473c8B"]
pi.pie(us,labels=la,startangle=270,explode=e,colors=c,autopct='%1.2f%%')
pi.show()