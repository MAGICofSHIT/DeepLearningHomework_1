from PIL import Image


# 定义一个函数，用于按照给定的比例缩放图像的宽度和高度
def resize_image(file_name, scale_width, scale_height):
    """
    按照给定的比例缩放图像的宽度和高度。

    参数:
    file_name (str): 图像文件的路径。
    scale_width (float): 宽度的缩放比例，例如0.5表示宽度减半。
    scale_height (float): 高度的缩放比例，例如0.5表示高度减半。
    """
    try:
        # 打开图像文件
        with Image.open(file_name) as img:
            # 获取原始图像的宽度和高度
            original_width, original_height = img.size

            # 计算新的宽度和高度
            new_width = int(original_width * scale_width)
            new_height = int(original_height * scale_height)

            # 使用Image模块的resize方法缩放图像
            # Image.Resampling.LANCZOS是高质量的重采样滤波器，用于缩放
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # 显示缩放后的图像
            resized_img.show()

            # 保存缩放后的图像，这里使用原文件名加上"_resized"后缀
            resized_img.save(file_name.rsplit('.', 1)[0] + '_resized.' + file_name.rsplit('.', 1)[1])
            print(f"缩放后的图像已保存为：{file_name.rsplit('.', 1)[0] + '_resized.' + file_name.rsplit('.', 1)[1]}")

    except FileNotFoundError:
        # 如果文件没有找到，打印错误信息
        print(f"错误：文件'{file_name}'未找到，请检查路径是否正确。")
    except Exception as e:
        # 如果发生其他错误，打印错误信息
        print(f"处理文件时发生错误：{e}")

# 示例用法
# 假设用户输入的文件名是'image.jpg'，宽度缩放比例是0.5，高度缩放比例是0.5
# resize_image('path/to/your/image.jpg', 0.5, 0.5)