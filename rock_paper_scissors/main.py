import cv2
from time import time
from cvzone.HandTrackingModule import HandDetector

video_capture = cv2.VideoCapture(0)
video_capture.set(3, 640) # Width
video_capture.set(4, 480) # Height

# 1138, 568 | 852, 148 background params

# 0.4453125 | 0.875 are the resizes for fx and fy

detector = HandDetector(maxHands=1)
timer = 0
game_result = False
game_start = False



while True:
    image_background = cv2.imread("Images/background.png")

    success, image = video_capture.read()

    image_resized = cv2.resize(image, (0, 0), None, 0.875, 0.875)
    image_resized = image_resized[:,137:423] # 137:423 or 138:424
    
    # Track hands
    hands, img = detector.findHands(image_resized)

    if game_start:

        if game_result is False:
            timer = time() - initialTime
            cv2.putText(image_background, str(int(timer)), (605, 400), cv2.FONT_HERSHEY_COMPLEX, 6, (0, 0, 0), 4)

        if hands:
            hand = hands[0]
            fingers_up = detector.fingersUp(hand)
            print(fingers_up)

    # Crop the resized video capture into the player position of the background
    image_background[148:568 , 852:1138] = image_resized

    cv2.imshow("Rock! Paper! Scissors!", image_background)
    key = cv2.waitKey(1)
    if key == ord('s'):
        game_start = True
        initialTime = time()


    
