# 이미지 속에서 사람 찾기

import cv2

hog = cv2.HOGDescriptor()  # HOG 객체 만들기
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())  # 사람 인식하는 사람모델 인수 지정하기

img01 = cv2.imread("img/img01.jpg")  # 샘플 이미지 img01 불러오기
img01_gray = cv2.cvtColor(img01, cv2.COLOR_BGR2GRAY)  # 이미지를 흑백사진으로 변환

human, r = hog.detectMultiScale(img01_gray)  # 검출된 사람의 위치정보 human

if len(human) > 0: # human 길이->사람의 수->사람의 수가 1명 이상이면 이미지에서 검출된 사람에게 사각형 표시
    for (x,y,w,h) in human:
        cv2.rectangle(img01, (x,y),(x+w,y+h),(255,255,255),3)

cv2.namedWindow("human search", cv2.WINDOW_NORMAL)
cv2.imshow("human search", img01)
cv2.imwrite("img/human_search.jpg", img01)
cv2.waitKey(0)
cv2.destroyAllWindows()