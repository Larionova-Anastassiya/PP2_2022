#змейка с меню и музыкой и супер яблоком

import pygame
from random import randrange

size = width, height = 1050, 650 #размер окна
block = 50 #прыжок длина 0, 50, 100, 150, 200, ... 800

x, y = randrange(0, width, block), randrange(0, height, block) #координаты головы в рандомном месте змейки по х, по y
apple = randrange(0, width, block), randrange(0, height, block) #координаты нашего яблока
apple2 = randrange(0, width, block), randrange(0, height, block) #координаты нашего super яблока
dirs = {'W': True, 'S': True, 'A': True, 'D': True} #правильность нажатия кнопок

score = 0
length = 1 #размер
snake = [(x, y)] #наша змейка уже
dx, dy = 0, 0 # движение змейки
fps = 5 #скорость с которой движется змейка

pygame.init() #для того чтобы работало как надо команды пайгейма
pygame.display.set_caption('Snake game') #название окна

screen = pygame.display.set_mode([width, height]) #создает окно и размер нашего окна
clock = pygame.time.Clock() #время

font_score = pygame.font.SysFont('Arial', 26, bold = True) #дает некий текст написать шрифт, размер, жирный (счет)
font_end = pygame.font.SysFont('Arial', 70, bold = True) #(концовку)
font_menu = pygame.font.SysFont('Arial', 50, bold = False) #pygame.font.Font('fontname', 50) со своим шрифтом

#фоны загрузить
game_background = pygame.image.load('fon2 — копия.jpg').convert()
menu_background = pygame.image.load('menu — копия.jpg').convert()

gamemenu = pygame.mixer.Sound("game.mp3") #музыка загружается
gameover = pygame.mixer.Sound("gameover_snake.mp3") #музыка загружается


def main_menu():

    gamemenu.play() #музыка заиграет
    menu = True

    while menu:
        screen.blit(menu_background, (0, 0)) #фон меню

        # при нажатии мышки ENTER
        #render_menu = font_menu.render('Press ENTER', True, pygame.Color('black')) #надпись нажать
        #screen.blit(render_menu, (400,500))

        #при нажатии мышки
        render_menu = font_menu.render('CLICK', True, pygame.Color('black'))  # надпись нажать
        screen.blit(render_menu, (430, 550))
        render_menu2 = font_menu.render('or Press ENTER', True, pygame.Color('black'))  # надпись нажать
        screen.blit(render_menu2, (350, 600))

        for event in pygame.event.get(): #выход при нажатии #при нажатии мышки

            mx, my = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and 430 <= mx <= 550 and 570 <= my <= 600:
                menu = False

        pygame.display.flip()

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]: #когда нажимаем enter то начинается (K_RETURN --> ENTER)
            #gamemenu.stop() #выключит музыку
            break

main_menu()


while True: #бесконечный форик пока может работать окно не закроется

    #фон
    #screen.fill(pygame.Color('darkgreen')) #простой цвет однотонный
    screen.blit(game_background, (0, 0)) #вставить картинку


    # рисунок змеи и яблока
    for i, j in snake:
        pygame.draw.rect(screen, pygame.Color('chartreuse'), (i, j, block - 1, block - 1)) #рисует некий квадрат ( где, цветом, тюпл который хранит 4 аргумента позиции где и ширину и длину прямоугольника)
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, block, block))
    pygame.draw.rect(screen, pygame.Color('yellow'), (*apple2, block, block))  # super


    #показать счет игры
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('black'))
    screen.blit(render_score, (5, 5)) #выводит сбоку


    #движение змейки
    x += dx * block
    y += dy * block
    snake.append((x, y))
    snake = snake[-length:] #если длина равна 1 то урежим змейку чтобы не оставляла след после себя каждой координатой


    #если проиграли конец
    if x < -block or x > width or y < -block or y > height or len(snake) != len(set(snake)): #когда выходим за стены (сверху и снизу это блок, право лево это размер) #когда проходим через себя
        while True:
            gameover.play()  # музыка заиграет концовки (но зацикленно)
            render_end = font_end.render('GAME OVER', True, pygame.Color('black'))
            gamemenu.stop() #остановит музыку игры
            screen.blit(render_end, (335, 300))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


    #поедание яблока при этом растет и ускоряется
    if snake[-1] == apple:
        apple = randrange(0, width, block), randrange(0, height, block) #появляется новое яблоко
        length += 1 #увеличивается размер
        fps += 1 #ускоряет
        score += 1 #увеличивает счет

    # поедание super яблока при этом растет и ускоряется двойне
    if snake[-1] == apple2:
        apple2 = randrange(0, width, block), randrange(0, height, block)  # появляется новое яблоко
        length += 1  # увеличивается размер
        fps += 5  # ускоряет больше
        score += 1  # увеличивает счет



    #выход
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #чтобы не было ошибки при выходе с экрана (крестик)
            exit() #выйдет с окна

    pygame.display.flip()  # чтобы работал и показывал верно роль обновления экрана
    clock.tick(fps)  # чтобы не лагал передает количество тиков


    #ходы змейки по нажатиям кнопок
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']: #если нажмем на "w" то сделается что либо ри этом условие правильности хода
        dx, dy = 0, -1 #изменится вверх y
        dirs = {'W': True, 'S': False, 'A': True, 'D': True} #'S': False потому что не можем пойти в ту сторону сразу
    if key[pygame.K_s] and dirs['S']: #если нажмем на "s" то сделается что либо
        dx, dy = 0, 1 #изменится вниз y
        dirs = {'W': False, 'S': True, 'A': True, 'D': True} #'W': False потому что не можем пойти в ту сторону сразу
    if key[pygame.K_a] and dirs['A']: #если нажмем на "a" то сделается что либо
        dx, dy = -1, 0 #изменится влево x
        dirs = {'W': True, 'S': True, 'A': True, 'D': False} #'D' False потому что не можем пойти в ту сторону сразу
    if key[pygame.K_d] and dirs['D']: #если нажмем на "w" то сделается что либо
        dx, dy = 1, 0 #изменится направо x
        dirs = {'W': True, 'S': True, 'A': False, 'D': True} #'A' False потому что не можем пойти в ту сторону сразу
