import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def text_to_speech_to_file(text, filename):
    str_text = str(text)
    language = 'en'
    goog_speech = gTTS(str_text, lang=language, slow=False)
    goog_speech.save(filename)


def merge_audios(list_of_audio_files):
    combined_audio = AudioSegment.empty()
    for audio in list_of_audio_files:
        combined_audio += AudioSegment.from_mp3(audio)
    return combined_audio


def generate_fixed_audio_content():
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1 - kripya dheyan dijiye
    print("Extraction for - kripya dheyan dijiye ..")
    start = 88000
    finish = 90200
    audio_processed = audio[start:finish]
    audio_processed.export("1_hindi.mp3", format="mp3")

    # 2 - from city - to be filled dynamically

    # 3 -  se chalkar
    print("Extraction for - se chalkar ..")
    start = 91000
    finish = 92200
    audio_processed = audio[start:finish]
    audio_processed.export("3_hindi.mp3", format="mp3")

    # 4 - via city - to be filled dynamically

    # 5 - ke raaste
    print("Extraction for - se chalkar ..")
    start = 94000
    finish = 95000
    audio_processed = audio[start:finish]
    audio_processed.export("5_hindi.mp3", format="mp3")

    # 6 - to city - to be filled dynamically

    # 7 - ko jaane wali gaadi ki sankhya
    print("Extraction for - ko jaane wali gaadi ki sankhya ..")
    start = 96000
    finish = 98900
    audio_processed = audio[start:finish]
    audio_processed.export("7_hindi.mp3", format="mp3")

    # 8 - train number and name - to be filled dynamically

    # 9 - kuch hi samay me platform sankhya
    print("Extraction for - kuch hi samay me platform sankhya ..")
    start = 105500
    finish = 108200
    audio_processed = audio[start:finish]
    audio_processed.export("9_hindi.mp3", format="mp3")

    # 10 - platform number - to be filled dynamically

    # 11 - par aa rahi hei
    print("Extraction for - par aa rahi hei ..")
    start = 10900
    finish = 112250
    audio_processed = audio[start:finish]
    audio_processed.export("11_hindi.mp3", format="mp3")


def generate_dynamic_audio_content(filename):
    df = pd.read_excel(filename)
    print(df)
    for idx, items in df.iterrows():
        # 2 - from city
        print(f"processing for {items['from']}")
        text_to_speech_to_file(items['from'], "2_hindi.mp3")
        # 4 - via city
        text_to_speech_to_file(items['via'], "4_hindi.mp3")
        # 6 - to city
        text_to_speech_to_file(items['to'], "6_hindi.mp3")
        # 8 - train number and name
        text_to_speech_to_file(items['train_no'] + " " + items['train_name'], "8_hindi.mp3")
        # 10 - platform number
        text_to_speech_to_file(items['platform'], "10_hindi.mp3")

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]
        announcement = merge_audios(audios)
        announcement.export(f"announcement_{items['train_no']}_{idx + 1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generate static audio content")
    generate_fixed_audio_content()
    print("Generate dynamic audio content")
    generate_dynamic_audio_content("announce_hindi.xlsx")
