import os
import random


def split_and_append(b, s, k, first_list, second_list, third_list):
    # Initialize variables to keep track of the current index in each list
    first_index = 0
    second_index = 0
    third_index = 0
    playlist = []

    # Loop until we have processed all the segments
    while first_index < len(first_list) or second_index < len(second_list) or third_index < len(third_list):
        # Append b segments from the first list
        for i in range(b):
            if first_index >= len(first_list):
                break
            playlist.append(first_list[first_index])
            first_index += 1

        # Append s segments from the second list
        for i in range(s):
            if second_index >= len(second_list):
                break
            playlist.append(second_list[second_index])
            second_index += 1

        # Append k segments from the third list
        for i in range(k):
            if third_index >= len(third_list):
                break
            playlist.append(third_list[third_index])
            third_index += 1

    return playlist


def playlist_to_file(playlist_name, playlist):
    # Write the playlist to a file
    with open(playlist_name, 'w') as f:
        for audio_file in playlist:
            f.write(audio_file + '\n')


def audio_files_lists(bachata_dir, salsa_dir, kizomba_dir):
    # Get a list of all audio files in the bachata_dir
    audio_files_bachata = []
    audio_files_kizomba = []
    audio_files_salsa = []

    for file in os.listdir(bachata_dir):
        if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.ogg'):
            audio_files_bachata.append(os.path.join(bachata_dir, file))
    for file in os.listdir(salsa_dir):
        if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.ogg'):
            audio_files_salsa.append(os.path.join(salsa_dir, file))
    for file in os.listdir(kizomba_dir):
        if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.ogg'):
            audio_files_kizomba.append(os.path.join(kizomba_dir, file))

    random.shuffle(audio_files_bachata)
    random.shuffle(audio_files_salsa)
    random.shuffle(audio_files_kizomba)

    return audio_files_bachata, audio_files_salsa, audio_files_kizomba
