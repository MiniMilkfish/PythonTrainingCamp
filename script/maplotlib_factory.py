import numpy.matlib
import numpy as np
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime

catlogDir = os.getcwd()
radarDetectOriginFileCatalog = catlogDir + "/static/json/radarJsonData/"

# 雷达坐标
# radarPosition = {'lat': 30.338573, 'lng': 120.133204}
# 探测数据文件名称

# 球面（地球）坐标系：已知起点、方位角、距离，求坐标
# var rate = Math.cos(startPoint.lat * Math.PI / 180); // 指定纬度球面长度和赤道长度的比率
#     var lat_meter = 111111; // 1纬度 ≈ 111,111米
#     var r = angle * Math.PI / 180.0;
#     var x = Math.sin(r) * distance;
#     var y = Math.cos(r) * distance;
#     x = x / lat_meter / rate; // x偏移量需要根据所在纬度进行计算
#     y = y / lat_meter;
rate = np.cos(np.pi / 180)          # 指定纬度球面长度和赤道长度的比率
axPosition = lambda angle,distance:[np.sin(angle * np.pi / 180.0) * distance / rate, np.cos(angle * np.pi / 180.0) * distance]

# 雷达探测数据可视化生成器
def radarDetectVisualizationGenerator(fileName: str):
    # 探测数据文件目录、存储文件目录
    originFileCatelog = radarDetectOriginFileCatalog + fileName
    targetComposeCatlog = catlogDir + '/temp/' + fileName[0:-5] + '.png'

    # 探测数据文件序列化
    f_obj = open(originFileCatelog)
    datas = json.load(f_obj)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot()

    # 绘制边界
    boundary = plt.Circle(np.array([0, 0]), radius=7, color='#C5C6C5', fill=False, linewidth=1.0)
    ax.add_patch(boundary)

    # 径向数据处理
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
        plt.contourf(X, Y, Z, 
            levels=[0, 50, 100, 150, 200, 300, 500, 800], 
            colors=['#73FF73', '#FFFF82', '#FFB973', '#FF7373', '#AF7373', '#737373', '#555555', '#000000'],
            alpha=1
        )

        # 绘制等高线
        plt.contour(X, Y, Z, 
            levels=[0, 50, 100, 150, 200, 300, 500, 800], 
            colors=['#73FF73', '#FFFF82', '#FFB973', '#FF7373', '#AF7373', '#737373', '#555555', '#000000'],
            linewidths=2.5,
            linestyles='solid',
            alpha=1
        )

    # 坐标轴
    plt.xticks(np.arange(-8, 9))
    plt.yticks(np.arange(-8, 9))
    plt.axis('off')

    # 图片生成
    plt.savefig(targetComposeCatlog, dpi=300, bbox_inches='tight', transparent=True)
    plt.close('all')

originFileList = os.listdir(radarDetectOriginFileCatalog)
secondExpendTotal = 0

for i, fName in enumerate(originFileList):
    starttime = datetime.now()
    radarDetectVisualizationGenerator(fName)
    endtime = datetime.now()
    secondExpend = (endtime - starttime).seconds
    print(str(i + 1) + '/' + str(len(originFileList)) , fName, '耗时：' + str(secondExpend) + ' 秒')
    secondExpendTotal += secondExpend

print("文件数：" + str(len(originFileList)), '共计耗时：' + str(secondExpendTotal) + ' 秒')