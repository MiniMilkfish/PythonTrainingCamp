import numpy.matlib
import numpy as np
import json
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpathes
from skimage import io
from skimage.io.collection import MultiImage

catlogDir = os.getcwd()

fileDate = '20210423074550'
filenameCatlog = catlogDir + "/static/json/" + fileDate + ".json"
baseImgCatlog = catlogDir + "/static/img/baseImg.png"
targetBeforeComposeCatlog = catlogDir + '/temp/' + fileDate + '.png'
targetAfterComposeCatlog = catlogDir + '/temp/afterCompose.png'

f_obj = open(filenameCatlog)
datas = json.load(f_obj)

# 平面坐标系：已知起点、方位角、距离，求坐标
# axPosition = lambda angle,distance:[distance * np.cos(angle), distance * np.sin(angle)]

# 球面（地球）坐标系：已知起点、方位角、距离，求坐标
# var rate = Math.cos(startPoint.lat * Math.PI / 180); // 指定维度球面长度和赤道长度的比率
#     var lat_meter = 111111; // 1维度 ≈ 111,111米
#     var r = angle * Math.PI / 180.0;
#     var x = Math.sin(r) * distance;
#     var y = Math.cos(r) * distance;
#     x = x / lat_meter / rate; // x偏移量需要根据所在维度进行计算
#     y = y / lat_meter;
rate = np.cos(np.pi / 180)          # 指定维度球面长度和赤道长度的比率
axPosition = lambda angle,distance:[np.sin(angle * np.pi / 180.0) * distance / rate, np.cos(angle * np.pi / 180.0) * distance]

# 绘制边界
# fig, ax = plt.subplots()
# boundary = mpathes.Circle(np.array([0, 0]), 7, fill=False, color="red")
# print(type(boundary), boundary)
# ax.add_patch(boundary)

# 插入底图
# baseImg = plt.imread(baseImgCatlog)

contourfC = None
contourC = None
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()

# 绘制边界
boundary = plt.Circle(np.array([0, 0]), radius=7, color='#C5C6C5', fill=False, linewidth=1.0)
ax.add_patch(boundary)

for lineData in datas:
    x = []
    y = []
    angle = lineData['HAngle'] + 312
    distanceArray = [elem for elem in lineData['DistanceArray'] if elem <= 7]
    valueArray = lineData['ValueArray'][0:len(distanceArray)]

    for d in distanceArray:
        currentPos = axPosition(angle, d)
        x.append(currentPos[0])
        y.append(currentPos[1])

    X, Y = np.meshgrid(x, y)
    zMat = np.matlib.identity(len(X), dtype = float)
    for i, elem in enumerate(valueArray):
        zMat[i] *= (elem * 1000 if elem != "NaN" else 0)

    Z = np.array(zMat)
    # 绘制等高线填充颜色
    contourfC = plt.contourf(X, Y, Z, 
        levels=[0, 50, 100, 150, 200, 300, 500, 800], 
        colors=['#73FF73', '#FFFF82', '#FFB973', '#FF7373', '#AF7373', '#737373', '#555555', '#000000'],
        alpha=1
    )

    # 绘制等高线
    contourC = plt.contour(X, Y, Z, 
        levels=[0, 50, 100, 150, 200, 300, 500, 800], 
        colors=['#73FF73', '#FFFF82', '#FFB973', '#FF7373', '#AF7373', '#737373', '#555555', '#000000'],
        linewidths=2.5,
        linestyles='solid',
        alpha=1
    )
    # contourC.set_cmap('hot')
    # contourC.set_clim(0, 800)

# 嵌入底图
# plt.imshow(baseImg, extent=[-8, 8, -8, 8]) 

# 颜色条
# plt.colorbar(contourfC, ticks=[0, 50, 100, 150, 200, 300, 500, 800])

# 坐标轴
plt.xticks(np.arange(-8, 9))
plt.yticks(np.arange(-8, 9))

plt.axis('off')

# 图片生成
plt.savefig(targetBeforeComposeCatlog, dpi=300, bbox_inches='tight', transparent=True)

# ------------------------------------------------
# # 正片叠底算法
# imgMultiply = lambda imga, imgb:imga * imgb

# # 正片叠底构建合成图
# beforeComposeImg = io.imread(targetBeforeComposeCatlog)
# beforeComposeImg = beforeComposeImg/255.0
# print(type(beforeComposeImg), len(beforeComposeImg))

# bottomBackgroundImg = io.imread(baseImgCatlog)
# bottomBackgroundImg = bottomBackgroundImg/255.0
# print(type(bottomBackgroundImg), len(bottomBackgroundImg))

# targetComposeI = imgMultiply(bottomBackgroundImg, beforeComposeImg)
# print(type(targetComposeI), len(targetComposeI))

# io.imsave(targetAfterComposeCatlog, targetComposeI)
# ------------------------------------------------

# 窗口展示
# plt.show() 
