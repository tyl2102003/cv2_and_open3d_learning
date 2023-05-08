import cv2
# 创建VideoWriter写多媒体文件
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('./cap_video.mp4', fourcc, 25, (1280, 720))
# 创建窗口

cv2.namedWindow('vd', flags=cv2.WINDOW_NORMAL)
cv2.resizeWindow('vd', 640, 480)
# 获取视频设备
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('vd', frame)
    # 写多媒体文件
    out.write(frame)
    key = cv2.waitKey(1)
    if key & 0xff == ord('q'):
        break

cap.release()
# 释放资源
out.release()
cv2.destroyAllWindows()
