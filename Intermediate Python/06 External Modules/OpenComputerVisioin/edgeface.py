import cv2 as cv

capture = cv.VideoCapture('face.mp4')


while True:
 ret, frame = capture.read()

 frame = cv.resize(frame, (int(frame.shape[1]*0.5),int(frame.shape[0]*0.5)), cv.INTER_CUBIC)

 blurred_frame = cv.GaussianBlur(frame, (3,3), cv.BORDER_DEFAULT)
 canny_frame = cv.Canny(blurred_frame, 125, 200)

 cv.imshow('video', frame)
 cv.imshow('canny video', canny_frame)

 if cv.waitKey(20) & 0xFF == ord('q'):
  break

capture.release()
cv.destroyAllWindows()