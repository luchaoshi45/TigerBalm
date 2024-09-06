# 检测图像中的绿色并绘制中心线
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image_path = "image/6D2FC6DD19344D2995395337177_6B3BA536_10D3C.jpg"
image = cv2.imread(image_path)

# 转换为HSV颜色空间以便提取绿色
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义绿色的HSV范围
lower_green = np.array([40, 40, 40])
upper_green = np.array([70, 255, 255])

# 创建掩码
mask = cv2.inRange(hsv, lower_green, upper_green)

# 寻找轮廓
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 计算质心
M = cv2.moments(contours[0])
if M["m00"] != 0:
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
else:
    cX, cY = 0, 0

# 计算中间线
rows, cols = mask.shape
[vx, vy, x, y] = cv2.fitLine(contours[0], cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)

# 确保 lefty 和 righty 是整数类型
lefty = int(lefty)
righty = int(righty)

# 绘制结果
result_image = image.copy()
cv2.line(result_image, (cols - 1, righty), (0, lefty), (0, 0, 255), 2)
cv2.circle(result_image, (cX, cY), 5, (255, 0, 0), -1)

# 可视化结果
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
plt.title("Center Line")
plt.show()
