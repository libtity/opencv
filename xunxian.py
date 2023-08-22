# 对图片进行透视变换
import sys
import cv2
import numpy as np


def perspective_transform(img, src, dst):
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]), flags=cv2.INTER_LINEAR)
    return warped, M
    # 返回透视变换后的图片，和透视变换矩阱
    # warped, M = warp(img, src, dst)
    # return warped, M
    # cv2.imshow('img', img)
    # cv2.imshow('warped', warped)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # return warped, M
    # 返回透视变换后的图片，和透视变换矩阱
    # warped, M = warp(img, src, dst)
    # return warped, M
    # cv2.imshow('img', img)
    # cv2.imshow('warped', warped)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # return warped, M


# 对图片进行边缘检测
def canny_edge(img):
    # img = cv2.imread('gray_image/gray_158.jpg')
    edges = cv2.Canny(img, 50, 150, apertureSize=3)
    return edges


# 对图片进行二值化，使灰度低于150的点灰度为0
def binary_image(img):
    ret, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    return thresh


# 对图片进行霍夫直线变换
def hough_transform(img, img1):
    # img = cv2.imread('gray_image/gray_158.jpg')
    edges = cv2.Canny(img, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 180, threshold=100, minLineLength=20, maxLineGap=20)

    if lines is None:
        print("wrong")
        return img

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img1, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.imshow('img1',img1)
    return img


if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    while 1:
        ret, frame = cap.read()
        if ret == 0:
            print('wrong mei da kai')
            sys.exit(0)

        # 切片
        img = frame[:, 320:, :]
        img1 = img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img = binary_image(img)
        img = hough_transform(img, img1)

        cv2.imshow("img", img)

        if cv2.waitKey(100) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

# img=cv2.imread('gray_image/gray_{}.jpg'.format(i))
#  img=Image.open('gray_image/gray_{}.jpg'.format(i))
#  img=img.crop((320,0,640,480))
# print(img.shape)
# for i in range(0,640,40):
#     cv2.line(img, (i, 0), (i, 480), (0, 0, 255), 2)
# for i in range(0,480,40):
#     cv2.line(img, (0, i), (640, i), (0, 255, 0), 2)
# cv2.line(img, (320, 280), (520, 440), (255, 0, 0), 2)
# cv2.line(img, (0, 0), (640, 480), (255, 0, 0), 2)

# src = np.array([[0, 280], [220, 440], [320, 440], [120, 280]]).astype(np.float32)
# dst = np.array([[200, 0], [220, 480], [320, 480], [320, 0]]).astype(np.float32)
# img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
# img, M = perspective_transform(img, src, dst)
