import speech_recognition as sr
import os

#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), '\\data\\')

AUDIO_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'split_audio')
TEXT_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'split_text')


for entry in os.listdir(AUDIO_FOLDER):
    #print(os.path.isdir(os.path.join(AUDIO_FOLDER, entry)))
    #print(entry)
    if os.path.isdir(os.path.join(AUDIO_FOLDER, entry)):
        participant_dir = os.path.join(TEXT_FOLDER, entry)
        print('+++')
        os.mkdir(participant_dir)
        
        for file in os.listdir(os.path.join(AUDIO_FOLDER, entry)):
            
            # use the audio file as the audio source
            r = sr.Recognizer()
            with sr.AudioFile(os.path.join(AUDIO_FOLDER, entry, file)) as source:
                audio = r.record(source)  # read the entire audio file

            # recognize speech using Google Speech Recognition
            try:
                file_text = r.recognize_google(audio)
                print("Google Speech Recognition thinks you said: " + file_text)
                output_file = open(os.path.join(participant_dir, os.path.splitext(file)[0] + '.txt' ), 'w')
                output_file.writelines(file_text)
                output_file.close()
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))



