import pygame
import sys
import numpy as np

# Initialisation de Pygame
pygame.init()

# Définition des constantes
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
# Couleurs
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
BUTTON_COLOR = (100, 100, 100)
BUTTON_TEXT_COLOR = (255, 255, 255)
# Police de caractères
FONT = pygame.font.SysFont(None, 60)

# Création de la fenêtre du jeu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Tableau de jeu
board = np.zeros((BOARD_ROWS, BOARD_COLS))

# Fonction pour dessiner la grille du jeu
def draw_grid():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Fonction pour dessiner les formes (X et O)
def draw_shapes():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), CIRCLE_RADIUS, LINE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

# Fonction pour placer la forme (X ou O) dans la case sélectionnée
def mark_square(row, col, player):
    board[row][col] = player

# Fonction pour vérifier si une case est vide
def is_square_available(row, col):
    return board[row][col] == 0

# Fonction pour vérifier si un joueur a gagné
def check_winner(player):
    # Vérification des lignes et colonnes
    for i in range(BOARD_ROWS):
        if np.all(board[i] == player) or np.all(board[:, i] == player):
            return True
    # Vérification des diagonales
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

# Fonction principale du jeu
def main():
    global board
    player = 1
    game_over = False
    replay_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0] // SQUARE_SIZE
                mouseY = event.pos[1] // SQUARE_SIZE

                if replay_button.collidepoint(event.pos):
                    board = np.zeros((BOARD_ROWS, BOARD_COLS))
                    game_over = False
                    player = 1
                elif not game_over and is_square_available(mouseY, mouseX):
                    mark_square(mouseY, mouseX, player)
                    if check_winner(player):
                        game_over = True
                    elif np.all(board != 0):
                        game_over = True  # Match nul

                    player = player % 2 + 1

        screen.fill(BG_COLOR)
        draw_grid()
        draw_shapes()

        if game_over:
            pygame.draw.rect(screen, BUTTON_COLOR, replay_button)
            text = FONT.render("Rejouer", True, BUTTON_TEXT_COLOR)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        pygame.display.update()

if __name__ == "__main__":
    main()
