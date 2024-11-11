import cv2
import numpy as np


# 定义一个函数，利用canny边缘检测器提取图像的轮廓
def extract_contours_canny(file_name):
    try:
        # 读取图像文件
        image = cv2.imread(file_name)

        # 将图像转换为灰度图，因为轮廓检测通常在灰度图上进行
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 应用高斯模糊，减少图像噪声
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # 使用Canny边缘检测器检测边缘
        edges = cv2.Canny(blurred, 50, 150)

        # 查找边缘的轮廓
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 在原始图像上z绘制轮廓
        contour_image = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)

        # 显示带有轮廓的图像
        cv2.imshow('Contours', contour_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # 保存带有轮廓的图像
        output_file_name = file_name.rsplit('.', 1)[0] + '_cannyContours.' + file_name.rsplit('.', 1)[1]
        cv2.imwrite(output_file_name, contour_image)
        print(f"图像已保存为：{output_file_name}")

    except FileNotFoundError:
        # 如果文件没有找到，打印错误信息
        print(f"错误：文件'{file_name}'未找到，请检查路径是否正确。")
    except Exception as e:
        # 如果发生其他错误，打印错误信息
        print(f"处理文件时发生错误：{e}")

# 示例用法
# 假设用户输入的文件名是'image.jpg'
# extract_contours('path/to/your/image.jpg')

# 定义一个函数，用于使用Sobel算子提取图像的轮廓
def extract_contours_sobel(file_name):
    """
    从指定的图像文件中使用Sobel算子提取轮廓，并在原始图像上绘制这些轮廓。

    参数:
    file_name (str): 图像文件的路径。
    """
    try:
        # 读取图像文件
        image = cv2.imread(file_name)

        # 将图像转换为灰度图，因为轮廓检测通常在灰度图上进行
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 使用Sobel算子计算图像的x和y方向梯度
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

        # 计算梯度的幅度
        magnitude = np.sqrt(sobelx ** 2 + sobely ** 2)

        # 将梯度幅度转换为8位图像
        magnitude = np.uint8(magnitude)

        # 使用阈值来确定边缘
        ret, thresh = cv2.threshold(magnitude, 50, 255, cv2.THRESH_BINARY)

        # 查找阈值图像的轮廓
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 在原始图像上绘制轮廓
        contour_image = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)

        # 显示带有轮廓的图像
        cv2.imshow('Contours', contour_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # 保存带有轮廓的图像
        output_file_name = file_name.rsplit('.', 1)[0] + '_sobelContours.' + file_name.rsplit('.', 1)[1]
        cv2.imwrite(output_file_name, contour_image)
        print(f"图像已保存为：{output_file_name}")

    except FileNotFoundError:
        # 如果文件没有找到，打印错误信息
        print(f"错误：文件'{file_name}'未找到，请检查路径是否正确。")
    except Exception as e:
        # 如果发生其他错误，打印错误信息
        print(f"处理文件时发生错误：{e}")

# 示例用法
# 假设用户输入的文件名是'image.jpg'
# extract_contours_sobel('path/to/your/image.jpg')