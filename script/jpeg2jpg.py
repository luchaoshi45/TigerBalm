import os
from PIL import Image

def convert_folder_to_jpg(input_folder, output_folder, quality=95):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        # 检查文件是否为JPEG图像
        if filename.endswith(".jpeg") or filename.endswith(".jpeg"):
            # 构建输入和输出文件的路径
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename[:-4]+'jpg')
            # 调用转换函数
            convert_to_jpg(input_image_path, output_image_path, quality)

def convert_to_jpg(input_image_path, output_image_path, quality=95):
    # 打开图像文件
    image = Image.open(input_image_path)
    # 保存为JPEG格式并指定质量
    image.save(output_image_path, 'JPEG', quality=quality)
    print(f"{input_image_path} 转换为 {output_image_path} 成功！")

# 示例用法
if __name__ == "__main__":
    input_folder = "lable-1-400"  # 输入文件夹路径
    output_folder = "lable-1-400"  # 输出文件夹路径
    # 调用函数进行转换
    convert_folder_to_jpg(input_folder, output_folder)
