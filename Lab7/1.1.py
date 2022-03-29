#часы с двумя стрелками рабочими

import pygame, datetime
from math import sin, cos, pi

pygame.init()

#картинки для работы
clock_background = pygame.transform.scale(pygame.image.load('mickeyclock2.jpeg'), (900, 900))  # фон для часов
right_hand = pygame.transform.scale(pygame.image.load('right hand.png'), (594 // 2, 322 // 2))
left_hand = pygame.transform.scale(pygame.image.load('left hand.png'), (770 // 2, 230 // 2))

#размеры
SIZE = (900, 900)
center = (SIZE[0] / 2, SIZE[1] / 2)
clock_radius = 400

#показ на окне и окно с нашим размером и названием
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Clock")
FPS = 60
clock = pygame.time.Clock()


#для поворота картинок по углам относительно центра (из сайта скинутым преподавателями)
def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset_center_to_pivot.rotate(angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)


running = True
while running:

    #выход
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #показ фона микки
    screen.blit(clock_background, (0, 0))


    #сейчас время (отдельно секунды и минуты)
    current_date_time = datetime.datetime.now()
    minute = current_date_time.minute
    second = current_date_time.second

    ## Minutes картинкой
    theta = (minute + second / 60) * (360 / 60)
    blitRotate(screen, right_hand, center, (right_hand.get_width() / 2 + 110, left_hand.get_height() / 2 + 75), theta + 75)

    ## Seconds картинкой
    theta = second * (360 / 60)
    blitRotate(screen, left_hand, center, (left_hand.get_width() / 2 - 145, left_hand.get_height() / 2), theta - 87)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
