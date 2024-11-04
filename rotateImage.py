from PIL import Image


# 定义一个函数，用于旋转图像
def rotate_image(file_name, degrees):
    """
    旋转图像文件指定的角度。

    参数:
    file_name (str): 图像文件的路径。
    degrees (int): 旋转的角度，正值表示逆时针旋转，负值表示顺时针旋转。
    """
    try:
        # 打开图像文件
        with Image.open(file_name) as img:
            # 使用Image模块的rotate方法旋转图像
            # expand=True表示调整图像大小以适应旋转后的内容
            rotated_img = img.rotate(degrees, expand=True)

            # 显示旋转后的图像
            rotated_img.show()

            # 保存旋转后的图像，这里使用原文件名加上"_rotated"后缀
            rotated_img.save(file_name.rsplit('.', 1)[0] + '_rotated.' + file_name.rsplit('.', 1)[1])
            print(f"旋转后的图像已保存为：{file_name.rsplit('.', 1)[0] + '_rotated.' + file_name.rsplit('.', 1)[1]}")

    except FileNotFoundError:
        # 如果文件没有找到，打印错误信息
        print(f"错误：文件'{file_name}'未找到，请检查路径是否正确。")
    except Exception as e:
        # 如果发生其他错误，打印错误信息
        print(f"处理文件时发生错误：{e}")

# 示例用法
# 假设用户输入的文件名是'image.jpg'，旋转角度是90度
# rotate_image('path/to/your/image.jpg', 90)
