# Rock Paper Scissors Game

This is a simple implementation of the Rock Paper Scissors game using computer vision techniques. The game allows the player to play against the computer using their webcam.

## Features

- Player can play Rock Paper Scissors against the computer.
- Computer uses a simple AI to make its choices.
- Real-time hand tracking is used to detect the player's hand gestures.
- Game result is displayed on the screen.
- Scores of the player and the computer are updated accordingly.
- The game can be started and restarted by pressing the 's' key.
- The game can be exited by pressing the 'x' or 'X' key.

## Requirements

To run this game, you need the following libraries installed:

- OpenCV (`cv2`)
- `time` module
- `cvzone` module
- `random` module
- MediaPipe (`mediapipe`)

You can install the required libraries using pip:

```
pip install opencv-python
pip install cvzone
pip install mediapipe
```

## Usage

1. Connect a webcam to your computer.
2. Navigate to the directory where the "main.py" script is. The program will start after typing "python main.py" when in correct directory.
3. The game window will open, showing the player's hand gesture and the computer's choice.
4. To start the game, press the 's' key.
5. Show your hand gesture in front of the webcam to make your choice (rock, paper, or scissors).
6. After 3 seconds, the game result will be displayed on the screen.
7. To play again, press the 's' key.
8. To exit the game, press the 'x' or 'X' key.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use it for your own purposes.

## Acknowledgments

- This project uses the `cvzone` library for hand tracking and overlaying images. Check out the [cvzone GitHub repository](https://github.com/codewithharry/cvzone) for more information.
- This project also uses the `mediapipe` library for hand tracking. Visit the [MediaPipe website](https://google.github.io/mediapipe/) for more details.
- The background image used in the game was made myself in [Canva](https://www.canva.com/).
- The hand images for rock, paper, and scissors are from [Flaticon](https://www.flaticon.com).