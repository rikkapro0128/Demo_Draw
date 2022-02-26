# import the opencv library
import cv2 as cv

# define a video capture object
vid = cv.VideoCapture(0)
color = (255, 140, 0)
width = int(vid.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv.CAP_PROP_FRAME_HEIGHT))
axesLength = (100, 50)
angle = 0
startAngle = 0
endAngle = 360

if not vid.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    cv.ellipse(frame, ((int)(width / 2), (int)(height / 2)), (150,90), 0, 0, 360, (255, 0, 0), thickness = 3)
    cv.putText(frame, "Nguyen Tan Phap", (150 , 400), fontFace = cv.FONT_HERSHEY_PLAIN, fontScale = 2,  color = color, thickness = 3)
    # show image
    cv.imshow("Display window", frame)
    
    k = cv.waitKey(1)
    if k == ord("q"):
        break
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()
