# clock minni с рукой в секундной стрелке

import pygame
import datetime
from math import pi, sin, cos

size = width, height = 800, 800  # 655, 669
center = (width / 2, height / 2)
clock_radius = 220
fps = 60

pygame.init()

pygame.display.set_caption('Clock')  # название окна

screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()

font_clock = pygame.font.SysFont('Arial', 26, bold=True)

game_background = pygame.image.load('minni_fon.png').convert()  # фон для часов

# руки
hand_min = pygame.image.load('hand_min.png').convert()  # рука для минут
hand_sec = pygame.image.load('hand_sec.png').convert()  # рука для секунд


def numbers(number, number_size, position):  # числа у часов
    font = pygame.font.SysFont('Arial', number_size, bold=True)
    text = font.render(number, True, pygame.Color('pink'))
    text_rect = text.get_rect(center=(position))  # твечает за позиции цифр
    screen.blit(text, text_rect)


def polar_to_cartesian(r, theta):  # формула специальная позиций цифр
    x, y = r * sin(pi * theta / 180), r * cos(pi * theta / 180)
    return x + width / 2, -(y - height / 2)


def Rotate(surf, image, pos, originPos, angle):
    screen.blit(game_background, (0, 0))  # вставить картинку
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset.rotate(angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)


w, h = hand_sec.get_size()
done = False

while not done:

    current_time = datetime.datetime.now()  # время сейчас
    second = current_time.second  # время сейчас секунды
    minute = current_time.minute  # время сейчас минуты

    # руки (картинка) секунды

    sec_angle = 6 * second
    clock.tick(fps)
    pos = (screen.get_width() / 2, screen.get_height() / 2)

    screen.fill(0)
    Rotate(screen, hand_sec, pos, (w / 2, h / 2), sec_angle)

    # minute полоской
    r = clock_radius - 120  # радиус
    theta = (minute + second / 60) * (360 / 60)
    pygame.draw.line(screen, pygame.Color('lightpink'), center, polar_to_cartesian(r, theta),
                     5)  # center начиная с центра, 10 ширина линии

    """


    #second простые полоски
    r = clock_radius - 80 #радиус
    theta = second * (360 / 60)
    pygame.draw.line(screen, pygame.Color('red'), center, polar_to_cartesian(r, theta), 5) #5 ширина линии



    #рука минуты картинка

    min_angle = minute * 6 + second * 0.1  # угол отклонения минутной стрелки за 1 секунду

    pos1 = (screen.get_width() / 2, screen.get_height() / 2)
    clock.tick(fps)
    screen.fill(0)
    Rotate(screen, hand_min, pos1, (w / 2, h / 2), min_angle)
    """

    # screen.fill(pygame.Color('black')) #фон

    pygame.draw.circle(screen, pygame.Color('pink'), center, clock_radius - 10,
                       10)  # рисуем круг пустой (границу) основной #clock_radius - 10 чтобы дальний круг был дальше
    pygame.draw.circle(screen, pygame.Color('white'), center, 10)  # рисуем круг (закрашенный)

    # надпись что это часы минни
    pygame.draw.rect(screen, pygame.Color('black'), [250, 650, 300, 100],
                     10)  # рисуем прямоугольник для текста пустой (границу)
    # показать текст
    render_clock = font_clock.render(f'CLOCK MINNI', 1, pygame.Color('black'))
    screen.blit(render_clock, (310, 690))  # выводит по середине

    for num in range(1, 13):  # цифры от 1 до 12 выведет
        numbers(str(num), 80,
                polar_to_cartesian(clock_radius - 80, num * 30))  # num * 30 чтобы отрезок между цифрами был

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
pygame.quit()
exit()
