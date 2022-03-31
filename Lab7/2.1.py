#музыкальный плеер лучший вариант

import pygame, time
#import os

global play_button, next_button, prev_button, music

play_button_img = pygame.transform.scale(pygame.image.load('play.png'), (80,80))
pause_button_img = pygame.transform.scale(pygame.image.load('pause.png'), (80,80))
next_button_img = pygame.transform.scale(pygame.image.load('next.png'), (60,60))
prev_button_img = pygame.transform.scale(pygame.image.load('prev.png'), (60,60))

fon = pygame.transform.scale(pygame.image.load('fon.jpg'), (400, 500))

pygame.init()
SIZE = (400, 600)
screen = pygame.display.set_mode(SIZE)
FPS = 60
clock = pygame.time.Clock()
pygame.display.set_caption('MP3 Player')
#musics = []


music = {
    1: 'Imagine Dragons - Enemy (Feat. JID)', #название песни
    2: 'Meric Again - Industry Baby (feat. 22angels)',
    3: 'T3NZU - Balenciaga',
    4: 'Varien ft. Andrew Zink - Can You Feel My Heart'
}

"""
for i in os.listdir('C:\\Users\\annalar\Documents\\Unik\Piton\PP2_2022\Lab7\TheWeeknd'):
    music = pygame.mixer.Sound('C:\\Users\\annalar\Documents\\Unik\Piton\PP2_2022\Lab7\TheWeeknd\\' + str(i))
    musics.append(music)
"""

def player(num, in_pause, timestamp):
    if not in_pause:
        pygame.mixer_music.load('Music\\' + music[num] + '.mp3')
        pygame.mixer_music.play()
    else:
        pygame.mixer_music.play(start = timestamp)


def player_status(num): #названия выводить с авторами

    artist_name = music[num][:music[num].find('-') - 1]
    song_name = music[num][music[num].find('-') + 2:]

    font = pygame.font.SysFont('Verdana', 20)
    song_name_result = font.render(song_name, True, (255, 255, 255))
    screen.blit(song_name_result, (10, 410))

    font = pygame.font.SysFont('Verdana', 16)
    artist_name_result = font.render(artist_name, True, (255, 255, 255))
    screen.blit(artist_name_result, (10, 433))

    ramka = pygame.transform.scale(pygame.image.load('ramka.png'), (350, 350))
    screen.blit(ramka, (25, 45))


    #картинки под трек разные
    try:
        album_cover = pygame.transform.scale(pygame.image.load('images\\' + music[num] + '.jpg'), (300, 300))
    except FileNotFoundError:
        album_cover = pygame.transform.scale(pygame.image.load('images\\' + music[num] + '.png'), (300, 300))
    screen.blit(album_cover, (50, 70))

    pygame.draw.rect(screen, (255, 255, 255), (47, 67, 303, 303), 5)


def main():
    running = True
    is_playing = False
    n_of_track = 1
    paused = False
    alreade_played = False
    time_stamp = int()
    last_time_stamp = 0


    while running:

        #screen.fill((255, 215, 5))
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (0, 470, 400, 400))
        #play_button = screen.blit(play_button_img, (165, 487))

        if is_playing:
            play_button = screen.blit(pause_button_img, (165, 490))
        else:
            play_button = screen.blit(play_button_img, (165, 487))

        next_button = screen.blit(next_button_img, (265, 500))
        prev_button = screen.blit(prev_button_img, (85, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if play_button.collidepoint(x, y):
                    already_played = False
                    if is_playing:
                        is_playing = False
                        paused = True
                        pygame.mixer.music.stop()
                    else:
                        player(n_of_track, paused, time_stamp + last_time_stamp)
                        is_playing = True
                        last_time_stamp = time_stamp
                        start_ticks = pygame.time.get_ticks()
                elif next_button.collidepoint(x, y):
                    last_time_stamp = 0
                    is_playing = True
                    paused = False
                    n_of_track += 1
                    while n_of_track > len(music): n_of_track -= len(music)
                    player(n_of_track, paused, time_stamp + last_time_stamp)
                    start_ticks = pygame.time.get_ticks()
                elif prev_button.collidepoint(x, y):
                    last_time_stamp = 0
                    is_playing = True
                    paused = False
                    n_of_track -= 1
                    while n_of_track < 1: n_of_track = len(music)
                    player(n_of_track, paused, time_stamp + last_time_stamp)
                    start_ticks = pygame.time.get_ticks()

        if is_playing: time_stamp = (pygame.time.get_ticks() - start_ticks) / 1000


        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 400, 471), 3)
        pygame.draw.rect(screen, (0, 0, 0), (0, 470, 400, 597), 3)

        if is_playing or paused: player_status(n_of_track)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


main()