def say():
    print('Hello, World!')

import numpy as np
import matplotlib.pyplot as plt
import os

catlogDir=os.getcwd()
baseImgCatlog = catlogDir + "/static/img/baseImg.png"
# 插入底图
baseImg = plt.imread(baseImgCatlog)

step = 0.01
x = np.arange(-10,10,step)
y = np.arange(-10,10,step)

X,Y = np.meshgrid(x,y)
Z = X**2+Y**2
plt.contourf(X,Y,Z, alpha=0.4)
plt.contour(X,Y,Z, alpha=0.1)

plt.imshow(baseImg, extent=[-10, 10, -10, 10]) 
plt.show()