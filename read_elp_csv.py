import pandas as pd
import matplotlib.pyplot as plt
elp_data1=pd.read_csv('elp_data1.csv', header=None)
elp_data2=pd.read_csv('elp_data2.csv', header=None)
plt.figure(figsize=(12,4))
plt.plot([elp_data1.iloc[0,0]-1000,elp_data1.iloc[0,-1]+1000],[elp_data1.iloc[1,0],elp_data1.iloc[1,-1]])
plt.plot(elp_data1.iloc[0,:],elp_data1.iloc[1,:])
plt.plot(elp_data2.iloc[0,:],elp_data2.iloc[1,:])
plt.axis('equal')
plt.xlabel('x(m)')
plt.ylabel('z(m)')
plt.legend(['ground surface','wide basin boundary','narrow basin boundary'])
plt.show()