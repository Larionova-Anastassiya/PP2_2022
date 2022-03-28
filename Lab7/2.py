#music player

import pygame

pygame.init()
pygame.mixer.init()

WHITE = (255,255,255)
RED = (255,0,0)


size = weight, hight = 500, 500 #по нашему размеру
screen = pygame.display.set_mode(size) #окно по нашему размеру
pygame.display.set_caption('Music player') #название окна
clock = pygame.time.Clock()

#картинки
music_img = pygame.image.load('music_fon.jpg').convert()  # картинка музыки
player = pygame.image.load('player.jpg').convert()  # картинка с кнопкой паузы
stop = pygame.image.load('player1.png').convert()  # с кнопкой игры музыки


#музыка
pygame.mixer.music.load('music.mp3')
song = ['music.mp3', 'game.mp3', 'melody.mp3'] #набор песен для перемотки


done = False
playing_state = False
cnt = 0


while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: #ENTER пуск
            screen.blit(player, (0, 300))  # вставить картинку с игрой музыки
            pygame.mixer.music.play()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT: #следующая музыка
            cnt -= 1
            if cnt < 0:
                cnt = len(song) - 1
            pygame.mixer.music.load(song[cnt])
            pygame.mixer.music.play()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT: #прошлая музыка
            cnt += 1
            if cnt > len(song) - 1:
                cnt = 0
            pygame.mixer.music.load(song[cnt])
            pygame.mixer.music.play()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #пробел стоп
            screen.blit(stop, (0, 300))  # вставить картинку с остановкой музыки
            pygame.mixer.music.stop()



    # показ на экране
    screen.blit(music_img, (0, 0)) # вставить картинку
    clock.tick(60)
    pygame.display.update()
pygame.quit()