import pygame
import sys
import random
import time

# Direction constants
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.direction = RIGHT
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.apple = self.get_random_apple()
        self.score = 0

    def get_random_apple(self):
        return (random.randint(0, self.width - 10) // 10 * 10, random.randint(0, self.height - 10) // 10 * 10)

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != DOWN:
                        self.direction = UP
                    elif event.key == pygame.K_DOWN and self.direction != UP:
                        self.direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.direction = RIGHT

            self.move_snake()
            self.check_collision()
            self.display_game()

            self.clock.tick(10)

    def move_snake(self):
        head = self.snake[0]
        if self.direction == UP:
            new_head = (head[0], head[1] - 10)
        elif self.direction == DOWN:
            new_head = (head[0], head[1] + 10)
        elif self.direction == LEFT:
            new_head = (head[0] - 10, head[1])
        elif self.direction == RIGHT:
            new_head = (head[0] + 10, head[1])

        self.snake.insert(0, new_head)
        if self.snake[0] == self.apple:
            self.score += 1
            self.apple = self.get_random_apple()
        else:
            self.snake.pop()

    def check_collision(self):
        head = self.snake[0]
        if (head[0] < 0 or head[0] >= self.width or
            head[1] < 0 or head[1] >= self.height or
            head in self.snake[1:]):
            self.reset()

    def display_game(self):
        self.display.fill((0, 0, 0))
        for pos in self.snake:
            pygame.draw.rect(self.display, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(self.apple[0], self.apple[1], 10, 10))
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.display.blit(text, (10, 10))
        pygame.display.flip()

if __name__ == '__main__':
    game = SnakeGame()
    game.play()