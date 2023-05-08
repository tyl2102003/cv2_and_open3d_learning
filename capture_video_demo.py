""" 从视频读取帧保存为图片"""
import cv2


# cap = cv2.VideoCapture("C:/Users/lenovo/Videos/1.mp4")#读取文件
cap = cv2.VideoCapture(0)  # 读取摄像头

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4v', fourcc, 20.0, (210, 240), 0)

while True:
    ret, frame = cap.read()
    # 下面三行可以根据自己的电脑进行调节
    src = cv2.resize(frame, (210, 200), interpolation=cv2.INTER_CUBIC)  # 窗口大小
    cv2.rectangle(src, (90, 60), (300, 300), (0, 255, 0))  # 框出截取位置
    roi = src[60:300, 90:300]  # 获取手势框图
    print(roi.shape)

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)  # 转化为灰度图片
    out.write(gray)
    cv2.imshow("2", gray)

    key = cv2.waitKey(50) & 0xFF
    if key == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

