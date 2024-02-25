import pygame
import time

pygame.init()
pygame.mixer.init()
current_song = None

while True:
    number = int(input("Enter a number: "))
    
    if number < 60:
        filename = "master_of_puppets_metal.mp3"
    elif 60 <= number <= 100:
        filename = "staying_alive.mp3"
    else:
        filename = "take5_jazz.mp3"

    if filename != current_song:
        try:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            current_song = filename
        except pygame.error:
            print("Error: Couldn't play music")
