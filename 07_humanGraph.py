# 사람 인식 시각화하기

import cv2
import pandas as pd
import matplotlib.pyplot as plt

print("분석 생성 시작!")
# 동영상 불러오기
mov01 = cv2.VideoCapture("mov/mov01.avi")  # 동영상 불러오기
mov01_width = mov01.get(cv2.CAP_PROP_FRAME_WIDTH)  # 동영상의 가로 크기 정보 불러오기
mov01_height = mov01.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 동영상의 세로 크기 정보 불러오기
mov01_fps = mov01.get(cv2.CAP_PROP_FPS)  # 동영상의 프레임 정보 불러오기(FPS:초당 프레임 수)
mov01_framecount = mov01.get(cv2.CAP_PROP_FRAME_COUNT)  # 총 프레임 수 불러오기

# hog 모델 선언
hog = cv2.HOGDescriptor()  # HOG 객체 만들기
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())  # 사람 인식하는 사람모델 인수 지정하기

# Timelapse 생성
movie_name = "timelapse.avi"
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')  # xvid 코덱 설정
video = cv2.VideoWriter(movie_name, fourcc, 30, (int(mov01_width), int(mov01_height)))

num = 0

list_df01 = []
list_df02 = []

while(mov01.isOpened()):
    ret, frame = mov01.read()
    if ret == True:
        if num % 10 == 0:  # 0, 10, 20, 30, 40, 50 .... 400
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            human, r = hog.detectMultiScale(gray)
            if len(human) >0:
                for (x, y, w, h) in human:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)
            tmp_se = pd.Series([num/mov01_fps, len(human)])

            list_df01.append(tmp_se[0])  # 시간
            list_df02.append(tmp_se[1])  # 사람 수

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else:
        break
    num = num + 1

data_df = pd.DataFrame({"time":list_df01, "people":list_df02})
# print(data_df)

video.release()
mov01.release()
cv2.destroyAllWindows()
print("분석 완료!")

plt.plot(data_df["time"], data_df["people"])
plt.xlabel("time(sec)")
plt.ylabel("population")
plt.ylim(0,25)
plt.show()

