import cv2 as cv

capture = cv.VideoCapture('cat_video.mp4')


while True:
  ret, frame = capture.read()

  cv.imshow('video', frame)
 

#  # Every 1 millisecond i am checking whether i am pressing q
  if cv.waitKey(1) & 0xFF == ord('q'):
    break

capture.release()
cv.destroyAllWindows()




