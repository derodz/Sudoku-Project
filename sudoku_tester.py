from sudoku_generator import SudokuGenerator
from button import Button
from text import Text
import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku Start Screen")

# Colors and Fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 35)

# Global y-shift
global_y_shift = 100

# Create Buttons and Texts
button_width, button_height = 200, 40
difficulty_button_x_shift = 100
buttons = [
    Button(difficulty_button_x_shift, 200 + global_y_shift, button_width, button_height, "EASY", GREEN, GRAY, font),
    Button(difficulty_button_x_shift, 300 + global_y_shift, button_width, button_height, "MEDIUM", BLUE, GRAY, font),
    Button(difficulty_button_x_shift, 400 + global_y_shift, button_width, button_height, "HARD", RED, GRAY, font)
]

cell_count_x_shift = 550
texts = [
    Text(cell_count_x_shift, 225 + global_y_shift, "30", small_font, WHITE, align="center"),
    Text(cell_count_x_shift, 325 + global_y_shift, "40", small_font, WHITE, align="center"),
    Text(cell_count_x_shift, 425 + global_y_shift, "50", small_font, WHITE, align="center")
]

# Main Header
main_header = Text(380, 0 + global_y_shift, "Welcome to Sudoku", font, WHITE, align="center")

# Select Header
select_header = Text(380, 50 + global_y_shift, "Select Game Mode:", font, WHITE, align="center")

# Column Headers
header1 = Text(200, 150 + global_y_shift, "Difficulty", font, WHITE, align="center")
header2 = Text(550, 150 + global_y_shift, "Number of empty cells", font, WHITE, align="center")

# Function to draw Sudoku board
def draw_sudoku_board(board):
    grid_size = SCREEN_WIDTH - 100
    cell_size = grid_size // 9
    offset_x, offset_y = 50, 50

    # Draw grid lines
    for i in range(10):
        line_width = 2 if i % 3 == 0 else 1
        pygame.draw.line(screen, WHITE, (offset_x + i * cell_size, offset_y), (offset_x + i * cell_size, offset_y + grid_size), line_width)
        pygame.draw.line(screen, WHITE, (offset_x, offset_y + i * cell_size), (offset_x + grid_size, offset_y + i * cell_size), line_width)

    # Fill in numbers
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                num_text = font.render(str(board[row][col]), True, WHITE)
                x = offset_x + col * cell_size + cell_size // 2 - num_text.get_width() // 2
                y = offset_y + row * cell_size + cell_size // 2 - num_text.get_height() // 2
                screen.blit(num_text, (x, y))

# Main loop
running = True
selected_difficulty = None
while running:
    screen.fill(BLACK)

    # Get mouse position and click state
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle button hover and click
    for idx, button in enumerate(buttons):
        button.check_hover(mouse_pos)
        if button.is_clicked(mouse_pos, mouse_pressed):
            selected_difficulty = [30, 40, 50][idx]
            print(f"Selected Difficulty: {button.text} ({selected_difficulty} empty cells)")
            running = False  # Exit the menu

    # Draw headers
    main_header.draw(screen)
    select_header.draw(screen)
    header1.draw(screen)
    header2.draw(screen)

    # Draw buttons and texts
    for button, text in zip(buttons, texts):
        button.draw(screen)
        text.draw(screen)

    # Update display
    pygame.display.flip()

# Generate Sudoku puzzle
sudoku_gen = SudokuGenerator(9, selected_difficulty)
sudoku_gen.fill_values()
sudoku_gen.remove_cells()
sudoku_board = sudoku_gen.get_board()

# Sudoku display loop
running = True
while running:
    screen.fill(BLACK)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw Sudoku board
    draw_sudoku_board(sudoku_board)

    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
