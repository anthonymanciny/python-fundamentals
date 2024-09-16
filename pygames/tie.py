import pygame
import sys

# Inicializa o pygame
pygame.init()

# Constantes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_COLOR = (50, 150, 50)
CELL_SIZE = WIDTH // 3

# Fonte para texto
font = pygame.font.Font(None, 74)

# Configurações da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha")

def draw_board():
    screen.fill(BOARD_COLOR)
    for x in range(1, 3):
        pygame.draw.line(screen, WHITE, (0, x * CELL_SIZE), (WIDTH, x * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, WHITE, (x * CELL_SIZE, 0), (x * CELL_SIZE, HEIGHT), LINE_WIDTH)

def draw_markers(board):
    for row in range(3):
        for col in range(3):
            marker = board[row][col]
            if marker:
                color = RED if marker == 'X' else BLUE
                text = font.render(marker, True, color)
                text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(text, text_rect)

def check_winner(board):
    lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for line in lines:
        if board[line[0][0]][line[0][1]] == board[line[1][0]][line[1][1]] == board[line[2][0]][line[2][1]] != '':
            return board[line[0][0]][line[0][1]]
    return None

def is_board_full(board):
    return all(cell != '' for row in board for cell in row)

def main():
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    draw_board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                row, col = y // CELL_SIZE, x // CELL_SIZE

                if board[row][col] == '':
                    board[row][col] = current_player
                    if check_winner(board):
                        print(f"Jogador {current_player} venceu!")
                        game_over = True
                    elif is_board_full(board):
                        print("Empate!")
                        game_over = True
                    current_player = 'O' if current_player == 'X' else 'X'
                
                draw_board()
                draw_markers(board)

        pygame.display.flip()

if __name__ == "__main__":
    main()
