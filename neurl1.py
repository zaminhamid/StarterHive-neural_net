#two neurons .

import numpy as np
inputs= [[1,2,3,2.5],
		[2,3,4,0.4],
		[1.2,3,4.9,0.8]]



baises=[ 2,3,0.5]

weights2=[[1,2,1.2],
		[1.1,2.1,3.1],
		[1.0,2.1,-0.9]]


weights=[[0.2,0.8,-0.5,1.0],
		[1,2.1,3.1,1.1],
		[-0.26,-0.27,0.17,0.87]]
		
baises2=[1.2,3,1]#1A1A1A


output1=np.dot(inputs,np.array(weights).T)+baises
output2=np.dot(output1,np.array(weights2).T)+baises2
print(output2)


