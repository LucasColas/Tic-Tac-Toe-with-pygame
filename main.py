import pygame 

# Initialize the game
pygame.init()

class TicTacToe:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.board = [[0, 0, 0], 
                      [0, 0, 0], 
                      [0, 0, 0]]
        self.turn = 1
        self.circle = pygame.transform.scale(pygame.image.load("Assets/circle.png"), (self.width // 3, self.height // 3))
        self.cross = pygame.transform.scale(pygame.image.load("Assets/cross.png"), (self.width // 3, self.height // 3))
        self.winner = 0
        self.game_over = False
        self.background = (0, 0, 0)
        pygame.display.set_caption("Tic Tac Toe")
        self.change_color(self.circle, (0, 255, 0, 255))
        

    def change_color(self, asset, color):
        w,h = asset.get_size()
        r,g,b,_ = color
        for x in range(w):
            for y in range(h):
                a = asset.get_at((x,y))[3]
                asset.set_at((x,y), pygame.Color(r,g,b,a))

    def draw_lines(self):
        # Vertical lines
        pygame.draw.line(self.screen, (255, 255, 255), (self.width // 3, 0), (self.width // 3, self.height), 4)
        pygame.draw.line(self.screen, (255, 255, 255), (self.width // 3 * 2, 0), (self.width // 3 * 2, self.height), 4)
        # Horizontal lines
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.height // 3), (self.width, self.height // 3), 4)
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.height // 3 * 2), (self.width, self.height // 3 * 2), 4)

    def draw_figures(self):
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == 1:
                    self.screen.blit(self.circle, (x * self.width // 3, y * self.height // 3))
                elif self.board[y][x] == -1:
                    self.screen.blit(self.cross, (x * self.width // 3, y * self.height // 3))
    
    def check_winner(self):
        for row in range(3):
            if sum(self.board[row]) == 3 or sum(self.board[row]) == -3:
                self.winner = self.turn
                self.game_over = True

        for col in range(3):
            if self.board[0][col] + self.board[1][col] + self.board[2][col] == 3 or self.board[0][col] + self.board[1][col] + self.board[2][col] == -3:
                self.winner = self.turn
                self.game_over = True

        if self.board[0][0] + self.board[1][1] + self.board[2][2] == 3 or self.board[0][0] + self.board[1][1] + self.board[2][2] == -3:
            self.winner = self.turn
            self.game_over = True

        if self.board[0][2] + self.board[1][1] + self.board[2][0] == 3 or self.board[0][2] + self.board[1][1] + self.board[2][0] == -3:
            self.winner = self.turn
            self.game_over = True

        if all([self.board[row][col] != 0 for row in range(3) for col in range(3)]):
            self.game_over = True
       
        if self.game_over:
            print(self.winner)
    
    def update_board(self, row, col):
        if self.board[row][col] == 0:
            
            self.board[row][col] = self.turn
            
            self.check_winner()
            self.turn *= -1

    def reset(self):
        self.board = [[0, 0, 0], 
                      [0, 0, 0], 
                      [0, 0, 0]]
        self.turn = 1
        self.winner = 0
        self.game_over = False

    def display_winner(self):
        font = pygame.font.Font(None, 36)

        if self.winner == 1:
            text = font.render("Circle wins!", True, (255, 255, 255))
        elif self.winner == -1:
            text = font.render("Cross wins!", True, (255, 255, 255))
        else:
            text = font.render("It's a tie!", True, (255, 255, 255))
        
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)

    def update(self):
        self.screen.fill(self.background)
        self.draw_lines()
        self.draw_figures()
        if self.game_over:
            self.display_winner()
        pygame.display.update()
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    
                    x, y = pygame.mouse.get_pos()
                    row, col = y // (self.height // 3), x // (self.width // 3)
                    self.update_board(row, col)

                if event.type == pygame.KEYDOWN and self.game_over:
                    self.reset()

            self.update()
        pygame.quit()


tictactoe = TicTacToe(600, 600)
tictactoe.run()
