# 导入cv2库
import cv2
import cv2 as cv
# 打开摄像头
cap = cv.VideoCapture(1)
count = 1

while (True):
    # 开始用摄像头读数据，返回hx为true则表示读成功，frame为读的图像
    hx, frame = cap.read()

    # 如果hx为Flase表示开启摄像头失败，那么就输出"read vido error"并退出程序
    if hx is False:
        # 打印报错
        print('read video error')
        # 退出程序
        exit(0)

    # 显示摄像头图像，其中的video为窗口名称，frame为图像
    cv.imshow('video', frame)

    # 监测键盘输入是否为q，为q则退出程序
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("./back/image_{}.jpg".format(count),frame)
        print("ok {}".format(count))
        count = count + 1


# 释放摄像头
cap.release()

# 结束所有窗口
cv.destroyAllWindows() 
