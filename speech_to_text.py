import speech_recognition as sr

r=sr.Recognizer()

audio = sr.AudioFile(r'D:\Python kurs\Project\record_out.wav')

with audio as source:
    audio = r.record(source)                  
    result = r.recognize_google(audio, language='sr_SR')
    
    
print(result)