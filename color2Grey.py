from PIL import Image


# 定义一个函数，用于将图像转换为灰度图
def color2grey(file_name):
    """
    将指定的图像文件转换为灰度图。

    参数:
    file_name (str): 图像文件的路径。
    """
    try:
        # 打开图像文件
        with Image.open(file_name) as img:
            # 使用Image模块的convert方法将图像转换为灰度图
            # "L"模式表示灰度模式
            grayscale_img = img.convert('L')

            # 显示灰度图
            grayscale_img.show()

            # 保存灰度图，这里使用原文件名加上"_grayscale"后缀
            grayscale_img.save(file_name.rsplit('.', 1)[0] + '_gray.' + file_name.rsplit('.', 1)[1])
            print(f"灰度图已保存为：{file_name.rsplit('.', 1)[0] + '_gray.' + file_name.rsplit('.', 1)[1]}")

    except FileNotFoundError:
        # 如果文件没有找到，打印错误信息
        print(f"错误：文件'{file_name}'未找到，请检查路径是否正确。")
    except Exception as e:
        # 如果发生其他错误，打印错误信息
        print(f"处理文件时发生错误：{e}")

# 示例用法
# 假设用户输入的文件名是'image.jpg'
# color2grey('path/to/your/image.jpg')