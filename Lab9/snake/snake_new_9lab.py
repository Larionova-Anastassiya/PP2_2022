#змейка с меню и музыкой и супер яблоком, со стенами
#примерно идеи:
#сделать меню с выбором классик (обычный готовый форик 1 и 5), изи ( увеличение будет по скорости на 1 и супер яблоко на 1)
#сделать меню с выбором медиум (увеличение на 1 и 3), хард ( увеличение будет по скорости на 3 и супер яблоко на 7 или со стенками)
#сделать меню и форик по нажатию картинок будет делать Медиум = Тру. Если медиум тру то фпс += 1 и так далее


#библиотека тайм и каждый раз в вайл считать секунды сколько прошло и если какое то количество секунд прошло, то обновится локация яблока (10000)

import pygame
from random import randrange
from datetime import timedelta
from datetime import datetime

size = width, height = 1050, 630 #размер окна
block = 30 #прыжок длина 0, 30, 70, 100, 130, ... 800

x, y = randrange(0, width, block), randrange(0, height, block) #координаты головы в рандомном месте змейки по х, по y
apple = randrange(0, width, 60), randrange(0, height, 60) #координаты нашего яблока
apple2 = randrange(0, width, block), randrange(0, height, block) #координаты нашего super яблока
dirs = {'W': True, 'S': True, 'A': True, 'D': True} #правильность нажатия кнопок

score = 0
length = 1 #размер
snake = [(x, y)] #наша змейка уже
dx, dy = 0, 0 # движение змейки
fps = 5 #скорость с которой движется змейка

start = int(datetime.now().strftime("%S"))  # сейчас время секунд



pygame.init() #для того чтобы работало как надо команды пайгейма
pygame.display.set_caption('Snake game') #название окна

screen = pygame.display.set_mode([width, height]) #создает окно и размер нашего окна
clock = pygame.time.Clock() #время

font_score = pygame.font.SysFont('Arial', 26, bold = True) #дает некий текст написать шрифт, размер, жирный (счет)
font_end = pygame.font.SysFont('Arial', 70, bold = True) #(концовку)
font_menu = pygame.font.SysFont('Arial', 120, bold = False) #pygame.font.Font('fontname', 50) со своим шрифтом

#фоны загрузить
game_background = pygame.image.load('fon_game.jpg').convert()
menu_background = pygame.image.load('menu.jpg').convert()
name = pygame.image.load('name_snake.png').convert()


#картинки кнопок
classic = pygame.image.load('classic.png').convert()
easy = pygame.image.load('easy.png').convert()
medium = pygame.image.load('medium.png').convert()
hard = pygame.image.load('hard.png').convert()


gamemenu = pygame.mixer.Sound("menu_snake.mp3") #музыка загружается
game = pygame.mixer.Sound("game.mp3") #музыка загружается
gameover = pygame.mixer.Sound("gameover_snake.mp3") #музыка загружается


#режимы
classic_game, easy_game, medium_game, hard_game = False, False, False, False



def main_menu():

    gamemenu.play() #музыка заиграет
    menu = True

    while menu:
        screen.blit(menu_background, (0, 0)) #фон меню

        #buttons
        classic_button = screen.blit(classic, (130, 30)) #кнопка классического режима
        easy_button = screen.blit(easy, (130, 140))  # кнопка easy режима
        medium_button = screen.blit(medium, (130, 250))  # кнопка medium режима
        hard_button = screen.blit(hard, (130, 360))  # кнопка hard режима

        # при нажатии мышки ENTER
        #render_menu = font_menu.render('Press ENTER', True, pygame.Color('black')) #надпись нажать
        #screen.blit(render_menu, (400,500))

        #name game
        screen.blit(name, (190, 490))


        for event in pygame.event.get(): #выход при нажатии #при нажатии мышки

            mx, my = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                exit()



            #нажатие кнопок
            if event.type == pygame.MOUSEBUTTONDOWN and classic_button.collidepoint(mx, my): #CLASSIC
                global classic_game
                classic_game = True
                gamemenu.stop()
                game.play()
                menu = False

            elif event.type == pygame.MOUSEBUTTONDOWN and easy_button.collidepoint(mx, my): #EASY
                global easy_game
                easy_game = True
                gamemenu.stop()
                game.play()
                menu = False

            elif event.type == pygame.MOUSEBUTTONDOWN and medium_button.collidepoint(mx, my): #MEDIUM
                global medium_game
                medium_game = True
                gamemenu.stop()
                game.play()
                menu = False

            elif event.type == pygame.MOUSEBUTTONDOWN and hard_button.collidepoint(mx, my): #HARD
                global hard_game
                hard_game = True
                gamemenu.stop()
                game.play()
                menu = False


        pygame.display.flip()


main_menu()




while True: #бесконечный форик пока может работать окно не закроется


    time = int(datetime.now().strftime("%S")) #сейчас время секунд


    #time = 5000  # после 5 секунд отсчет
    #first = pygame.time.get_ticks()  # начало создавания нашей работы




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
            gameover.play(0)  # музыка заиграет концовки (но зацикленно)
            render_end = font_end.render('GAME OVER', True, pygame.Color('black'))
            game.stop() #остановит музыку игры
            screen.blit(render_end, (335, 300))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()



    #поедание яблока при этом растет и ускоряется
    if snake[-1] == apple:
        apple = randrange(0, width, block), randrange(0, height, block) #появляется новое яблоко

        if classic_game == True:
            fps += 1 #ускоряет
            score += 1 #увеличивает счет
        elif easy_game == True:
            fps += 1 #ускоряет
            score += 1 #увеличивает счет
        elif medium_game == True:
            fps += 2 #ускоряет
            score += 2 #увеличивает счет
        elif hard_game == True:
            fps += 3 #ускоряет
            score += 2 #увеличивает счет

        length += 1  # увеличивается размер


    # поедание super яблока при этом растет и ускоряется двойне
    if snake[-1] == apple2:
        apple2 = randrange(0, width, block), randrange(0, height, block)  # появляется новое яблоко


        if classic_game == True:
            fps += 5  # ускоряет больше
            score += 2  # увеличивает счет
        elif easy_game == True:
            fps += 2 #ускоряет
            score += 2 #увеличивает счет
        elif medium_game == True:
            fps += 3 #ускоряет
            score += 3 #увеличивает счет
        elif hard_game == True:
            fps += 5 #ускоряет
            score += 3 #увеличивает счет

        length += 1 #увеличивается размер


    if start == time - 10: #поистечению 10 секунд супер яблоко меняет свое положение и отсчет идет заново
        apple2 = randrange(0, width, block), randrange(0, height, block)  # появляется новое яблоко
        start = time







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
