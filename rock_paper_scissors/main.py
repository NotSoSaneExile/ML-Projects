import cv2
from time import time
from cvzone.HandTrackingModule import HandDetector
from cvzone import overlayPNG
import random


class RockPaperScissorsGame:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.video_capture.set(3, 640)  # Width
        self.video_capture.set(4, 480)  # Height

        self.detector = HandDetector(maxHands=1)
        self.timer = 0
        self.game_result = False
        self.game_start = False
        self.initialTime = 0
        self.player_score = 0
        self.ai_score = 0

    def determine_winner(self, player_choice, ai_choice):
        if player_choice == ai_choice:
            return "It's a tie!"
        elif (player_choice == "rock" and ai_choice == "scissors") or (player_choice == "scissors" and ai_choice == "paper") or (player_choice == "paper" and ai_choice == "rock"):
            return "Player wins!"
        else:
            return "AI wins!"

    def run(self):
        image_AI = None

        while True:
            image_background = cv2.imread("Images/background.png")
            cv2.putText(image_background, str(int(self.ai_score)), (430, 128), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            cv2.putText(image_background, str(int(self.player_score)), (1092, 128), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            success, image = self.video_capture.read()

            image_resized = cv2.resize(image, (0, 0), None, 0.875, 0.875)
            image_resized = image_resized[:, 137:423]  # 137:423 or 138:424

            try:
                # Track hands
                hands, img = self.detector.findHands(image_resized)

                if self.game_start:
                    if self.game_result is False:
                        self.timer = time() - self.initialTime
                        cv2.putText(image_background, str(int(self.timer)), (590, 400), cv2.FONT_HERSHEY_COMPLEX, 6,(0, 0, 0), 4)

                        if self.timer > 3:
                            self.game_result = True
                            self.timer = 0

                            if hands:
                                hand = hands[0]
                                fingers_up = self.detector.fingersUp(hand)
                                players_choice = sum(fingers_up)
                                options = ["rock", "paper", "scissors"]
                                random_option = random.choice(options)
                                image_AI = cv2.imread(f'Images/{random_option}.png', cv2.IMREAD_UNCHANGED)
                                image_AI = cv2.resize(image_AI, (241, 241), interpolation=cv2.INTER_AREA)
                                image_background = overlayPNG(image_background, image_AI, (212, 214))

                                if 0 <= players_choice <= 1:
                                    # Rock
                                    print("Rock")
                                    player_choice = "rock"
                                elif 1 < players_choice < 5:
                                    # Scissors
                                    print("Scissors")
                                    player_choice = "scissors"
                                elif players_choice == 5:
                                    # Paper
                                    print("Paper")
                                    player_choice = "paper"

                                ai_choice = random_option
                                winner = self.determine_winner(player_choice, ai_choice)
                                if winner == "Player wins!":
                                    self.player_score += 1
                                elif winner == "AI wins!":
                                    self.ai_score += 1
                                

                if self.game_result:
                    image_background = overlayPNG(image_background, image_AI, (212, 214))
                    cv2.putText(image_background, winner, (480, 660), cv2.FONT_HERSHEY_COMPLEX, 2,(0, 0, 0), 2)

                # Crop the resized video capture into the player position of the background
                image_background[148:568, 852:1138] = image_resized

                cv2.imshow("Rock! Paper! Scissors!", image_background)
                key = cv2.waitKey(1)
                if key == ord('s'):
                    self.game_start = True
                    self.initialTime = time()
                    self.game_result = False
                elif key == ord('x') or key == ord('X'):
                    break

            except Exception as e:
                # Handle the exception when no hands are detected at first
                print("No hands detected...")
                self.game_start = False
                self.game_result = False
                continue
        
        # Release video capture and close windows
        self.video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run()
