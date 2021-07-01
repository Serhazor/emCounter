import nltk
import os

input_folder = "C:\\Users\Sergej\\Desktop\Projects\\emCounter\\text"
output_folder = "C:\\Users\Sergej\\Desktop\Projects\\emCounter\\data"

for file in os.listdir(input_folder):
    with open (os.path.join(input_folder, file), "r") as participant_script:
        data = participant_script.read().replace('\n', ' ')

    data = data.split(' ')
    fdist1 = nltk.FreqDist(data)
    print (fdist1.most_common(100))

    with open(os.path.join(output_folder, os.path.splitext(file)[0]+'.csv'), "w") as data_file:
        for word, count in fdist1.most_common(100):
            if count > 3:
                data_file.write(f'{word},{count}\n')




