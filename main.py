# 导入Pillow库中的Image模块，用于图像处理
from PIL import Image
from grey2Color import grey2color
from resizeImage import resize_image
from rotateImage import rotate_image
from color2Grey import color2grey
from filpHorizontal import flip_image_horizontal
from filpVertical import flip_image_vertical
from extractContour import extract_contours_canny, extract_contours_sobel
from histogramEqualization import histogram_equalization
from filter import mean_filter, gaussian_filter

# 让用户输入文件名
colorImagePath = "./Pictures/test.jpg"
greyImagePath = "./Pictures/test_gray.jpg"

# 均值滤波器参数
m_mean = 15
n_mean = 15

# 高斯滤波参数
m_gaussian = 15
n_gaussian = 15
sigma_gaussian = 0

if __name__ == '__main__':
    # 尝试打开图像文件
    try:
        # 使用Image.open()函数打开图像
        with Image.open(colorImagePath) as img:
            # 显示图像
            img.show()

            # 获取图像的大小（宽度和高度）
            width, height = img.size

            # 输出图像的大小信息
            print(f"图像大小：宽度 = {width}像素, 高度 = {height}像素")

            # 旋转图像
            rotate_image(colorImagePath, 45)

            # 缩放图像
            resize_image(colorImagePath, 0.5, 1.2)

            # 彩图转灰度图
            color2grey(colorImagePath)

            # 灰度图转伪彩图
            grey2color(greyImagePath)

            # 图像水平反转
            flip_image_horizontal(colorImagePath)

            # 图像垂直反转
            flip_image_vertical(colorImagePath)

            # 利用canny边缘检测器进行图像轮廓提取
            extract_contours_canny(colorImagePath)

            # 利用sobel算子进行图像轮廓提取
            extract_contours_sobel(colorImagePath)
    
            # 直方图均衡化
            histogram_equalization(colorImagePath)
    
            # 均值滤波
            mean_filter(colorImagePath, 15, 15)

            # 高斯滤波
            gaussian_filter(colorImagePath, 15, 15, 0)
    except FileNotFoundError:
        # 如果文件没有找到，打印错误信息
        print(f"错误：文件'{colorImagePath}'未找到，请检查路径是否正确。")
    except Exception as e:
        # 如果发生其他错误，打印错误信息
        print(f"打开文件时发生错误：{e}")