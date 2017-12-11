from gtts import gTTS

s = input("enter the text: \n")
tts = gTTS(text=s , lang= 'en', slow=True)
speech_name = input("enter the name of the speech file: \n")
tts.save(speech_name+'.mp3')
