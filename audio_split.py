from pydub import AudioSegment
import math
import os

folder = "C:\\Users\Sergej\\Desktop\Projects\\emCounter\\audio"
output_folder = "C:\\Users\Sergej\\Desktop\Projects\\emCounter\\split_audio"




class SplitWavAudioMubin():
    def __init__(self, folder, filename, output_folder):
        self.folder = folder
        self.filename = filename
        self.filepath = os.path.join(folder, filename)
        self.output_folder = output_folder
        self.audio = AudioSegment.from_wav(self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(os.path.join(self.output_folder, split_filename), format="wav")
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = f'{i:0>2}' + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')


for file in os.listdir(folder):
    participant_dir = os.path.join(output_folder, os.path.splitext(file)[0])
    os.mkdir(participant_dir)
    split_wav = SplitWavAudioMubin(folder, file, participant_dir)
    split_wav.multiple_split(min_per_split=1)
