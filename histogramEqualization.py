import cv2
import numpy as np
from matplotlib import pyplot as plt


# 定义一个函数，用于对彩色图像进行直方图均衡化，并输出均衡化后的直方图
def histogram_equalization(file_name):
    try:
        # 读取图像文件
        image = cv2.imread(file_name)  # 以彩色模式读取图像

        # 检查图像是否成功加载
        if image is None:
            raise FileNotFoundError("无法加载图像，请检查文件路径。")

        # 分离图像的颜色通道
        b, g, r = cv2.split(image)

        # 对每个通道进行直方图均衡化
        b_eq = cv2.equalizeHist(b)
        g_eq = cv2.equalizeHist(g)
        r_eq = cv2.equalizeHist(r)

        # 合并均衡化后的通道
        equalized_image = cv2.merge((b_eq, g_eq, r_eq))

        # 计算原始图像的直方图
        hist_b, bins_b = np.histogram(b.flatten(), 256, [0, 255])
        hist_g, bins_g = np.histogram(g.flatten(), 256, [0, 255])
        hist_r, bins_r = np.histogram(r.flatten(), 256, [0, 255])

        # 计算均衡化后图像的直方图
        hist_b_eq, bins_b_eq = np.histogram(b_eq.flatten(), 256, [0, 255])
        hist_g_eq, bins_g_eq = np.histogram(g_eq.flatten(), 256, [0, 255])
        hist_r_eq, bins_r_eq = np.histogram(r_eq.flatten(), 256, [0, 255])

        # 绘制原始图像的直方图
        plt.figure()
        plt.title(file_name.rsplit('.', 1)[0].split('/')[-1] + "_originalHistogram." + file_name.rsplit('.', 1)[1])
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Number of Pixels")
        plt.plot(bins_b[0:-1], hist_b, color='b', label='Blue')
        plt.plot(bins_g[0:-1], hist_g, color='g', label='Green')
        plt.plot(bins_r[0:-1], hist_r, color='r', label='Red')
        plt.legend()

        # 保存原始直方图图像
        plt.savefig(file_name.rsplit('.', 1)[0] + '_originalHistogram.' + file_name.rsplit('.', 1)[1])
        plt.show()
        plt.close()

        # 绘制均衡化后图像的直方图
        plt.figure()
        plt.title(file_name.rsplit('.', 1)[0].split('/')[-1] + "_equalizedHistogram." + file_name.rsplit('.', 1)[1])
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Number of Pixels")
        plt.plot(bins_b_eq[0:-1], hist_b_eq, color='b', label='Blue')
        plt.plot(bins_g_eq[0:-1], hist_g_eq, color='g', label='Green')
        plt.plot(bins_r_eq[0:-1], hist_r_eq, color='r', label='Red')
        plt.legend()

        # 保存直方图图像
        plt.savefig(file_name.rsplit('.', 1)[0] + '_equalizedHistogram.' + file_name.rsplit('.', 1)[1])
        plt.show()
        plt.close()

        # 显示均衡化后的图像
        plt.figure()
        plt.title(file_name.rsplit('.', 1)[0].split('/')[-1] + "_equalized." + file_name.rsplit('.', 1)[1])
        plt.imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB))  # 转换颜色空间以正确显示
        plt.show()

        # 保存均衡化后的图像
        output_file_name = file_name.rsplit('.', 1)[0] + '_equalized.' + file_name.rsplit('.', 1)[1]
        cv2.imwrite(output_file_name, equalized_image)
        print(f"均衡化后的图像已保存为：{output_file_name}")

    except FileNotFoundError as e:
        # 如果文件没有找到，打印错误信息
        print(e)
    except Exception as e:
        # 如果发生其他错误，打印错误信息
        print(f"处理文件时发生错误：{e}")

# 示例用法
# 假设用户输入的文件名是'image.jpg'
# histogram_equalization_color('path/to/your/image.jpg')
