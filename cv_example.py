import cv2

#ziad asem 
#code for webcam and close it by pressing 'q'

capture = cv2.VideoCapture(0);  #open default webcam 
capture.set(3, 700) #set width of frame
capture.set(4, 700) #set hieght of frame
capture.set(5, 20) #set FPS
capture.set(10, 20) #set brightness

while 1 :
  1 , img =  capture.read();
  cv2.imshow("preview", image) ;
  key = cv2.waitKey(1) & 0xFF        
  if key == ord("q"):
    break
