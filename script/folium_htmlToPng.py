import  folium
import  webbrowser
from selenium import webdriver
import time

radarPosition = {'lat': 36.692202, 'lon': 117.130092}

map=folium.Map(
    location=list(radarPosition.values()), 
    # tiles="Spinal Map",
    tiles='http://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7',
    zoom_start=13, 
    control_scale=True,
    zoom_control= True,
    min_zoom = 12,
    max_zoom = 19,
    attr="&copy; <a href=\"http://ditu.amap.com/\">高德地图</a>"
    ) # 绘制地图，确定聚焦点

folium.Marker(
    location=list(radarPosition.values()),
    icon=folium.Icon(color='blue'), 
    tooltip="雷达"
    ).add_to(map)  # 中心点

# 绘制雷达边界
folium.Circle(
    location=list(radarPosition.values()),
    radius=7000,
    color='red', # C4C5C4
    fill=False,
).add_to(map)

map.save('./temp/temp.html')
webbrowser.open('file:///C:/zWork/Study/pythonLeaner/temp/temp.html')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('lang=zh_CN.UTF-8')
chrome_options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')
chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面
chrome_options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--disk-cache=yes')
chrome_options.add_argument('--ignore-ssl-errors=true')
chrome_options.add_argument('--disable-infobars')  # 禁止策略化
chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
# chrome_options.add_argument('--disable-javascript') # 禁用javascript
# chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1030, 1030)  # choose a resolution
driver.get('file:///C:/zWork/Study/pythonLeaner/temp/temp.html')

# You may need to add time.sleep(seconds) here
# time.sleep(5)
# driver.get_screenshot_as_file("./temp/screenshot.png")

driver.quit()