# 对图像进行骨架化处理并绘制外接矩形
import cv2
import numpy as np

def skeletonize(image):
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = image
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    size = np.size(binary)
    skeleton = np.zeros(binary.shape, np.uint8)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    finished = False

    while not finished:
        eroded = cv2.erode(binary, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(binary, temp)
        skeleton = cv2.bitwise_or(skeleton, temp)
        binary = eroded.copy()

        zeros = size - cv2.countNonZero(binary)
        if zeros == size:
            finished = True

    return skeleton


def fit_line_least_squares(points):
    [vx, vy, x, y] = cv2.fitLine(points, cv2.DIST_L2, 0, 0.01, 0.01)
    lefty = int((-x * vy / vx) + y)
    righty = int(((points.shape[1] - x) * vy / vx) + y)
    return (0, lefty), (points.shape[1] - 1, righty)


# 读取图像
image = cv2.imread('image/shap_mask2.png')
if image is None:
    print("Error: Could not read the image file.")
    exit()

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 二值化处理
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 细化（骨架化）图像
skeleton = skeletonize(binary)

# 查找骨架图像中的非零像素
points = np.column_stack(np.where(skeleton > 0))

# 如果有足够的点，则拟合直线
if len(points) > 0:
    # 使用最小二乘法拟合直线
    pt1, pt2 = fit_line_least_squares(points)
    cv2.line(image, pt1, pt2, (0, 255, 0), 2)

# 查找轮廓
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 遍历轮廓
for contour in contours:
    # 计算最小外接旋转矩形
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    # 绘制旋转矩形
    cv2.drawContours(image, [box], 0, (0, 0, 255), 2)

# 显示结果
cv2.imshow('Center Line and Bounding Rectangles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
