import speech_recognition as sr
from pydub import AudioSegment, utils
import time
import os
import os
import openai

def convert_to_wav(input_file, output_file):
    sound = AudioSegment.from_mp3(input_file)
    sound.export(output_file, format='wav')

def recognize_speech(audio_file, language='sr_SR'):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)                  
        result = r.recognize_google(audio, language=language)
    return result

def get_prober_name():
    return r'D:\Python kurs\Project\ffprobe.exe'

def get_response(prompt):
    
    openai.api_key = os.getenv("OPENAI_API_KEY")


    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are my personal assistant: I have one message with grammatical and punctuation mark mistakes in Serbian.\
              Please correct them and you always write messages like you are me and in Serbian" },
            
            {"role": "user", "content": prompt}
        ]
    )

    text=response.choices[0].message.content
    print(text)


#Ovaj input fajl je glasovna poruka koja bi se preuzela, a nakon konverzije izbrisala iz os, to treba dodati nakon implementaacije tog dijela
input_file = 'Ćao kako si Šta radi.mp3'
output_file = f'Record_{time.strftime("%Y-%m-%d_%H-%M-%S")}.wav'

#Potrebno preuzeti ffmpeg-master-latest-win64-gpl.zip sa https://github.com/BtbN/FFmpeg-Builds/releases
AudioSegment.converter=r'D:\Python kurs\Project\ffmpeg.exe'
utils.get_prober_name = get_prober_name

convert_to_wav(input_file, output_file)
result = recognize_speech(output_file)

os.remove(output_file)

print(result)
prompt = result

get_response(prompt)
