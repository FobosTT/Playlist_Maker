import os
import random


class Music:

    playlist = []

    def __init__(self, directory, split_value, loop_index, music_list):
        self.directory = str(directory)
        self.split_value = int(split_value)
        self.loop_index = int(loop_index)
        self.music_list = music_list

    def split(self):
        for i in range(self.split_value):
            if self.loop_index >= len(self.music_list):
                break
            Music.playlist.append(self.music_list[self.loop_index])
            self.loop_index += 1

    def files(self):
        for file in os.listdir(self.directory):
            if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.ogg'):
                self.music_list.append(os.path.join(self.directory, file))
        random.shuffle(self.music_list)

    @staticmethod
    def playlist_to_file(playlist_name, playlist):
        # Write the playlist to a file
        with open(playlist_name, 'w') as f:
            for audio_file in playlist:
                f.write(audio_file + '\n')
