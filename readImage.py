# 导入Pillow库中的Image模块，用于图像处理
from PIL import Image

# 让用户输入文件名
file_name = input("请输入图像文件的完整路径：")

# 尝试打开图像文件
try:
    # 使用Image.open()函数打开图像
    with Image.open(file_name) as img:
        # 显示图像
        img.show()

        # 获取图像的大小（宽度和高度）
        width, height = img.size

        # 输出图像的大小信息
        print(f"图像大小：宽度 = {width}像素, 高度 = {height}像素")

except FileNotFoundError:
    # 如果文件没有找到，打印错误信息
    print(f"错误：文件'{file_name}'未找到，请检查路径是否正确。")
except Exception as e:
    # 如果发生其他错误，打印错误信息
    print(f"打开文件时发生错误：{e}")