# now in this chapter we add some or method to  modify our plot
# now we disscuss xlim and ylim
# aghar ham na xaxis and yaxis ki ranges ko control karna ha tab ham ias ka use karay ga
import matplotlib.pyplot as plt
months=[1,2,3,4]
sales=[1000,1500,1200,1800]
plt.plot(months,sales)
# now we enter limt of x asix value matlab input ya months
plt.xlim(1,4)
# now we enter the limit of yaxis ya output matlab values
plt.ylim(0,2000)
# now we discuss xticks and yticks
# ya hamra xaxis or y axis ki values ko replace karna ka lea istamal hota ha
# ias ma ham phlay apni porni values enter karay ga pair new values enter karay ga
# now ham apni xaxis ki values 1,2,3,4 ko M1,M2,M3,M4 ka sath change karty ha
plt.xticks([1,2,3,4],['M1','M2','M3','M4'])
plt.show()