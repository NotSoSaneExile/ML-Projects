import cv2
from time import time
from cvzone.HandTrackingModule import HandDetector
from cvzone import overlayPNG
import random

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
            cv2.putText(image_background, str(int(timer)), (590, 400), cv2.FONT_HERSHEY_COMPLEX, 6, (0, 0, 0), 4)

            if timer > 3:
                game_result = True
                timer = 0

                if hands:
                    hand = hands[0]
                    fingers_up = detector.fingersUp(hand)
                    players_choice = sum(fingers_up)
                    if players_choice == 0:
                        # Rock
                        print("Rock")
                        pass
                    elif players_choice > 0 and players_choice < 5:
                        # Scissors
                        print("Scissors")
                        pass
                    elif players_choice == 5:
                        # Paper
                        print("Paper")
                        pass
                    
                    options = ["rock", "paper", "scissors"]
                    random_option = random.choice(options)
                    image_AI = cv2.imread(f'Images/{random_option}.png', cv2.IMREAD_UNCHANGED)
                    image_AI = cv2.resize(image_AI, (241, 241), interpolation=cv2.INTER_AREA)
                    image_background = overlayPNG(image_background, image_AI, (212, 214))


    if game_result:
        image_background = overlayPNG(image_background, image_AI, (212, 214))

    # Crop the resized video capture into the player position of the background
    image_background[148:568 , 852:1138] = image_resized

    cv2.imshow("Rock! Paper! Scissors!", image_background)
    key = cv2.waitKey(1)
    if key == ord('s'):
        game_start = True
        initialTime = time()
        game_result = False


    
