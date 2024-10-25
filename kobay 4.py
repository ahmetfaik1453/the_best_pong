import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Fullscreen mode

# Screen dimensions
WIDTH, HEIGHT = screen.get_size()  # Get the current screen size
pygame.display.set_caption("Dünyanın En İyi Pong'u")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Paddle properties
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 350
initial_paddle_speed = 40
paddle_speed1 = 0
paddle_speed2 = 0
paddle_decay = 6.0  # Decay factor

# Ball properties
BALL_SIZE = 25
ball_speed_x, ball_speed_y = 10.0, 10.0
MAX_BALL_SPEED = 15.0  # Max speed for the ball

# Player scores
player1_score = 0
player2_score = 0

# Set scores
player1_sets = 0
player2_sets = 0

# Paddle positions
paddle1_y = paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Ball position
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

# Font for scores
font = pygame.font.Font(None, 74)

# Trail properties
trail_length = 30  # Number of previous positions to keep
trail = []

# Load sounds
hit_sound = pygame.mixer.Sound("C:/Users/ahmet/Desktop/python dosyalari/mixkit-basketball-ball-hard-hit-2093.wav")
score_sound = pygame.mixer.Sound("C:/Users/ahmet/Desktop/python dosyalari/negative_beeps-6008.mp3")

# Load and scale the icon
icon = pygame.image.load("C:/Users/ahmet/Desktop/python dosyalari/loser-hand-sign-language-gesture-humor-mens-t-shirt.jpg")
icon_size = (100, 100)  # Desired size (width, height)
icon = pygame.transform.scale(icon, icon_size)

# Initial score colors
player1_score_color = WHITE
player2_score_color = WHITE

# Function to get a dynamic color based on time
def get_dynamic_color(time):
    r = int((math.sin(time) + 1) * 127.5)
    g = int((math.sin(time + 2) + 1) * 127.5)
    b = int((math.sin(time + 4) + 1) * 127.5)
    return (r, g, b)

# Function to draw the ball with transparency
def draw_ball(color, pos_x, pos_y, alpha=255):
    s = pygame.Surface((BALL_SIZE, BALL_SIZE), pygame.SRCALPHA)
    s.fill((0, 0, 0, 0))
    pygame.draw.ellipse(s, (color[0], color[1], color[2], alpha), (0, 0, BALL_SIZE, BALL_SIZE))
    screen.blit(s, (pos_x, pos_y))

