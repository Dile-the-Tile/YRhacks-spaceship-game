import pygame
import random
import math
import pygame.font
from pygame import mixer
from Enemy import Enemy
from Player import Player
from Laser import Laser


pygame.init()

display_width = 1400
display_height = 800
screen = pygame.display.set_mode((display_width, display_height))
current_player = Player(x=670, y=675)
white = (255, 255, 255)
black = (0, 0, 0)
red = (170, 0, 0)
light_red = (255, 0, 0)
green = (0, 155, 0)
light_green = (0, 255, 0)
yellow = (200, 200, 0)
light_yellow = (255, 255, 0)
blue = (105, 89, 246)
light_blue = (35, 13, 233)

background = pygame.image.load("2474215.jpg")
mixer.music.load("background music.mp3")
mixer.music.play(-1)

pygame.display.set_caption("Spaceship Game")
icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)

score_value = 0
font = pygame.font.Font("Transformers Movie.ttf", 90)
intro_font = pygame.font.Font("Sun Beach hotel.otf", 52)
score_font = pygame.font.Font("Elrotex.ttf", 28)
game_over_font = pygame.font.Font("GOOD PEOPLE.otf", 84)
button_font = pygame.font.Font("CartooNature.ttf", 42)
staff_font = pygame.font.Font("EnjoytheRide-Regular copy.otf", 68)
text_x = 10
text_y = 10

bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 0
bullet_y_change = 5
bullet_state = "ready"

enemy_list = []
Enemy1 = Enemy(random.randint(0, 1336), random.randint(150, 250), pygame.image.load("Enemy 1.png"))
Enemy2 = Enemy(random.randint(0, 1336), random.randint(150, 250), pygame.image.load("Enemy2.png"))
Enemy3 = Enemy(random.randint(0, 1336), random.randint(150, 250), pygame.image.load("Enemy3.png"))
Enemy4 = Enemy(random.randint(0, 1336), random.randint(150, 250), pygame.image.load("Enemy4.png"))
Enemy5 = Enemy(random.randint(0, 1336), random.randint(150, 250), pygame.image.load("Enemy 5.png"))
Enemy6 = Enemy(random.randint(0, 1336), random.randint(150, 250), pygame.image.load("Enemy6.png"))
Enemy7 = Enemy(random.randint(0, 1336), random.randint(150, 250), pygame.image.load("Enemy7.png"))
Enemy8 = Enemy(random.randint(0, 1336), random.randint(150, 250), pygame.image.load("Enemy8.png"))
enemy_list.append(Enemy1)
enemy_list.append(Enemy2)
enemy_list.append(Enemy3)
enemy_list.append(Enemy4)
enemy_list.append(Enemy5)
enemy_list.append(Enemy6)
enemy_list.append(Enemy7)
enemy_list.append(Enemy8)

intro_pics = pygame.image.load("2472783.jpg")
pausing_pics = pygame.image.load("19333449.jpg")

clock = pygame.time.Clock()


def pause():
    paused = True
    screen.blit(pausing_pics, (0, 0))
    first_message = font.render("Paused", True, (255, 255, 255))
    second_message = font.render("R: Continue or Q: Quit", True, (255, 255, 255))
    current_score = font.render(f"Current Score: {str(score_value)}", True, red)

    screen.blit(first_message, (580, 150))
    screen.blit(second_message, (280, 350))
    screen.blit(current_score, (350, 550))
    pygame.display.update()
    clock.tick(5)

    while paused:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_r:
                    paused = False
                elif events.key == pygame.K_q:
                    pygame.quit()
                    quit()


def game_intro():
    intro = True

    while intro:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_r:
                    intro = False
                if events.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.blit(intro_pics, (0, 0))

        message1 = font.render("Welcome Player", True, (255, 255, 255))
        message2 = font.render("Goal: Shoot Enemies", True, red)
        message3 = font.render("Press R to start the Game", True, (255, 255, 255))
        message4 = font.render("Press P to Pause  the Game", True, (255, 255, 255))
        screen.blit(message1, (350, 100))
        screen.blit(message2, (280, 250))
        screen.blit(message3, (100, 390))
        screen.blit(message4, (100, 530))

        show_button("Play", 200, 700, 150, 80, green, light_green, action="Play")
        show_button("Info", 650, 700, 150, 80, yellow, light_yellow, action="Info")
        show_button("Quit", 1050, 700, 150, 80, red, light_red, action="Quit")
        pygame.display.update()
        clock.tick(120)


def show_staff():
    showing = True
    while showing:

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(pausing_pics, (0, 0))
        message1 = staff_font.render("Game Created By", True, white)
        message2 = staff_font.render("Kevin Li", True, light_green)
        message3 = staff_font.render("Ethan Shi", True, light_green)
        message4 = staff_font.render("Matthew So", True, light_green)
        screen.blit(message1, (500, 100))
        screen.blit(message2, (300, 250))
        screen.blit(message3, (300, 390))
        screen.blit(message4, (300, 530))

        show_button("Return", 800, 400, 200, 100, green, light_green, action="Return")
        pygame.display.update()



