import pygame, random

WIDTH, HEIGHT = 1200, 800  # базовый размер окна
FPS = 60
draw = False  # нажатие, зажатие - рисуем, отжали - не рисуем
lastPos = (0, 0)  # базовая позиция
radius = 15  # базовый радиус для инструментов
color = 'blue'  # базовый цвет
mode = 'pen'  # базовый режим

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint')
clock = pygame.time.Clock()
screen.fill(pygame.Color('black'))  # закрашиваем в цвет, чтобы внутри цикла не обновлялось
fontRadius = pygame.font.SysFont('Arial', 66, bold=True)
fontText = pygame.font.SysFont('Arial', 16, bold=True)


def drawLine(screen, start, end, width, color): #рисунок для линии
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)


def drawCircle(screen, start, end, width, color): #рисунок для кругов
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)


def drawRectangle(screen, start, end, width, color): #рисунок для прямоугольников
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    widthr = abs(x1 - x2)
    height = abs(y1 - y2)
    pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)


while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # Нажатия на клавиатуру
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rectangle'

            if event.key == pygame.K_w: #вызовет готовый пэинт из сайта
                import paint1

            if event.key == pygame.K_RETURN: #все вернет в исходное
                screen.fill(pygame.Color('black'))

            if event.key == pygame.K_c:
                mode = 'circle'
            if event.key == pygame.K_p:
                mode = 'pen'
            if event.key == pygame.K_e:
                mode = 'erase'
            if event.key == pygame.K_y:
                color = 'yellow'
            if event.key == pygame.K_d:
                color = 'red'
            if event.key == pygame.K_b:
                color = 'black'
            if event.key == pygame.K_g:
                color = 'gray'
            if event.key == pygame.K_n:
                color = 'green'
            if event.key == pygame.K_o:
                color = (random.randrange(256), random.randrange(256), random.randrange(256))
            if event.key == pygame.K_UP:
                radius = min(200, radius + 1)  # ограничение по максимальному размеру радиуса
            if event.key == pygame.K_DOWN:
                radius = max(1, radius - 1)  # ограничение по минимальному размеру радиуса

        # Нажатие на мышку
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            if mode == 'pen':
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)
            prevPos = event.pos

        # Отпускание мышки
        if event.type == pygame.MOUSEBUTTONUP:
            if mode == 'rectangle':
                drawRectangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'circle':
                drawCircle(screen, prevPos, event.pos, radius, color)
            draw = False

        # Перемещение мышки
        if event.type == pygame.MOUSEMOTION:
            if draw and mode == 'pen':
                drawLine(screen, lastPos, event.pos, radius, color)
            elif draw and mode == 'erase':
                drawLine(screen, lastPos, event.pos, radius, 'black')
            lastPos = event.pos

    # show radius & color
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))
    renderRadius = fontRadius.render(f'{radius}', True, pygame.Color(color))
    screen.blit(renderRadius, (5, 5))
    renderText = fontText.render(f'| Pen - P | '
                                 f'Rectangle - R | '
                                 f'Circle - C | '
                                 f'Erase - E | '
                                 f'Yellow - Y | '
                                 f'Black - B | '
                                 f'Gray - G | '
                                 f'Red - D | '
                                 f'Green - N | '
                                 f'Random - O |', False, pygame.Color('red'))
    screen.blit(renderText, (125, 15))
    renderText1 = fontText.render(f' Размер стрелочками вверх и вниз | '
                                  f' Переходный цвет - W' , False, pygame.Color('red'))
    screen.blit(renderText1, (125, 35))
    renderText1 = fontText.render(f' Очистить все - ENTER (убрать после переходного)', False, pygame.Color('red'))
    screen.blit(renderText1, (125, 65))

    # display
    pygame.display.flip()
    clock.tick(FPS)

# 1. -- Создание окна (1200x800)
# 2. -- Events - нажатие, отпускание, перемещение мышки
# 3. -- Рисование линии
# 4. -- Функции рисование круга, прямоугольника
# 5. -- Добавление режимов: 'circle', 'rectangle', 'erase'
# 6. -- Добавление цветов
# 7. -- Вывод радиуса и цвета на экран
