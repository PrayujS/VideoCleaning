import cv2

vidcap = cv2.VideoCapture('TrimmedVideo.mp4')
success, image = vidcap.read()

cv2.imwrite("frame.jpg", image)  # save frame as JPEG file

vidcap.release()
cv2.destroyAllWindows()