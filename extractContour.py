import cv2
import numpy as np


# 定义一个函数，利用canny边缘检测器提取图像的轮廓
def extract_contours_canny(file_name):
    """
    从指定的图像文件中提取轮廓，并在原始图像上绘制这些轮廓。

    参数:
    file_name (str): 图像文件的路径。
    """
    try:
        # 读取图像文件
        image = cv2.imread(file_name)

        # 将图像转换为灰度图，因为轮廓检测通常在灰度图上进行
        # cv2.COLOR_BGR2GRAY指将图像从BGR颜色空间转换为灰度颜色空间
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 应用高斯模糊，减少图像噪声
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # 使用Canny边缘检测器检测边缘
        # 50为低阈值，用于确定弱边缘，低于该值的像素被丢弃；150为高阈值，用于确定强边缘，高于该值的像素被丢弃
        # edges为用于轮廓检测的二值图像，其中边缘像素被标记为白色（255），非边缘像素被标记为黑色（0）
        edges = cv2.Canny(blurred, 50, 150)

        # 查找边缘的轮廓坐标
        # cv2.RETR_EXTERNAL指定只检索最外层的轮廓，忽略轮廓之间的层次结构
        # cv2.CHAIN_APPROX_SIMPLE代表只保留轮廓的拐点信息，从而减少轮廓数据的大小
        contours = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        # 在原始图像上绘制轮廓
        # -1代表绘制所有轮廓坐标；(0, 255, 0)代表用绿色的线条绘制轮廓；2代表轮廓线厚度
        contour_image = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)

        # 显示带有轮廓的图像
        # 'Contours'代表创建的窗口标题
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
        # cv2.COLOR_BGR2GRAY指将图像从BGR颜色空间转换为灰度颜色空间
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 使用Sobel算子计算图像的x和y方向梯度
        # cv2.CV_64F指定输出图像的像素值类型为64位浮点数，利于梯度计算
        # ksize代表Sobel算子的大小
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

        # 计算梯度的幅度
        magnitude = np.sqrt(sobelx ** 2 + sobely ** 2)

        # 将梯度幅度转换为8位无符号整数，即0到255
        magnitude = np.uint8(magnitude)

        # 使用阈值来确定边缘
        # 50代表阈值，即梯度幅度低于该值的像素值不是边缘；255代表高于高于阈值的像素值将被设置为这个值
        # cv2.THRESH_BINARY代表对阈值二值化处理，高于阈值的像素值被设置为255，否则为0
        thresh = cv2.threshold(magnitude, 50, 255, cv2.THRESH_BINARY)[1]

        # 查找阈值图像的轮廓
        # cv2.RETR_EXTERNAL指定只检索最外层的轮廓，忽略轮廓之间的层次结构
        # cv2.CHAIN_APPROX_SIMPLE代表只保留轮廓的拐点信息，从而减少轮廓数据的大小
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        # 在原始图像上绘制轮廓
        # -1代表绘制所有轮廓坐标；(0, 255, 0)代表用绿色的线条绘制轮廓；2代表轮廓线厚度
        contour_image = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)

        # 显示带有轮廓的图像
        # 'Contours'代表创建的窗口标题
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