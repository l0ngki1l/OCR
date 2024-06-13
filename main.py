import cv2
import easyocr
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt

reader = easyocr.Reader(['ch_sim'])
image_path = 'test.png'
image = cv2.imread(image_path)
results = reader.readtext(image_path)

# 使用Pillow创建一个图像和绘图对象
pillow_image = Image.open(image_path)
draw = ImageDraw.Draw(pillow_image)

# 指定中文字体路径和大小
font_path = 'SimKai.ttf'
font_size = 20
font = ImageFont.truetype(font_path, font_size)

for (bbox, text, prob) in results:
    if prob >= 0.5:  # 只处理概率大于等于0.5的结果
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))

        # 使用Pillow绘制中文文本
        draw.text((top_left[0], top_left[1] - 20), text, font=font, fill=(255, 0, 0))

        # 将Pillow图像转换为OpenCV图像
        cv_image = np.array(pillow_image)
        cv_image = cv_image[:, :, ::-1].copy()  # 转换颜色通道

        # 使用OpenCV绘制边界框
        cv2.rectangle(cv_image, top_left, bottom_right, (0, 0, 255), 2)

# 使用matplotlib显示图像
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()