def show_button(text, x, y, width, height, inactive_colour, active_color, action=None):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))

        if click[0] == 1 and action is not None:
            if action == "Quit":
                pygame.quit()
                quit()
            if action == "Play":
                gaming_loop()
            if action == "Info":
                game_info()
            if action == "Main":
                game_intro()
            elif action == "Staff":
                show_staff()
            elif action == "Return":
                game_intro()

    else:
        pygame.draw.rect(screen, inactive_colour, (x, y, width, height))
    text = button_font.render(text, True, (255, 255, 255))
    screen.blit(text, (x+30, y+25))


def game_info():
    check = True
    while check:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gaming_loop()

        screen.blit(background, (0, 0))
        message1 = font.render("INFO BAR", True, (255, 255, 255))
        message2 = intro_font.render("The Space invader game is to shoot the enemies", True, (255, 255, 255))
        message3 = intro_font.render("Press the R button to start the game ", True, (255, 255, 255))
        message4 = intro_font.render("Press P to Pause the game at any time", True, (255, 255, 255))
        screen.blit(message1, (450, 100))
        screen.blit(message2, (250, 250))
        screen.blit(message3, (250, 370))
        screen.blit(message4, (250, 490))

        show_button("Play", 250, 650, 150, 100, green, light_green, action="Play")
        show_button("Quit", 950, 650, 150, 100, red, light_red, action="Quit")

        pygame.display.update()



def show_score(x, y):
    score = score_font.render(f"Score {str(score_value)}", True, (255, 255, 255))
    pause_message = score_font.render("Press \"P\" to Pause ", True, (255,255,255))
    screen.blit(score, (x, y))
    screen.blit(pause_message, (x, y+50))


def fire_bullet(x_pos, y_pos):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x_pos+18, y_pos+15))


def collision_check(enemy_x, enemy_y, b_x, b_y):
    distance = math.sqrt(math.pow(enemy_x - b_x, 2) + math.pow(enemy_y - b_y, 2))
    if distance < 70:
        return True
    return False


def game_over_text():
    text = game_over_font.render("Game Over", True, (255, 0, 0))
    text2 = game_over_font.render(f"You Scored: {str(score_value)}", True, (255, 0, 0))
    text3 = game_over_font.render("Return to Main or Quit", True, (255, 0, 0))
    screen.blit(text, (450, 120))
    screen.blit(text2, (400, 190))
    screen.blit(text3, (300, 260))
    show_button("Staff", 630, 450, 150, 100, blue, light_blue, action="Staff")


# def reset():
#   game_over_text.empty()
#   current_player = Player(x=670, y=680)

def gaming_loop():
    global bullet_state, bullet_x, bullet_y
    running = True
    laser = Laser(random.randint(0, 1336), 0)
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        pygame.draw.line(screen, light_red, (0, 615), (1400, 620), 5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_player.x_change = -30
                elif event.key == pygame.K_RIGHT:
                    current_player.x_change = 30
                elif event.key == pygame.K_SPACE:
                    if bullet_state == "fire":
                        fire_bullet(bullet_x, bullet_y)
                    else:
                        bullet_sound = mixer.Sound("laser.mp3")
                        bullet_sound.play()
                        bullet_x = current_player.x
                        bullet_y = 680
                        fire_bullet(bullet_x, bullet_y)
                elif event.key == pygame.K_p:
                    pause()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    current_player.x_change = 0
                elif event.key == pygame.K_RIGHT:
                    current_player.x_change = 0

        laser.y += laser.y_change
        current_player.x += current_player.x_change
        screen.blit(Laser.laser_img, (laser.x, laser.y))
        if current_player.x <= 0:
            current_player.x = 0
        if current_player.x >= 1400 - 88:
            current_player.x = 1400 - 88
        if laser.y > 800:
            laser = Laser(random.randint(0, 1336), 0)

        for enemy in enemy_list:
            if enemy.y > 600 or laser.x in range(current_player.x-8, current_player.x+86) and laser.y in range(current_player.y, current_player.y+84):
                mixer.music.stop()
                for individual_enemy in enemy_list:
                    individual_enemy.y = 900
                    game_over_text()
                    show_button("Main", 240, 450, 150, 100, yellow, light_yellow, action="Main")
                    show_button("Quit", 950, 450, 150, 100, red, light_red, action="Quit")

            else:
                enemy.move()

            collision = collision_check(enemy.x, enemy.y, bullet_x, bullet_y)
            if collision:
                explosion_sound = mixer.Sound("Explosion-n.mp3")
                explosion_sound.play()
                bullet_y = 680
                bullet_state = "ready"
                global score_value
                score_value += 1

                enemy.x = random.randint(0, 1328)
                enemy.y = random.randint(50, 150)
            enemy.draw_enemy(enemy.x, enemy.y, screen)

            if bullet_state == "fire":
                if bullet_y < 0:
                    bullet_y = 680
                    bullet_state = "ready"
                else:
                    fire_bullet(bullet_x, bullet_y)
                    bullet_y -= bullet_y_change

            current_player.draw_player(current_player.x, current_player.y, screen)

            show_score(text_x, text_y)

            clock.tick(120)
        pygame.display.update()


game_intro()
gaming_loop()
