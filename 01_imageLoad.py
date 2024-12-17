# 이미지 불러오기

import cv2  # pip install opencv-python : 이미지 및 동영상 분석 라이브러리

img01 = cv2.imread("img/img01.jpg")  # 이미지를 img1에 저장
# print(img01.shape[0:2])  # 튜플로 반환(세로, 가로)

height, width = img01.shape[0:2]  # img01 이미지에 포함된 가로, 세로 이미지 정보를 추출

print(f"img01 이미지의 가로 크기 : {width}")
print(f"img01 이미지의 세로 크기 : {height}")

cv2.namedWindow("Sample Image", cv2.WINDOW_NORMAL)
cv2.imshow("Sample Image", img01)  # 이미지를 출력
cv2.waitKey(0)  # 이미지 표시시간(밀리세컨드)->0으로 지정하면 윈도우를 닫을 때까지 멈춰있게 됨
cv2.destroyAllWindows()  # 윈도우 닫기