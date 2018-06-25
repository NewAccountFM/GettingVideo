# import OpenCV
import cv2

# create instanceVideoCapture
cap = cv2.VideoCapture(0)
    
while True:
# read a frame
    ret, frame = cap.read()

    # show image
    cv2.imshow('Raw Frame', frame)


    # wait for user input for 1ms
    # when the esc key input, break 
    k = cv2.waitKey(1)
    if k == 27:
        break

# release and close all windows
cap.release()
cv2.destroyAllWindows()