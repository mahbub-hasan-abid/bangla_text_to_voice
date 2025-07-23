import openpyxl
from gtts import gTTS
import os

# Define paths
excel_file = r"F:\BdApps\Bd apps\Book1.xlsx"  # Replace with your Excel file path
output_folder = r"F:\BdApps\New folder (2)"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

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
                    # Generate audio in Bengali
                    tts = gTTS(text=text, lang='bn')  # Use 'bn' for Bengali
                    # Define audio file path using cell coordinates
                    audio_file = os.path.join(output_folder, f"cell_{cell.coordinate}.mp3")
                    # Save audio file
                    tts.save(audio_file)
                    print(f"Saved audio for cell {cell.coordinate} to {audio_file}")
                except Exception as e:
                    print(f"Error processing cell {cell.coordinate}: {e}")
except Exception as e:
    print(f"Error loading Excel file: {e}")