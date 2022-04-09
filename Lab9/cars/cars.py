#машинки с музыкой игры, концовкой в виде меню счета, с монетками, супер монетками и счетом машин

import pygame
import random, time


pygame.init()
pygame.display.set_caption("Racer")


road = pygame.transform.scale(pygame.image.load("race.png"), (900, 800))
enemy = pygame.transform.scale(pygame.image.load("enemy.png"), (51, 100))
car = pygame.transform.scale(pygame.image.load("pla.png"), (51, 100))
coin = pygame.transform.scale(pygame.image.load("coin.png"), (50, 50))
coins = pygame.transform.scale(pygame.image.load("coins.png"), (50, 50))


font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 30)

gamemusic = pygame.mixer.Sound("carsgame.mp3") #музыка загружается


size = road.get_size()
size1 = car.get_size()
size2 = enemy.get_size()
size3 = coin.get_size()
size4 = coins.get_size()


font_end = pygame.font.SysFont('Arial', 66, bold = True)
font_money = pygame.font.SysFont('Arial', 30, bold = True)


screen = pygame.display.set_mode(size)
FPS = 60

#для машинок нас
x = random.randint(180,620)
y = 540

#для машинок врагов
x1 = random.randint(180,620)
y1 = 0

dy = 10 #скорость врагов
cnt = 0

#для монеток
x2 = random.randint(180,620)
y2 = random.randint(50,650)

#для super монеток
x3 = random.randint(180,620)
y3 = random.randint(50,650)
money = 0
super_money = 0

Clock = pygame.time.Clock()
running = True
while running:
    gamemusic.play()


    #показывает все эелементы
    screen.blit(road, (0,0))
    screen.blit(enemy,(x1,y1))
    screen.blit(coin,(x2,y2))
    screen.blit(coins, (x3, y3))
    screen.blit(car,(x,y))

    # показать счет игры
    render_score = font_money.render(f'SCORE: {money}', 1, pygame.Color('red'))
    screen.blit(render_score, (35, 35))  # выводит сбоку счет монеток
    render_score = font_money.render(f'SUPER: {super_money}', 1, pygame.Color('red'))
    screen.blit(render_score, (35, 60))  # выводит сбоку счет super монеток
    render_score = font_money.render(f'Cars: {cnt}', 1, pygame.Color('red'))
    screen.blit(render_score, (35, 85))  # выводит сбоку счет машин



    pressed = pygame.key.get_pressed()
    y1 += dy #скорость врагов

    if y1 > size[1]:
        x1 = random.randint(180,620)
        y1 = 0
        cnt += 1
        if cnt % 5 == 0:
            dy += 1 #скорость врагов увеличивается

    for event in pygame.event.get():  #выход
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    #чтобы были границы и не выходил за них
    if pressed[pygame.K_UP] and y > 0:
        y -= 10
    if pressed[pygame.K_DOWN] and y < 650:
        y += 10
    if pressed[pygame.K_LEFT] and x > 50:
        x -= 10
    if pressed[pygame.K_RIGHT] and x < 790:
        x += 10


    if y <= y2 + size3[1] and y >= y2 - size1[1] and x <= x2 + size1[0] and x >= x2 - size3[0]: #собрать монетку
        y2 = random.randint(50,650)
        x2 = random.randint(180,620)
        money += 1

    if y <= y3 + size4[1] and y >= y3 - size1[1] and x <= x3 + size1[0] and x >= x3 - size4[0]: #собрать super монетку
        y3 = random.randint(50,650)
        x3 = random.randint(180,620)
        super_money += 2

    if y <= y1 + size1[1] and y >= y1 - size2[1] and x <= x1 + size1[0] and x >= x1 - size2[0]: #столкновение с машиной
        running = False


    pygame.display.flip()
    Clock.tick(FPS)


menu = True
while menu:
    gamemusic.stop()

    pygame.display.flip()
    Clock.tick(FPS)
    screen.blit(road, (0,0))
    """
    render_end = font_end.render('GAME OVER',True, pygame.Color('black'))
    screen.blit(render_end, (190, 300))
    """


    time.sleep(0.5)  # небольшая задержка

    screen.fill('slategrey')  # окно серого цвета
    game_over = font.render("Game Over", True, pygame.Color('black'))
    screen.blit(game_over, (300, 250))  # с надписью конец игры
    score = font_small.render(f"Score: {money}", True, pygame.Color('black'))  # напишет общий счет
    screen.blit(score, (350, 350))  # покажет этот счет снизу
    score = font_small.render(f"Super score: {super_money}", True, pygame.Color('black'))  # напишет общий счет super
    screen.blit(score, (350, 380))  # покажет этот счет снизу
    score = font_small.render(f"Cars: {cnt}", True, pygame.Color('black'))  # напишет общий счет машин
    screen.blit(score, (350, 410))  # покажет этот счет снизу


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            menu = False
            pygame.quit()