import cv2

video_capture = cv2.VideoCapture(0)
video_capture.set(3, 1024) # Width
video_capture.set(4, 768) # Height

while True:

    # Crop the background with the video capture
    image_background = cv2.imread("Images/background.png")

    success, image = video_capture.read()
    cv2.imshow("Rock - Paper - Scissors", image)
    cv2.imshow("Background", image_background)
    cv2.waitKey(1)