import pygame
import os

class MusicPlayer:
    def __init__(self, folder_name):
        pygame.mixer.init()
        base_path = os.path.dirname(__file__)
        self.music_folder = os.path.join(base_path, folder_name)
        self.playlist = self.load_tracks()
        self.index = 0
        self.is_playing = False
    def load_tracks(self):
        files = []
        if not os.path.exists(self.music_folder):
            print(f"Ошибка: Папка не найдена по пути {self.music_folder}")
            return files
        for f in os.listdir(self.music_folder):
            if f.endswith((".mp3", ".wav")):
                files.append(os.path.join(self.music_folder, f))
        return files
    def load_current(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.index])
    def play(self):
        if not self.playlist:
            print("Плейлист пуст!")
            return
        if not self.is_playing:
            self.load_current()
            pygame.mixer.music.play()
            self.is_playing = True
        else:
            pygame.mixer.music.unpause()
            self.is_playing = True
    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
    def pause(self):
        pygame.mixer.music.pause()
        self.is_playing = False
    def next(self):
        if self.playlist:
            self.index = (self.index + 1) % len(self.playlist)
            self.load_current()
            pygame.mixer.music.play()
            self.is_playing = True
    def previous(self):
        if self.playlist:
            self.index = (self.index - 1) % len(self.playlist)
            self.load_current()
            pygame.mixer.music.play()
            self.is_playing = True
    def get_current_track(self):
        if self.playlist:
            return os.path.basename(self.playlist[self.index])
        return "Нет треков"
    def get_pos(self):
        return pygame.mixer.music.get_pos() // 1000