# Function to display defeat effect
def display_defeat_effect(loser):
    global ball_x, ball_y, ball_speed_x, ball_speed_y, trail

    # Backup original screen content
    original_screen = screen.copy()

    # Animation duration
    duration = 0.5  # 0.5 seconds
    start_time = time.time()

    while time.time() - start_time < duration:
        # Calculate elapsed time ratio
        t = (time.time() - start_time) / duration

        # Update screen background color
        bg_color = (255 * t, 0, 255 * (1 - t))
        screen.fill(bg_color)

        if loser == 1:
            # Scale and draw the icon for player 1
            scale = 1 + 0.5 * math.sin(10 * t * math.pi)
            scaled_icon = pygame.transform.scale(icon, (int(icon_size[0] * scale), int(icon_size[1] * scale)))
            screen.blit(scaled_icon, (WIDTH // 4 - scaled_icon.get_width() // 2, HEIGHT // 2 - scaled_icon.get_height() // 2))
        else:
            # Scale and draw the icon for player 2
            scale = 1 + 0.5 * math.sin(10 * t * math.pi)
            scaled_icon = pygame.transform.scale(icon, (int(icon_size[0] * scale), int(icon_size[1] * scale)))
            screen.blit(scaled_icon, (3 * WIDTH // 4 - scaled_icon.get_width() // 2, HEIGHT // 2 - scaled_icon.get_height() // 2))

        # Update the screen
        pygame.display.flip()
        pygame.time.delay(30)

    # Restore original screen content
    screen.blit(original_screen, (0, 0))
    pygame.display.flip()

    # Play score sound
    score_sound.play()

# Function to get a random color
def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Score limit for each set
SCORE_LIMIT = 10

# Function to check collision between ball and paddle
def ball_paddle_collision(ball_x, ball_y, paddle_x, paddle_y):
    # Check for collision using rects
    ball_rect = pygame.Rect(ball_x, ball_y, BALL_SIZE, BALL_SIZE)
    paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    return ball_rect.colliderect(paddle_rect)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            # Handle key releases to stop paddle movement
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddle_speed1 = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle_speed2 = 0
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle_speed1 = -initial_paddle_speed
    if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle_speed1 = initial_paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle_speed2 = -initial_paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle_speed2 = initial_paddle_speed
    
    # Apply decay to paddle speeds
    if paddle_speed1 > 0:
        paddle_speed1 = max(0, paddle_speed1 - paddle_decay)
    elif paddle_speed1 < 0:
        paddle_speed1 = min(0, paddle_speed1 + paddle_decay)
    
    if paddle_speed2 > 0:
        paddle_speed2 = max(0, paddle_speed2 - paddle_decay)
    elif paddle_speed2 < 0:
        paddle_speed2 = min(0, paddle_speed2 + paddle_decay)

    # Update paddle positions
    paddle1_y += paddle_speed1
    paddle2_y += paddle_speed2

    # Ensure paddles stay within screen bounds
    paddle1_y = max(0, min(paddle1_y, HEIGHT - PADDLE_HEIGHT))
    paddle2_y = max(0, min(paddle2_y, HEIGHT - PADDLE_HEIGHT))
    
    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Add the current ball position to the trail
    trail.append((ball_x, ball_y))
    if len(trail) > trail_length:
        trail.pop(0)
    
    # Check for ball collision with walls
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y *= -1
        hit_sound.play()  # Play hit sound
    
    # Check if the ball collides with the paddles
    if ball_speed_x < 0 and ball_paddle_collision(ball_x, ball_y, 0, paddle1_y):
        ball_speed_x *= -1
        hit_sound.play()  # Play hit sound
    if ball_speed_x > 0 and ball_paddle_collision(ball_x, ball_y, WIDTH - PADDLE_WIDTH, paddle2_y):
        ball_speed_x *= -1
        hit_sound.play()  # Play hit sound
    
    # Check if the ball goes out of bounds on the left side
    if ball_x < -BALL_SIZE:
        player2_score += 1
        player2_score_color = get_random_color()
        display_defeat_effect(1)  # Display defeat effect for player 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x, ball_speed_y = random.choice([5, 7, 9, 11, 13, 14]) * random.choice((1, -1)), random.choice([5, 7, 9, 11, 13, 14]) * random.choice((1, -1))
        trail = []
        print(f"{time.asctime(time.localtime(time.time()))}: Player 1 has {player1_score} points. Player 2 has {player2_score} points.")
        
        # Check if a set is won
        if player2_score >= SCORE_LIMIT:
            player2_sets += 1
            print(f"{time.asctime(time.localtime(time.time()))}: Player 2 wins the set! Sets: Player 1 - {player1_sets}, Player 2 - {player2_sets}")
            # Reset scores for the next set
            player1_score = player2_score = 0
            player1_score_color = player2_score_color = WHITE

    # Check if the ball goes out of bounds on the right side
    if ball_x > WIDTH:
        player1_score += 1
        player1_score_color = get_random_color()
        display_defeat_effect(2)  # Display defeat effect for player 2
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x, ball_speed_y = random.choice([5, 7, 9, 11, 13, 14]) * random.choice((1, -1)), random.choice([5, 7, 9, 11, 13, 14]) * random.choice((1, -1))
        trail = []
        print(f"{time.asctime(time.localtime(time.time()))}: Player 1 has {player1_score} points. Player 2 has {player2_score} points.")
        
        # Check if a set is won
        if player1_score >= SCORE_LIMIT:
            player1_sets += 1
            print(f"{time.asctime(time.localtime(time.time()))}: Player 1 wins the set! Sets: Player 1 - {player1_sets}, Player 2 - {player2_sets}")
            # Reset scores for the next set
            player1_score = player2_score = 0
            player1_score_color = player2_score_color = WHITE

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    draw_ball(get_dynamic_color(time.time()), ball_x, ball_y)
    
    # Draw the trails
    for i in range(len(trail)):
        alpha = int(255 * (1 - i / trail_length))
        draw_ball(get_dynamic_color(time.time()), trail[i][0], trail[i][1], alpha)

    # Draw scores
    player1_score_surface = font.render(str(player1_score), True, player1_score_color)
    player2_score_surface = font.render(str(player2_score), True, player2_score_color)
    screen.blit(player1_score_surface, (WIDTH // 4 - player1_score_surface.get_width() // 2, 10))
    screen.blit(player2_score_surface, (3 * WIDTH // 4 - player2_score_surface.get_width() // 2, 10))

    # Draw set scores at the top
    set_scores_surface = font.render(f"Player 1 Sets: {player1_sets} | Player 2 Sets: {player2_sets}", True, YELLOW)
    screen.blit(set_scores_surface, (WIDTH // 2 - set_scores_surface.get_width() // 2, 0))

    pygame.display.flip()
    clock.tick(144)

pygame.quit()
