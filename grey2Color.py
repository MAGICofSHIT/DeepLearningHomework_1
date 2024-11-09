from PIL import Image


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

                    # 灰度映射，将亮度低的映射为蓝色(冷色)，亮度高的映射为红色（暖色）
                    # 输入灰度级        输出彩色
                    # 0～63  1/4         蓝色
                    # 64～127 2/4        紫色
                    # 128～191 3/4       黄色
                    # 192～255  4/4      红色
                    if grayscale_pixel <= 63:
                        red = 0
                        green = grayscale_pixel * 4
                        blue = 255
                    elif grayscale_pixel <= 127:
                        red = 0
                        green = 255
                        blue = -4 * grayscale_pixel + 2 * 255
                    elif grayscale_pixel <= 191:
                        red = 4 * grayscale_pixel - 2 * 255
                        green = 255
                        blue = 0
                    else:
                        red = 255
                        green = 4 * (255 - grayscale_pixel)
                        blue = 0

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
