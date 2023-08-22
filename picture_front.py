import cv2
import public as pb
import numpy as np

# if __name__ == '__main__':
#     for i in range(1, 91):
#         img = cv2.imread("front\image_{}.jpg".format(i))
#         cv2.imshow('w1', img)
#
#         # 转换为HSV图像并提取蓝色像素
#         img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#         low_blue = np.array([100,30,30])
#         high_blue = np.array([124,255,255])
#         img_blue = cv2.inRange(img_hsv,low_blue,high_blue)
#
#         cv2.imshow('b',img_blue)
#
#         cnt = 0
#
#         for i in img_blue:
#             if img_blue[0][i] == 255:
#                 cnt += 1
#
#
#         pb.delay_key(100)
#
#     cv2.destroyAllWindows()



if __name__ == '__main__':
    for i in range(1, 91):
        img = cv2.imread("front\image_{}.jpg".format(i))
        # cv2.imshow('w1', img)

        # 转换为HSV图像并提取蓝色像素
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        low_blue = np.array([100,65,0])
        high_blue = np.array([132,255,100])
        img_blue = cv2.inRange(img_hsv,low_blue,high_blue)

        # 边缘检测
        img_edge = cv2.Canny(img_blue,100,1000,apertureSize=3,L2gradient=True)

        res = np.hstack((img_blue,img_edge))
        cv2.imshow('b',res)

        # b,g,r = cv2.split(img)
        # zeros = np.zeros(img.shape[:2],dtype="uint8")
        #
        # img_blue = cv2.merge([b,zeros,zeros])
        #
        # cv2.imshow('w2', img_blue)

        pb.delay_key(100)

    cv2.destroyAllWindows()
