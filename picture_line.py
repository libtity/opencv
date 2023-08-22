import cv2
import sys
import numpy as np


def delay_key(i):
    key = cv2.waitKey(i)
    if key == ord('q'):
        cv2.destroyAllWindows()
        sys.exit(0)
    elif key == ord('p'):
        key = cv2.waitKey(0)
        while key != ord('c'):
            if key == ord('q'):
                cv2.destroyAllWindows()
                sys.exit(0)


if __name__ == '__main__':
    for i in range(50, 201):
        # 读取原始图像
        # 转换为灰度图
        # 高斯滤波图像
        # 边缘提取图像
        img = cv2.imread('image\image_{}.jpg'.format(i))
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur_img = cv2.GaussianBlur(img_gray, (5, 5), 0)

        cv2.imshow('g',blur_img)

        edges_blur = cv2.Canny(blur_img, 300, 400)

        cv2.imshow("image", edges_blur)

        lines = cv2.HoughLinesP(edges_blur, 1, np.pi / 180, 100, minLineLength=10, maxLineGap=20)
        if lines is None:
            print("wrong mei jian ce dao")
            continue

        for line in lines:
            x1, y1, x2, y2 = line[0]
            k = (y1 - y2) / (x1 - x2)
            if k < 3 / 2 and k > 1 / 2:
                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

            cv2.imshow("res", img)

        delay_key(100)

    cv2.destroyAllWindows()
