#import library speech_recognition
import speech_recognition as sr

#pendefinisian
engine = sr.Recognizer()
mic = sr.Microphone()
hasil = ''
engine.pause_threshold = 0.5

#input dan proses
with mic as source:
    #inputan
    print("Perintah Anda....")
    rekaman = engine.listen(source)
    print("Kehabisan Waktu")

    #proses
    try:
        hasil = engine.recognize_google(rekaman, language= "id-ID")
        print(hasil)
    except engine.UnknownValueError:
        print("Suara Tidak Terdeteksi, Coba Lagi")
    except Exception as e:
        print(e)

#output
text_file = open("Hasil.txt", "w")
text_file.write(hasil)
text_file.close()