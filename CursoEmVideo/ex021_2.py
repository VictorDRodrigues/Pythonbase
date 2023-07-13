import pygame

pygame.init()

# Inicializa o mixer de áudio
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load('C:\Games/tralala.mp3')

# Reproduz o arquivo MP3
pygame.mixer.music.play()

# Mantém o programa em execução enquanto a música está sendo reproduzida
while pygame.mixer.music.get_busy():
    pass

# Encerra a reprodução do áudio
pygame.mixer.music.stop()

# Encerra o pygame
pygame.quit()