# 加载红外图像并根据 JSON 文件中的标注信息，在图像上绘制多边形并填充为黑色，最终生成一个黑白图像
import json
import cv2
from PIL import Image, ImageDraw
import numpy as np

# 文件路径
infrared_image_path = 'batch_data/test/1.jpg'
json_path = 'batch_data/test/1.json'

# 加载红外图像
infrared_image = cv2.imread(infrared_image_path)

# 检查是否成功加载图像
if infrared_image is None:
    raise ValueError(f"无法加载图像: {infrared_image_path}")

# 将红外图像转换为灰度图像
gray_image = cv2.cvtColor(infrared_image, cv2.COLOR_BGR2GRAY)

# 创建一个全白的图像
white_image = np.ones_like(gray_image) * 255

# 加载JSON文件
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 创建PIL图像对象
pil_image = Image.fromarray(white_image)
draw = ImageDraw.Draw(pil_image)

# 在图像上绘制多边形标注并填充为黑色
for shape in data['shapes']:
    points = shape['points']
    polygon = [(point[0], point[1]) for point in points]
    draw.polygon(polygon, fill='black')

# 保存黑白图像
output_image_path = 'output_image.png'
pil_image.save(output_image_path)

# 显示黑白图像
result_image = np.array(pil_image)
cv2.imshow('Black and White Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()