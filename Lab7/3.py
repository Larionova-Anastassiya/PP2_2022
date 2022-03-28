import pygame

pygame.init()

WHITE = (255,255,255)
RED = (255,0,0)


size = weight, hight = 690, 690
screen = pygame.display.set_mode(size) #окно по нашему размеру
pygame.display.set_caption('Ellipse') #название окна
clock = pygame.time.Clock()

color = RED

#позиции
x, y = 100, 100
dx, dy = 0, 0

done = False

while not done:
    for event in pygame.event.get():

        key = pygame.key.get_pressed()

        # управление выходом
        if event.type == pygame.QUIT:
            done = True

        #управление клавишами перемещение
        if key[pygame.K_w]: #перемещение вверх
            dx, dy = 0, -20
            x += dx
            y += dy

            # ограничение чтобы не вышли за стену при нажатии
            if y < 0:
                x -= dx
                y -= dy

            pygame.draw.ellipse(screen, color, [x, y, 50, 50]) #рисунок круга

        if key[pygame.K_s]: #перемещение вниз
            dx, dy = 0, 20
            x += dx
            y += dy

            # ограничение чтобы не вышли за стену при нажатии
            if y > 650:
                x -= dx
                y -= dy

            pygame.draw.ellipse(screen, color, [x, y, 50, 50]) #рисунок круга

        if key[pygame.K_a]: #перемещение влево
            dx, dy = -20, 0
            x += dx
            y += dy

            # ограничение чтобы не вышли за стену при нажатии
            if x < 0:
                x -= dx
                y -= dy

            pygame.draw.ellipse(screen, color, [x, y, 50, 50]) #рисунок круга

        if key[pygame.K_d]: #перемещение вправо

            dx, dy = 20, 0
            x += dx
            y += dy

            #ограничение чтобы не вышли за стену при нажатии
            if x > 650:
                x -= dx
                y -= dy

            pygame.draw.ellipse(screen, color, [x, y, 50, 50]) #рисунок круга



    # показ на экране
    screen.fill(WHITE)
    pygame.draw.ellipse(screen, color, [x, y, 50,50]) #рисунок круга
    clock.tick(60)
    pygame.display.update()
pygame.quit()
