# 타임랩스 동영상 만들기
# 타임랩스 : 일정 간격으로 1 프레임씩 이미지를 추출하여 이어붙여 만든 동영상 -> 분석 시간을 줄여줌

import cv2

print("타입랩스 시작")
# 동영상 불러오기
mov01 = cv2.VideoCapture("mov/mov01.avi") # 동영상 불러오기
mov01_width = mov01.get(cv2.CAP_PROP_FRAME_WIDTH) # 동영상의 가로 크기 정보 볼러오기
mov01_height = mov01.get(cv2.CAP_PROP_FRAME_HEIGHT) # 동영상의 세로 크기 정보 볼러오기
mov01_fps = mov01.get(cv2.CAP_PROP_FPS) # 동영상의 프레임 정보 불러오기(fps : 초당 프레임수)
mov01_framecount = mov01.get(cv2.CAP_PROP_FRAME_COUNT) # 동영상의 총 프레임 수

# hog 모델 선언
hog = cv2.HOGDescriptor()  # HOG 객체 만들기
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())  # 사람 인식하는 사람모델 인수 지정하기

# Timelaps 생성
movie_name = "timelapse.avi"
fourcc = cv2.VideoWriter_fourcc("X","V","I","D")  # xvid 코덱 설정
video = cv2.VideoWriter(movie_name, fourcc, 30, (int(mov01_width), int(mov01_height)))

num = 0

while(mov01.isOpened()):
    ret, frame = mov01.read()
    if ret == True:
        if num % 10 == 0: # 0, 10, 20, 30.... 400
            grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            human, r = hog.detectMultiScale(grey)
            if len(human) > 0:
                for (x,y,w,h) in human:
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)

            video.write(frame)
    else:
        break

    num = num + 1

video.release()
mov01.release()
cv2.destroyAllWindows()

print("타입랩스 끝")