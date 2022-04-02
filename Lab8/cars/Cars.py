#машинки с музыкой и музыкой концовкой (но без монеток)

# библиотеки
import pygame, sys
from pygame.locals import * #чтобы не использовать постоянно пайгейм в указании клавиш
import random, time #для рандомного появления противника

# чтобы работали команды
pygame.init()

# скорость прорисовки
FPS = 60
FramePerSec = pygame.time.Clock()

# цвета используемые
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# данные размер, скорость и начало счета
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600


SPEED = 5
SCORE = 0
new_score = 0 #для монеток

# шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 30)
game_over = font.render("Game Over", True, BLACK)


background = pygame.image.load("race.png") #фон
music = pygame.mixer.Sound('carsgame.mp3') #музыка в самой игре

# создали окно
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")





#класс противники прорисовываются
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("enemy.png"), (51, 100)) #картинка противника
        self.rect = self.image.get_rect() #размер картинки берем
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) #центр картинки по размеру

    def move(self): #действие машинки
        global SCORE
        self.rect.move_ip(0, SPEED) #со скоростью едет
        if (self.rect.top > 600):
            SCORE += 1 #увеличивается счет если проехала и заново появляется
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) #появление в рандомном месте



#игрок уже мы машинка которой управляем
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("pla.png"), (51, 100)) #картинка игрока
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) #центр картинки

    #движение и управление картинкой
    def move(self):
        pressed_keys = pygame.key.get_pressed() #присваиваем значение действий

        #управление клавишами стрелками
        if pressed_keys[K_UP]:#вверх
            self.rect.move_ip(0, -5)
        if self.rect.height < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:#вниз
                self.rect.move_ip(0,5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]: #влево и чтобы не уходило за стену
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH: #вправо и чтобы не уходило за стену
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# присваиваем классы
P1 = Player()
E1 = Enemy()

# Создание групп при столкновении sprite
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Добавление нового пользовательского события увеличение скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Основное игровое окно
running = True
while running:



    music.play()
    # скорость добавляется и при нажатии выход
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == pygame.QUIT:
            running = False

    #рисуем фон и первоначальный счетчик сверху во время игры
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, WHITE)
    DISPLAYSURF.blit(scores, (10, 10))

    # Перемещает и перерисовывает все спрайты
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()




    # если произойдет столкновение между Игроком и врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        music.stop()
        pygame.mixer.Sound('gameover.mp3').play()
        time.sleep(0.5) #небольшая задержка

        DISPLAYSURF.fill('slategrey')  #окно серого цвета
        DISPLAYSURF.blit(game_over, (30, 250)) #с надписью конец игры
        score = font_small.render(f"Score: {SCORE}", True, BLACK) #напишет общий счет
        DISPLAYSURF.blit(score, (150, 350)) #покажет этот счет снизу
        score = font_small.render(f"Score coin: {new_score}", True, BLACK)  # напишет счет монеток
        DISPLAYSURF.blit(score, (150, 400))  # покажет этот счет снизу

        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(8) #задержка закрытия
        pygame.quit() #выход из окна
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)