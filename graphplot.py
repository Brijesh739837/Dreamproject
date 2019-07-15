import matplotlib.pyplot as plt
days=[1,2,3,4,5]
max=[44,77,30,54,83]
min=[10,20,30,40,50]
plt.plot(days,max,color="red")
plt.plot(days,min,color="yellow")
plt.xlabel('Days')
plt.ylabel('Temprature')
plt.title('Weatherinfo')
plt.legend(loc="best",shadow="true",fontsize="large")
plt.savefig("Weather.png")
plt.show()