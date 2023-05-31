import cv2

video_capture = cv2.VideoCapture(0)
video_capture.set(3, 640) # Width
video_capture.set(4, 480) # Height

# 1138, 568 | 852, 148 background params

# 0.4453125 | 0.875 are the resizes for fx and fy

while True:

    # Crop the background with the video capture
    image_background = cv2.imread("Images/background.png")

    success, image = video_capture.read()

    image_resized = cv2.resize(image, (0, 0), None, 0.875, 0.875)
    image_resized = image_resized[:,137:423] # 137:423 or 138:424

    image_background[148:568 , 852:1138] = image_resized

    cv2.imshow("Background", image_background)
    cv2.waitKey(1)