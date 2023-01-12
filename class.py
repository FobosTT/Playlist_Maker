class Music:

    playlist = []

    def __init__(self):
        self.directory = ''
        self.split_value = 1
        self.loop_index = 0
        self.list = []

    
    def split(self):
        for i in range(self.split_value):
            if self.loop_index >= len(self.list):
                break
            playlist.append(self.list[self.loop_index])
            self.loop_index += 1


    def files(self):
        for file in os.listdir(self.directory):
            if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.ogg'):
               self.list.append(os.path.join(self.directory, file))
        random.shuffle(self.list)