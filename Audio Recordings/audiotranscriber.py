import os
from io import BytesIO
import base64
import banana_dev as banana
from pydub import AudioSegment

api_key = "YOUR_API_KEY"
model_key = "YOUR_MODEL_KEY"

# Get the current working directory
rootDirectory = os.getcwd()
audioFolderName = 'Audio Recordings'

# If cwd ends with ReaperopolyProject, add the path to the audio recordings folder
if rootDirectory.endswith('ReaperopolyProject'):
    cwd = os.path.join(rootDirectory, audioFolderName)

print(cwd)

# Get the list of files in the current working directory, excluding this python file
files = [f for f in os.listdir(cwd) if f != 'audiotranscriber.py']

numFiles = len(files)
x = 0

for audioFile in files:
    try:
        x += 1
        # Get the full path to the audio file
        audioFilePath = os.path.join(cwd, audioFile)
        
        # Expects an mp3 file
        with open(audioFilePath, 'rb') as file:
            mp3bytes = BytesIO(file.read())
        mp3 = base64.b64encode(mp3bytes.getvalue()).decode("ISO-8859-1")

        model_payload = {"mp3BytesString": mp3}

        out = banana.run(api_key, model_key, model_payload)
        
        # print(out)

        text = out['modelOutputs'][0]['text']
        
        # Create a new text file with the same name as the audio file
        textFilePath = os.path.splitext(audioFilePath)[0] + '.txt'
        with open(textFilePath, 'w') as file:
            file.write(text)

        # Move audio file and text file to a new folder called 'Completed Audio Recordings and Transcriptions'
        completedFolderName = 'Completed Audio Recordings and Transcriptions'
        completedFolderPath = os.path.join(rootDirectory, completedFolderName)
        if not os.path.exists(completedFolderPath):
            os.makedirs(completedFolderPath)
        
        # Move audio file
        audioFileNewPath = os.path.join(completedFolderPath, audioFile)
        os.rename(audioFilePath, audioFileNewPath)

        # Move text file
        textFileNewPath = os.path.join(completedFolderPath, os.path.basename(textFilePath))
        os.rename(textFilePath, textFileNewPath)

        print(f'{x}/{numFiles} Complete - {audioFile} written to {textFilePath}')
    
    except Exception as e:
        print(e)
        # Move the audio file to the "Too Large Audio Recordings" folder
        tooLargeFolderName = 'Too Large Audio Recordings'
        tooLargeFolderPath = os.path.join(rootDirectory, tooLargeFolderName)
        audioFileNewPath = os.path.join(tooLargeFolderPath, audioFile)
        os.rename(audioFilePath, audioFileNewPath)
