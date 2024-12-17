# 동영상 불러오기

import cv2

mov01 = cv2.VideoCapture("mov/mov01.avi") # 동영상 불러오기
mov01_width = mov01.get(cv2.CAP_PROP_FRAME_WIDTH) # 동영상의 가로 크기 정보 볼러오기
mov01_height = mov01.get(cv2.CAP_PROP_FRAME_HEIGHT) # 동영상의 세로 크기 정보 볼러오기
mov01_fps = mov01.get(cv2.CAP_PROP_FPS) # 동영상의 프레임 정보 불러오기(fps : 초당 프레임수)
mov01_framecount = mov01.get(cv2.CAP_PROP_FRAME_COUNT) # 동영상의 총 프레임 수

print(f"동영상의 가로 크기 : {mov01_width}")
print(f"동영상의 세로 크기 : {mov01_height}")
print(f"동영상의 초당 프레임수 : {mov01_fps}")
print(f"동영상의 총 프레임수 : {mov01_framecount}")

while(mov01.isOpened()):
    ret, frame = mov01.read() # mov01 에 저장된 동영상을 프레임 단위로 처리하여 불러오기
    #  ret -> 동영상을 잘 불러왔는지 체크하는 bool 타입 변수-> 동영상을 불러왔을 때 에러가 없으면 True
    if ret == True:  # 참이면 동영상이 잘 로드된 경우
        cv2.imshow("mov01 frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): # 키보드 q 가 클릭되면 종료
        break

mov01.release()
cv2.destroyAllWindows() # 창 닫기