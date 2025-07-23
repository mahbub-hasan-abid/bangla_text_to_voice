import openpyxl
import pyttsx3
import os
from gtts import gTTS
import tempfile

# Define paths
excel_file = r"F:\BdApps\Bd apps\Book1.xlsx"  # Replace with your Excel file path
output_folder = r"F:\BdApps\New folder (2)"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize pyttsx3 engine for baby voice effect
def create_baby_voice_audio(text, output_path):
    """
    Create baby voice audio using pyttsx3 with higher pitch and faster speed
    """
    try:
        # Initialize text-to-speech engine
        engine = pyttsx3.init()
        
        # Get available voices
        voices = engine.getProperty('voices')
        
        # Try to find a female voice (usually sounds more baby-like)
        female_voice = None
        for voice in voices:
            if 'female' in voice.name.lower() or 'woman' in voice.name.lower():
                female_voice = voice.id
                break
        
        # Set voice properties for baby-like sound
        if female_voice:
            engine.setProperty('voice', female_voice)
        
        # Set speech rate (words per minute) - faster for baby-like speech
        engine.setProperty('rate', 220)  # Default is usually 200, increase for baby voice
        
        # Set volume (0.0 to 1.0)
        engine.setProperty('volume', 0.9)
        
        # Save to file
        engine.save_to_file(text, output_path)
        engine.runAndWait()
        
        return True
        
    except Exception as e:
        print(f"Error in pyttsx3 baby voice processing: {e}")
        # Fallback to gTTS if pyttsx3 fails
        try:
            tts = gTTS(text=text, lang='bn', slow=False)  # Use fast speech for baby-like effect
            tts.save(output_path)
            return True
        except Exception as fallback_error:
            print(f"Fallback gTTS also failed: {fallback_error}")
            return False

# Load Excel file
try:
    wb = openpyxl.load_workbook(excel_file)
    sheet = wb.active  # Use active sheet; change to wb['SheetName'] for specific sheet

    # Iterate through each cell in the used range
    for row in sheet.iter_rows():
        for cell in row:
            if cell.value:  # Skip empty cells
                try:
                    text = str(cell.value)
                    # Define audio file path using cell coordinates
                    audio_file = os.path.join(output_folder, f"baby_voice_cell_{cell.coordinate}.mp3")
                    
                    # Generate baby voice audio
                    if create_baby_voice_audio(text, audio_file):
                        print(f"Saved baby voice audio for cell {cell.coordinate} to {audio_file}")
                    else:
                        print(f"Failed to create baby voice for cell {cell.coordinate}")
                        
                except Exception as e:
                    print(f"Error processing cell {cell.coordinate}: {e}")
except Exception as e:
    print(f"Error loading Excel file: {e}")