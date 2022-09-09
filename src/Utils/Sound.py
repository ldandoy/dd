
import pygame
import os

class Sound:

    @staticmethod
    def play(base_folder, audio_name, channel=0, volume=0.5):
        name = audio_name if len(audio_name.split(".")) > 1 else audio_name + ".wav"
        pygame.mixer.Channel(channel).set_volume(volume)
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(os.path.join(base_folder, '../medias/audio/'+ name)))

    @staticmethod
    def background(base_folder, audio_name="epic.ogg"):
        pygame.mixer.music.set_volume(0)
        pygame.mixer.music.load(os.path.join(base_folder, '../medias/audio/'+ audio_name))
        pygame.mixer.music.play(loops=0)

    @staticmethod
    def stopBackground():
        pygame.mixer.music.stop()