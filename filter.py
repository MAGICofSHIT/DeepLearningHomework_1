import cv2


# 定义一个函数，用于对图像进行均值滤波
def mean_filter(file_name, m, n):
    """
    对指定的图像文件进行均值滤波。

    参数:
    file_name (str): 图像文件的路径。
    m, n：滤波器大小
    """
    try:
        # 读取图像文件
        image = cv2.imread(file_name)

        # 检查图像是否成功加载
        if image is None:
            raise FileNotFoundError("无法加载图像，请检查文件路径。")

        # 对图像进行均值滤波
        # cv2.blur函数进行均值滤波，(m, n)是滤波器的大小
        filtered_image = cv2.blur(image, (m, n))

        # 显示滤波后的图像
        cv2.imshow('Filtered Image', filtered_image)

        # 等待用户按键，再关闭所有窗口
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # 保存滤波后的图像
        output_file_name = file_name.rsplit('.', 1)[0] + '_meanFiltered.' + file_name.rsplit('.', 1)[1]
        cv2.imwrite(output_file_name, filtered_image)
        print(f"滤波后的图像已保存为：{output_file_name}")

    except FileNotFoundError as e:
        # 如果文件没有找到，打印错误信息
        print(e)
    except Exception as e:
        # 如果发生其他错误，打印错误信息
        print(f"处理文件时发生错误：{e}")


# 示例用法
# 假设用户输入的文件名是'image.jpg'
# mean_filter('path/to/your/image.jpg')


# 定义一个函数，用于对图像进行高斯滤波
def gaussian_filter(file_name, m, n, sigma):
    """
    对指定的图像文件进行高斯滤波。

    参数:
    file_name (str): 图像文件的路径。
    m, n：滤波器大小
    sigma：高斯滤波器标准差
    """
    try:
        # 读取图像文件
        image = cv2.imread(file_name)

        # 检查图像是否成功加载
        if image is None:
            raise FileNotFoundError("无法加载图像，请检查文件路径。")

        # 对图像进行高斯滤波
        # cv2.GaussianBlur函数进行高斯滤波，(m, n)是滤波器的大小，0是标准差CV_DEFAULT(0)，即自动计算
        filtered_image = cv2.GaussianBlur(image, (m, n), sigma)

        # 显示滤波后的图像
        cv2.imshow('Filtered Image', filtered_image)

        # 等待用户按键，再关闭所有窗口
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # 保存滤波后的图像
        output_file_name = file_name.rsplit('.', 1)[0] + '_gaussianFiltered.' + file_name.rsplit('.', 1)[1]
        cv2.imwrite(output_file_name, filtered_image)
        print(f"滤波后的图像已保存为：{output_file_name}")

    except FileNotFoundError as e:
        # 如果文件没有找到，打印错误信息
        print(e)
    except Exception as e:
        # 如果发生其他错误，打印错误信息
        print(f"处理文件时发生错误：{e}")

# 示例用法
# 假设用户输入的文件名是'image.jpg'
# gaussian_filter('path/to/your/image.jpg')
