
import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
while True:
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    #lower_blue = np.array([110,50,50]) 
    upper_blue = np.array([255,255,130])
    lower_blue = np.array([50, 86, 100])
    #upper_blue = np.array([121, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
 
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
 
    for contour in contours:
        area = cv2.contourArea(contour)
 
        if area > 7000:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)
 
    cv2.rectangle(frame,(100,400),(320,450),(0,255,0),-1)
    cv2.rectangle(frame,(321,450),(521,400),(255,0,0),-1)
    cv2.circle(frame,(550,320), 70, (0,0,255), -1)
    cv2.ellipse(frame, (60, 300), (100, 40), 270, 0, 360, (255, 255,0), -1);
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    #cv2.imshow("Mak", blurred_frame)
 
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()

