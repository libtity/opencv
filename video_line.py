import cv2
import public as pb
import numpy as np

if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    while True:
        # 读取原始图像
        ret, img = cap.read()

        # 转换为灰度图
        # 高斯滤波图像
        # 边缘提取图像
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur_img = cv2.GaussianBlur(img_gray, (5, 5), 0)
        edges_blur = cv2.Canny(blur_img, 300, 400)

        cv2.imshow("image", edges_blur)

        lines = cv2.HoughLinesP(edges_blur, 1, np.pi / 180, 100, minLineLength=10, maxLineGap=10)
        if lines is None:
            print("wrong mei jian ce dao")
            continue

        for line in lines:
            x1, y1, x2, y2 = line[0]
            k = (y1 - y2) / (x1 - x2)
            if k < 3 / 2 and k > 1 / 2:
                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

            cv2.imshow("res", img)

        pb.delay_key(100)

    cv2.destroyAllWindows()
