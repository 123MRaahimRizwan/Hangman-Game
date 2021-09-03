"""
Project : Hangman Game
Author : M.Raahim Rizwan
"""
# Setting up pygame
import pygame
import math
import random

from pygame.constants import K_SPACE

pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13)/2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)


# Load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# Game variables
hangman_status = 0
words = ["HELLO", "PORTUGAL", "SPAIN", "RONALDO", "MONKEY", "PIZZA", "MESSI","BIRTHDAY","SUN","MOON","STARS","UNIVERSE"]
word = random.choice(words)
guessed = []
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setting up the gameloop



def draw():
    """
    Draws the images and buttons on the screen and updates it
    """
    win.fill(WHITE)

    # Draw title
    text = TITLE_FONT.render("HANGMAN GAME", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    """
    Displays the message on the screen
    """
    pygame.time.delay(1000)
    win.fill(BLACK)
    text = WORD_FONT.render(message, 1, WHITE)
    win.blit(text, (WIDTH/2 - text.get_width() /
             2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)


# Main game loop
def main():
    """
    Plays the main game loop
    """
    global hangman_status
    run = True
    while run:
        FPS = 60
        clock = pygame.time.Clock()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        draw()
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message("YOU WON!")
            break
        if hangman_status == 6:
            display_message("YOU LOST!")
            break

if __name__ == '__main__':
    run = True
    while run:
        display_message("Welcome to the Hangman Game")
        main()
        run = False
pygame.quit()
quit()