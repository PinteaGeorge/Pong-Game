import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
lime = (0, 255, 0)
pink = (255, 182, 193)
dark_blue = (0, 0, 128)
dark_green = (0, 128, 0)
orange = (255, 165, 0)
purple = (128, 0, 128)
gray = (128,128,128)

# Set up fonts
font = pygame.font.Font(None, 24)

# Set up buttons
play_button = pygame.Rect(width // 2 - 50, height // 2 - 50, 100, 40)
play_player_vs_player_button = pygame.Rect(width // 2 - 100, height // 2 + 20, 200, 40)
about_button = pygame.Rect(width // 2 - 50, height // 2 + 90, 100, 40)
settings_button = pygame.Rect(width // 2 - 50, height // 2 + 160, 100, 40)
quit_button = pygame.Rect(width // 2 - 50, height // 2 + 230, 100, 40)

# Set up end screen buttons
play_again_button = pygame.Rect(width // 2 - 75, height // 2 - 50, 150, 40)
back_to_main_button = pygame.Rect(width // 2 - 75, height // 2 + 20, 150, 40)

# Set up about page button
back_to_main_about_button = pygame.Rect(10, height - 30, 120, 20)

# Set up settings page and button
ball_color_options = [white, blue, red, yellow, green, lime, pink, dark_blue, dark_green, orange, purple]
left_paddle_color_options = [white, blue, red, yellow, green, lime, pink, dark_blue, dark_green, orange, purple]
right_paddle_color_options = [white, blue, red, yellow, green, lime, pink, dark_blue, dark_green, orange, purple]
back_to_main_settings_button = pygame.Rect(width // 2 - 75, height - 50, 150, 40)

selected_ball_color = white
selected_left_paddle_color = white
selected_right_paddle_color = white

# Default selected color
selected_color = pygame.Color(gray)

# Set up the paddles
paddle_width, paddle_height = 15, 60
paddle_speed = 5
left_paddle = pygame.Rect(50, height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 50 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Set up the ball
ball_size = 15
ball_speed = [5, 5]
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)

# Set up scores
left_score = 0
right_score = 0

# Game state
in_menu = True
in_game = False
in_about = False
in_end_screen = False
player_vs_player_mode = False 
in_settings = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            mouse_pos = event.pos
            if in_menu:
                if play_button.collidepoint(mouse_pos):
                    in_menu = False
                    in_game = True
                    in_end_screen = False  # Reset end screen state
                    left_score = 0
                    right_score = 0
                    player_vs_player_mode = False
                    in_settings = False
                elif play_player_vs_player_button.collidepoint(mouse_pos):
                    in_menu = False
                    in_game = True
                    in_end_screen = False  # Reset end screen state
                    left_score = 0
                    right_score = 0
                    player_vs_player_mode = True
                    in_settings = False
                elif about_button.collidepoint(mouse_pos):
                    in_menu = False
                    in_about = True
                    in_end_screen = False  # Reset end screen state
                    player_vs_player_mode = False
                    in_settings = False
                elif settings_button.collidepoint(mouse_pos):
                    in_menu = False
                    in_about = False
                    in_end_screen = False  # Reset end screen state
                    player_vs_player_mode = False 
                    in_settings = True
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
            elif in_end_screen:
                if play_again_button.collidepoint(mouse_pos):
                    in_end_screen = False
                    in_game = True
                    left_score = 0
                    right_score = 0
                elif back_to_main_button.collidepoint(mouse_pos):
                    in_end_screen = False
                    in_menu = True
                    player_vs_player_mode = False 
            elif in_about:
                if back_to_main_about_button.collidepoint(mouse_pos):
                    in_about = False
                    in_menu = True
                    player_vs_player_mode = False
            elif in_settings:
                # Check color selection in settings page
                for i, color_rect in enumerate(ball_color_rects):
                    if color_rect.collidepoint(mouse_pos):
                        selected_ball_color = ball_color_options[i]
                        break
                for i, color_rect in enumerate(left_paddle_color_rects):
                    if color_rect.collidepoint(mouse_pos):
                        selected_left_paddle_color = left_paddle_color_options[i]
                        break
                for i, color_rect in enumerate(right_paddle_color_rects):
                    if color_rect.collidepoint(mouse_pos):
                        selected_right_paddle_color = right_paddle_color_options[i]
                        break
                if back_to_main_settings_button.collidepoint(mouse_pos):
                    in_about = False
                    in_menu = True
                    player_vs_player_mode = False
                    in_settings = False

    if in_menu:
        # Draw menu
        win.fill(black)
        pygame.draw.rect(win, white, play_button)
        pygame.draw.rect(win, white, play_player_vs_player_button)
        pygame.draw.rect(win, white, about_button)
        pygame.draw.rect(win, white, settings_button)
        pygame.draw.rect(win, white, quit_button)

        # Draw text on buttons
        play_text = font.render("Play", True, black)
        play_player_vs_player_text = font.render("Player vs Player", True, black)
        about_text = font.render("About", True, black)
        settings_text = font.render("Settings", True, black)
        quit_text = font.render("Quit", True, black)

        # Calculate text positions for centering on buttons
        play_text_pos = (play_button.centerx - play_text.get_width() // 2, play_button.centery - play_text.get_height() // 2)
        play_player_vs_player_text_pos = (play_player_vs_player_button.centerx - play_player_vs_player_text.get_width() // 2, play_player_vs_player_button.centery - play_player_vs_player_text.get_height() // 2)
        about_text_pos = (about_button.centerx - about_text.get_width() // 2, about_button.centery - about_text.get_height() // 2)
        settings_text_pos = (settings_button.centerx - settings_text.get_width() // 2, settings_button.centery - settings_text.get_height() // 2)
        quit_text_pos = (quit_button.centerx - quit_text.get_width() // 2, quit_button.centery - quit_text.get_height() // 2)

        win.blit(play_text, play_text_pos)
        win.blit(play_player_vs_player_text, play_player_vs_player_text_pos)
        win.blit(about_text, about_text_pos)
        win.blit(settings_text, settings_text_pos)
        win.blit(quit_text, quit_text_pos)

    elif in_game:
        # Draw everything
        win.fill(black)  # Clear the screen with a black background
        pygame.draw.rect(win, selected_left_paddle_color, left_paddle)
        pygame.draw.rect(win, selected_right_paddle_color, right_paddle)
        pygame.draw.ellipse(win, selected_ball_color, ball)

        # Draw scores
        left_score_text = font.render(str(left_score), True, white)
        right_score_text = font.render(str(right_score), True, white)
        win.blit(left_score_text, (width // 4 - left_score_text.get_width() // 2, 20))
        win.blit(right_score_text, (3 * width // 4 - right_score_text.get_width() // 2, 20))

        # Game logic goes here
        keys = pygame.key.get_pressed()

        if player_vs_player_mode:
            # Player vs Player mode
            if keys[pygame.K_w] and left_paddle.top > 0:
                left_paddle.y -= paddle_speed
            if keys[pygame.K_s] and left_paddle.bottom < height:
                left_paddle.y += paddle_speed

            if keys[pygame.K_UP] and right_paddle.top > 0:
                right_paddle.y -= paddle_speed
            if keys[pygame.K_DOWN] and right_paddle.bottom < height:
                right_paddle.y += paddle_speed
        else:
            # Player vs Computer mode
            if keys[pygame.K_UP] and right_paddle.top > 0:
                right_paddle.y -= paddle_speed * 1.5
            if keys[pygame.K_DOWN] and right_paddle.bottom < height:
                right_paddle.y += paddle_speed * 1.5

            # Computer-controlled opponent logic
            if ball.y < left_paddle.centery and left_paddle.top > 0:
                left_paddle.y -= paddle_speed * 0.72
            elif ball.y > left_paddle.centery and left_paddle.bottom < height:
                left_paddle.y += paddle_speed * 0.72

        # Update ball position
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Ball collisions with walls
        if ball.top <= 0 or ball.bottom >= height:
            ball_speed[1] = -ball_speed[1]

        # Reset ball position if it goes beyond the right wall
        if ball.right >= width:
            ball.x = width // 2 - ball_size // 2
            ball.y = height // 2 - ball_size // 2
            left_score += 1

        # Reset ball position if it goes beyond the left wall
        if ball.left <= 0:
            ball.x = width // 2 - ball_size // 2
            ball.y = height // 2 - ball_size // 2
            right_score += 1

        # Check for game end
        if left_score == 10 or right_score == 10:
            in_game = False
            in_end_screen = True

        # Ball collisions with paddles
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_speed[0] = -ball_speed[0]

    elif in_about:
        # Draw "About" page
        about_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean feugiat pretium ante, vel fringilla tellus ornare eget. Suspendisse tincidunt magna ac mi ornare, sed elementum elit auctor. Phasellus nec molestie orci, sit amet condimentum urna. Curabitur aliquet enim a urna rutrum vehicula. Morbi vitae luctus leo, id congue odio. In sollicitudin nibh ac elit posuere imperdiet nec eu magna. Sed facilisis nisl vitae erat convallis rutrum. Phasellus semper lacus ac dapibus volutpat."

        # Wrap text to fit within the window width
        lines = []
        words = about_text.split()
        current_line = words[0]
        for word in words[1:]:
            if font.size(current_line + ' ' + word)[0] < width - 50:  # 50 is the margin
                current_line += ' ' + word
            else:
                lines.append(current_line)
                current_line = word

        # Append the last line
        lines.append(current_line)

        # Calculate total height of the text block
        total_height = len(lines) * font.get_height()

        # Draw "About" page
        win.fill(black)
        y = (height - total_height) // 2
        for line in lines:
            about_text = font.render(line, True, white)
            win.blit(about_text, (width // 2 - about_text.get_width() // 2, y))
            y += font.get_height()

        # Draw back to main page button
        pygame.draw.rect(win, white, back_to_main_about_button)
        back_to_main_about_text = font.render("Back", True, black)
        back_to_main_about_text_pos = (back_to_main_about_button.centerx - back_to_main_about_text.get_width() // 2, back_to_main_about_button.centery - back_to_main_about_text.get_height() // 2)
        win.blit(back_to_main_about_text, back_to_main_about_text_pos)

    elif in_end_screen:
        # Draw end screen
        win.fill(black)
        pygame.draw.rect(win, white, play_again_button)
        pygame.draw.rect(win, white, back_to_main_button)

        # Draw text on buttons
        play_again_text = font.render("Play Again", True, black)
        back_to_main_text = font.render("Back to Main Page", True, black)

        # Calculate text positions for centering on buttons
        play_again_text_pos = (play_again_button.centerx - play_again_text.get_width() // 2, play_again_button.centery - play_again_text.get_height() // 2)
        back_to_main_text_pos = (back_to_main_button.centerx - back_to_main_text.get_width() // 2, back_to_main_button.centery - back_to_main_text.get_height() // 2)

        win.blit(play_again_text, play_again_text_pos)
        win.blit(back_to_main_text, back_to_main_text_pos)

        # Draw winning player text
        if player_vs_player_mode:
            if left_score == 10:
                winning_text = font.render("Player 1 Wins!", True, white)
            elif right_score == 10:
                winning_text = font.render("Player 2 Wins!", True, white)
        else:
            if left_score == 10:
                winning_text = font.render("Computer Wins!", True, white)
            elif right_score == 10:
                winning_text = font.render("Player Wins!", True, white)

        win.blit(winning_text, (width // 2 - winning_text.get_width() // 2, height // 4))
    elif in_settings:
        # Draw settings page
        win.fill(black)

        # Draw ball color options
        ball_color_rects = []
        ball_color_text = font.render("Ball Color", True, white)
        win.blit(ball_color_text, (width // 8 - ball_color_text.get_width() // 2, height // 8))
        for i, color in enumerate(ball_color_options):
            rect = pygame.Rect((i * 60) + 20, height // 4 + 30, 50, 50)
            pygame.draw.rect(win, color, rect)
            pygame.draw.rect(win, gray if color == selected_ball_color else white, rect, 2)
            ball_color_rects.append(rect)

        # Draw left paddle color options
        left_paddle_color_rects = []
        left_paddle_color_text = font.render("Left Paddle Color", True, white)
        win.blit(left_paddle_color_text, (width // 8 - left_paddle_color_text.get_width() // 2, height // 8 + 200))
        for i, color in enumerate(left_paddle_color_options):
            rect = pygame.Rect((i * 60) + 20, height // 2 + 30, 50, 50)
            pygame.draw.rect(win, color, rect)
            pygame.draw.rect(win, gray if color == selected_left_paddle_color else white, rect, 2)
            left_paddle_color_rects.append(rect)

        # Draw right paddle color options
        right_paddle_color_rects = []
        right_paddle_color_text = font.render("Right Paddle Color", True, white)
        win.blit(right_paddle_color_text, (width // 8 - right_paddle_color_text.get_width() // 2, height // 8 + 350))
        for i, color in enumerate(right_paddle_color_options):
            rect = pygame.Rect((i * 60) + 20, 3 * height // 4 + 30, 50, 50)
            pygame.draw.rect(win, color, rect)
            pygame.draw.rect(win, gray if color == selected_right_paddle_color else white, rect, 2)
            right_paddle_color_rects.append(rect)

        # Draw back to main menu button
        pygame.draw.rect(win, white, back_to_main_settings_button)
        back_to_menu_text = font.render("Back to Main Menu", True, black)
        back_to_menu_text_pos = (back_to_main_settings_button.centerx - back_to_menu_text.get_width() // 2, back_to_main_settings_button.centery - back_to_menu_text.get_height() // 2)
        win.blit(back_to_menu_text, back_to_menu_text_pos)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)