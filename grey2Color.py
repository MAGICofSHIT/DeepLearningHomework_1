from PIL import Image
import math


# 定义一个函数，用于将灰度图转换为RGB类型的伪彩图像
def grey2color(file_name):
    """
    将指定的灰度图像文件转换为RGB类型的伪彩图像。
    伪彩图像将使用蓝色和红色通道来表示灰度值，而绿色通道保持不变。

    参数:
    file_name (str): 灰度图像文件的路径。
    """
    try:
        # 打开灰度图像文件
        with Image.open(file_name) as img:
            # 获取图像的宽度和高度
            width, height = img.size

            # 创建一个新的RGB图像
            rgb_img = Image.new('RGB', (width, height))

            # 遍历图像的每个像素
            for x in range(width):
                for y in range(height):
                    # 获取灰度图像中当前像素的灰度值
                    grayscale_pixel = img.getpixel((x, y))

                    # 将灰度值映射到蓝色和红色通道
                    # 灰度值越小，蓝色成分越多；灰度值越大，红色成分越多
                    blue = int(255 * (1 - grayscale_pixel / 255))  # 灰度值越小，蓝色越亮
                    red = int(255 * (grayscale_pixel / 255))  # 灰度值越大，红色越亮
                    green = grayscale_pixel  # 绿色通道保持灰度值

                    # 将映射后的RGB值赋给当前像素
                    rgb_img.putpixel((x, y), (red, green, blue))

            # 显示伪彩图像
            rgb_img.show()

            # 保存伪彩图像，这里使用原文件名加上"_colorized"后缀
            colorized_file_name = file_name.rsplit('.', 1)[0] + '_colorized.' + file_name.rsplit('.', 1)[1]
            rgb_img.save(colorized_file_name)
            print(f"伪彩图像已保存为：{colorized_file_name}")

    except FileNotFoundError:
        # 如果文件没有找到，打印错误信息
        print(f"错误：文件'{file_name}'未找到，请检查路径是否正确。")
    except Exception as e:
        # 如果发生其他错误，打印错误信息
        print(f"处理文件时发生错误：{e}")

# 示例用法
# 假设用户输入的文件名是'image_grayscale.jpg'
# grey2color('path/to/your/image_grayscale.jpg')