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


def drawRectangle(screen, start, end, width, color): #рисунок для прямоугольников (правильно если снизу слева, до правого верха)
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    widtht = abs(x1 - x2)
    height = abs(y1 - y2)
    #чтобы были правильные в разные стороны
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widtht, height), width)
    if x1 > x2 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widtht, height), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widtht, height), width)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widtht, height), width)


def drawSquare(screen, start, end, width, color):  #рисунок для квадрата
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    #найдем ширину и высоту, а потом по меньшей построим квадрат
    widthr = abs(x2 - x1)
    heightr = abs(y2 - y1)
    mn = min(widthr, heightr) #меньшей


    #правый низ (правильно если сверху лева, до правого низа)
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn), width)
        #pygame.draw.line(screen, pygame.Color(color), (x1, y1 - radius / 2.3), (x1 ,y1 + mn), width) #start position and end права первая линия (radius / 2.3 чтобы ровно было угол)
        #pygame.draw.line(screen, pygame.Color(color), (x1 + mn, y1 - radius / 2.3), (x1 + mn, y1 + mn), width)  # start position and end слева вторая линия
        #pygame.draw.line(screen, pygame.Color(color), (x1, y1), (x1 + mn, y1), width)  # start position and end сверху первая линия
        #pygame.draw.line(screen, pygame.Color(color), (x1 - radius / 2.3, y1 + mn), (x1 + mn + radius / 2, y1 + mn), width)  # start position and end снизу вторая линия
    #pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn), width)

    # правый верх (правильно если снизу лева, до правого верха)
    if y2 < y1 and x2 > x1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn), width)
        #pygame.draw.line(screen, pygame.Color(color), (x1, y1), (x1, y1 - mn), width)  # start position and end права первая линия
        #pygame.draw.line(screen, pygame.Color(color), (x1 + mn, y1 + radius / 2), (x1 + mn, y1 - mn - radius / 2.3), width)  # start position and end слева вторая линия
        #pygame.draw.line(screen, pygame.Color(color), (x1 - radius / 2.3, y1 - mn), (x1 + mn, y1 - mn), width)  # start position and end сверху первая линия
        #pygame.draw.line(screen, pygame.Color(color), (x1 - radius / 2.3, y1), (x1 + mn, y1), width)  # start position and end снизу вторая линия

    # левый верх (правильно если снизу справа, до левого верха)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn), width)
        #pygame.draw.line(screen, pygame.Color(color), (x1 - mn, y1 + radius / 2), (x1 - mn, y1 - mn - radius / 2.3), width)  # start position and end права первая линия
        #pygame.draw.line(screen, pygame.Color(color), (x1, y1 + radius / 2), (x1, y1 - mn - radius / 2.3), width)  # start position and end слева вторая линия
        #pygame.draw.line(screen, pygame.Color(color), (x1 - mn, y1 - mn), ( x1, y1 - mn), width)  # start position and end сверху первая линия
        #pygame.draw.line(screen, pygame.Color(color), (x1 - mn, y1), (x1, y1), width)  # start position and end снизу вторая линия

    # левый низ (правильно если сверху справа, до левого низа)
    if x1 > x2 and y1 < y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn), width)
        #pygame.draw.line(screen, pygame.Color(color), (x1, y2 + radius / 2), (x1, y2 - mn - radius / 2.3), width)  # start position and end права первая линия
        #pygame.draw.line(screen, pygame.Color(color), (x1 - mn, y2 - mn - radius / 2.3), (x1 - mn, y2 + radius / 2), width)  # start position and end слева вторая линия
        #pygame.draw.line(screen, pygame.Color(color), (x1 - mn, y2), (x1, y2), width)  # start position and end снизу первая линия
        #pygame.draw.line(screen, pygame.Color(color), (x1 - mn, y2 - mn), (x1, y2 - mn), width)  # start position and end сверху вторая линия



def drawRightTriangle(screen, start, end, width, color):  #рисунок прямоугольный треугольник закрашенный
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    # чтобы были правильные в разные стороны
    if x2 > x1 and y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2) , (x1, y2))) #чтобы линиями то добавить (, width)
    if x1 > x2 and y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2) , (x1, y2)))
    if x1 > x2 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2) , (x1, y2)))
    if x2 > x1 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2) , (x1, y2)))



def drawequilateralTriangle(screen, start, end, width, color):  # рисунок равносторонний треугольник закрашенный
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    width_b = abs(x2 - x1)
    height = (3**0.5) * width_b / 2  #высота

    # чтобы были правильные в разные стороны
    if y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)))  # чтобы линиями то добавить (, width)
    else:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)))




def drawerhombus(screen, start, end, width, color):  # рисунок ромба
  x1 = start[0]
  x2 = end[0]
  y1 = start[1]
  y2 = end[1]

  pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width) #о точкам даем значения

  """
  # чтобы были правильные в разные стороны
  if x2 > x1 and y2 > y1:
      pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))  # чтобы линиями то добавить (, width)
  if x1 > x2 and y2 > y1:
      pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
  if x1 > x2 and y1 > y2:
      pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
  if x2 > x1 and y1 > y2:
      pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
"""




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
            if event.key == pygame.K_s:
                mode = 'square'
            if event.key == pygame.K_t:
                mode = 'Righttriangle'
            if event.key == pygame.K_l:
                mode = 'equilateraltriangle'
            if event.key == pygame.K_j:
                mode = 'rhombus'
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
            elif mode == 'square':
                drawSquare(screen, prevPos, event.pos, radius, color)
            elif mode == 'Righttriangle':
                drawRightTriangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'equilateraltriangle':
                drawequilateralTriangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'rhombus':
                drawerhombus(screen, prevPos, event.pos, radius, color)
            draw = False

        # Перемещение мышки
        if event.type == pygame.MOUSEMOTION:
            if draw and mode == 'pen':
                drawLine(screen, lastPos, event.pos, radius, color)
            elif draw and mode == 'erase':
                drawLine(screen, lastPos, event.pos, radius, 'black')
            lastPos = event.pos

    # show radius & color
    pygame.draw.rect(screen, pygame.Color('red'), (5, 5, 115, 75))
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
                                 f'Random - O | '
                                 f'Square - S | ', False, pygame.Color('red'))
    screen.blit(renderText, (125, 15))
    renderText1 = fontText.render(f' Размер стрелочками вверх и вниз | '
                                  f' Переходный цвет - W | '
                                  f'Right triangle - T | '
                                  f'equilateral triangle - L |'
                                  f' rhombus - J |' , False, pygame.Color('red'))
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
# 8. -- Рисование квадрата
# 9. -- рисование прямоугольного треугольника
# 10. -- рисование равностороннего треугольника
# 11. -- рисование ромба

