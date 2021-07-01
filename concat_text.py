import os

FINAL_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'text')

TEXT_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'split_text')


for entry in os.listdir(TEXT_FOLDER):
    #print(os.path.isdir(os.path.join(AUDIO_FOLDER, entry)))
    #print(entry)
    if os.path.isdir(os.path.join(TEXT_FOLDER, entry)):
        test_arr = []
              
        for file in os.listdir(os.path.join(TEXT_FOLDER, entry)):
            test_arr.append(file)
        #print('added not sorted ' + str(test_arr)) 
        test_arr.sort()
        #print('sorted ' + str(test_arr)) 
        output_file = open(os.path.join(FINAL_FOLDER, entry + '.txt'), 'w')

        for each in test_arr:

            input_file = open(os.path.join(TEXT_FOLDER, entry, each), 'r')
            lines = input_file.readlines()
            input_file.close()
            output_file.writelines(lines)
            output_file.write(' ')

        output_file.close()
            