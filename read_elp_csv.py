import pandas as pd
import matplotlib.pyplot as plt
elp_data1=pd.read_csv('elp_data1.csv', header=None)
elp_data2=pd.read_csv('elp_data2.csv', header=None)
plt.figure(figsize=(12,7))
#plt.plot([elp_data1.iloc[0,0]-1000,elp_data1.iloc[0,-1]+1000],[elp_data1.iloc[1,0],elp_data1.iloc[1,-1]])
plt.subplot(2,1,1)
plt.plot(elp_data1.iloc[0,:],elp_data1.iloc[1,:])
#plt.axis('equal')
#plt.xlabel('x(m)')
plt.ylabel('z(m)')
plt.xlim((-150e3,150e3))
plt.ylim((-50e3,0))
plt.title('wide basin boundary')

plt.subplot(2,1,2)
#plt.plot([elp_data1.iloc[0,0]-1000,elp_data1.iloc[0,-1]+1000],[elp_data1.iloc[1,0],elp_data1.iloc[1,-1]])
plt.plot(elp_data2.iloc[0,:],elp_data2.iloc[1,:])
#plt.axis('equal')
plt.xlabel('x(m)')
plt.ylabel('z(m)')
plt.xlim((-100e3,100e3))
plt.ylim((-50e3,0))
plt.title('narrow basin boundary')
plt.show()