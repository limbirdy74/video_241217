import cv2

mov01 = cv2.VideoCapture("mov/mov01.avi") # 동영상 불러오기

imageNum = 0
while(mov01.isOpened()):

    ret, frame = mov01.read() # mov01 에 저장된 동영상을 프레임 단위로 처리하여 불러오기
    #  ret -> 동영상을 잘 불러왔는지 체크하는 bool 타입 변수-> 동영상을 불러왔을 때 에러가 없으면 True
    if ret == True:  # 참이면 동영상이 잘 로드된 경우
        cv2.imshow("mov01 frame", frame)
        filepath = f"snapshot/snapsot_{imageNum}.jpg"  # 이미지가 저장될 경로 지정
        cv2.imwrite(filepath, frame)
        if cv2.waitKey(1) & 0xFF == ord("q"): # 키보드 q 가 클릭되면 종료
            break
    imageNum = imageNum + 1

mov01.release()
cv2.destroyAllWindows() # 창 닫기