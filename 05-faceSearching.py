# 이미지 속의 사람 얼굴 검출하기

import cv2


# https://github.com/oreillymedia/Learning-OpenCV-3_examples/blob/master/haarcascade_frontalface_alt.xml
# opencv 관련.
cascade_file = "haarcascade_frontalface_alt.xml"  # 앞을 보는 얼굴 찾기 모델 소스
cascade = cv2.CascadeClassifier(cascade_file)  # 정면을 보는 얼굴 검출 모델.

# img02 = cv2.imread("img/img02.jpg") # 이미지 불러오기
# img02_grey = cv2.cvtColor(img02, cv2.COLOR_BGR2GRAY)  # 흑백이미지로 변경
face = cv2.imread("img/face.png") # 이미지 불러오기
face_grey = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # 흑백이미지로 변경

face_info = cascade.detectMultiScale(face_grey, minSize=(50,50))  # 얼굴 검출->얼굴의 위치 정보를 반환
# print(face_info)

for (x, y, w, h) in face_info:
    cv2.rectangle(face, (x,y), (x+w, y+h), (0, 0, 255), 2) # rgb 위치가 다름 (b,g,r)

cv2.namedWindow("face search2", cv2.WINDOW_NORMAL)
cv2.imshow("face search2", face)
cv2.imwrite("img/face_search2.jpg", face)
cv2.waitKey(0)
cv2.destroyAllWindows()