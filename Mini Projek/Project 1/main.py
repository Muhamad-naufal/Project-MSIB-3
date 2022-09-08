import speech_recognition as sr
engine = sr.Recognizer()
mic = sr.Microphone()
hasil = ''
engine.pause_threshold = 1

with mic as source:
    print("Perintah Anda....")
    rekaman = engine.listen(source)
    print("Kehabisan Waktu")

    try:
        hasil = engine.recognize_google(rekaman, language= "id-ID")
        print(hasil)
    except engine.UnknownValueError:
        print("Suara Tidak Terdeteksi, Coba Lagi")
    except Exception as e:
        print(e)

text_file = open("Hasil.txt", "w")
text_file.write(hasil)
text_file.close()