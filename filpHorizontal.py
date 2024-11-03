from PIL import Image


# 定义一个函数，用于将图像水平反转
def flip_image_horizontal(file_name):
    """
    将指定的图像文件水平反转。

    参数:
    file_name (str): 图像文件的路径。
    """
    try:
        # 打开图像文件
        with Image.open(file_name) as img:
            # 使用Image模块的transpose方法水平反转图像
            # Image.FLIP_LEFT_RIGHT是指定水平反转的选项
            flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

            # 显示水平反转后的图像
            flipped_img.show()

            # 保存水平反转后的图像，这里使用原文件名加上"_horizontallyFlipped"后缀
            flipped_file_name = file_name.rsplit('.', 1)[0] + '_horizontallyFlipped.' + file_name.rsplit('.', 1)[1]
            flipped_img.save(flipped_file_name)
            print(f"水平反转后的图像已保存为：{flipped_file_name}")

    except FileNotFoundError:
        # 如果文件没有找到，打印错误信息
        print(f"错误：文件'{file_name}'未找到，请检查路径是否正确。")
    except Exception as e:
        # 如果发生其他错误，打印错误信息
        print(f"处理文件时发生错误：{e}")

# 示例用法
# 假设用户输入的文件名是'image.jpg'
# flip_image_horizontally('path/to/your/image.jpg')