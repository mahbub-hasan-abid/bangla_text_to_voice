import pyttsx3
import os
from gtts import gTTS
from langdetect import detect

# Define paths
text_file = "text_input.txt"  # Text file containing input text
output_folder = "audio"  # Folder to save audio files

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Read text from file
try:
    with open(text_file, "r", encoding="utf-8") as file:
        text = file.read()

    # Detect language of the text
    try:
        detected_language = detect(text)
        print(f"Detected language: {detected_language}")

        # Initialize pyttsx3 engine
        engine = pyttsx3.init()

        # Ensure audio file path is defined before saving
        audio_file = os.path.join(output_folder, "output_audio.mp3")

        if detected_language == 'bn':
            try:
                # Use gTTS for Bengali
                print(f"Processing Bengali text: {text}")
                tts = gTTS(text=text, lang='bn', slow=False)
                tts.save(audio_file)
                print(f"Bengali audio saved to {audio_file}")
            except Exception as e:
                print(f"Error generating Bengali audio: {e}")
                print("Ensure the text is valid and gTTS supports the input.")
        elif detected_language == 'en':
            try:
                # Use gTTS for English with slower speech
                print(f"Processing English text: {text}")
                tts = gTTS(text=text, lang='en', slow=True)
                tts.save(audio_file)
                print(f"English audio saved to {audio_file}")
            except Exception as e:
                print(f"Error generating English audio: {e}")
        else:
            print(f"Unsupported language detected: {detected_language}. Defaulting to English.")
            try:
                # Default to English
                voices = engine.getProperty('voices')
                selected_voice = None
                for voice in voices:
                    if 'english' in voice.name.lower() or 'en' in voice.id.lower():
                        selected_voice = voice.id
                        break
                if selected_voice:
                    engine.setProperty('voice', selected_voice)
                else:
                    print("English voice not found. Using default voice.")

                engine.setProperty('rate', 200)  # Speed of speech
                engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
                engine.save_to_file(text, audio_file)
                engine.runAndWait()
                print(f"Default English audio saved to {audio_file}")
            except Exception as e:
                print(f"Error generating default English audio: {e}")
    except Exception as e:
        print(f"Error detecting language: {e}")
except Exception as e:
    print(f"Error: {e}")
