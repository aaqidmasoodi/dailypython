import cv2 as cv

capture = cv.VideoCapture(0)


while True:
  ret, frame = capture.read()

  cv.imshow('video', frame)
 

#  # Every 1 millisecond i am checking whether i am pressing q
  if cv.waitKey(20) & 0xFF == ord('q'):
    break

capture.release()
cv.destroyAllWindows()




