World's Best Pong Game
This project is a unique, dynamic Pong game created using Python and the Pygame library. It includes features such as paddle and ball movement, score tracking, defeat effects, and randomized colors. The game operates in fullscreen mode and has unique sound effects and graphical enhancements.

Features
Full-Screen Gameplay: The game automatically adjusts to your screen size for an immersive experience.
Dynamic Colors and Effects: Uses dynamic colors based on time, creating a vibrant and evolving visual experience.
Paddle and Ball Physics: The paddles respond with smooth deceleration after key release, and the ball has collision physics for realistic interactions.
Score and Set Tracking: Tracks points for each player and announces set victories when a player reaches the set score limit.
Sound Effects: Audio feedback for hits and scores, adding intensity to the gameplay.
Defeat Effects: Animated defeat graphics display for the player who loses a point.
Ball Trail Effect: Adds a fading trail behind the ball, enhancing the visual impact.
Installation
Clone the Repository

git clone https://github.com/ahmetfaik1453/pong-game.git
cd pong-game
Install Pygame Ensure you have Pygame installed. You can install it via pip:

pip install pygame
Add Sound and Image Files

Place your sound files in the specified directory or adjust the code paths.
Update paths for the hit sound (mixkit-basketball-ball-hard-hit-2093.wav) and score sound (negative_beeps-6008.mp3).
Include the defeat icon image (loser-hand-sign-language-gesture-humor-mens-t-shirt.jpg).
How to Play
Player 1 Controls: Use W to move up and S to move down.
Player 2 Controls: Use the Up and Down arrow keys to move.
Objective: Score points by getting the ball past the opponent's paddle. First player to reach the set limit wins the set.
Running the Game
Run the following command in the project's directory:


python pong_game.py
The game will launch in fullscreen mode.

Code Overview
Ball Physics: Ball speed increases after each paddle collision up to a max speed, while direction changes based on the paddle's position.
Defeat Animation: When a player loses a point, a visual effect is displayed before gameplay resumes.
Trail Effect: Ball trails create a smoother and more visually pleasing experience.
Future Improvements
Enhanced AI for Single Player Mode
Power-Ups and Special Moves
Adjustable Settings for Ball Speed and Paddle Size

Contact
Ahmet Faik Özsoy

GitHub: ahmetfaik1453

LinkedIn: Ahmet Faik Özsoy

Enjoy playing the World's Best Pong Game!
