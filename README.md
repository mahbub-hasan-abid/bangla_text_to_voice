# Bangla Text to Voice Script

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Text to Voice](#text-to-voice)
  - [Excel Sheet to Voice](#excel-sheet-to-voice)
  - [Renaming Files](#renaming-files)
- [Example](#example)
  - [Text Input Example](#text-input-example)
  - [Excel Input Example](#excel-input-example)
  - [Renaming Files Example](#renaming-files-example)
- [License](#license)
- [Author](#author)
- [Contact](#contact)

## Overview

This project allows users to convert text into audio files in Bengali or English. Users can choose to generate a single audio file for the entire text or separate audio files for each line. The script automatically detects the language of the text and generates the corresponding voice. Additionally, the project supports converting Excel sheets to voice and renaming audio files sequentially.

## Features

- Automatic language detection (Bengali or English).
- Option to generate a single audio file or separate audio files for each line.
- Supports child-like voice for English.
- Ensures unique file names to avoid overwriting.
- Renames all audio files sequentially.
- Converts Excel sheets to voice.

## Requirements

- Python 3.x
- Required Python libraries:

  - `pyttsx3`
  - `gtts`
  - `langdetect`
  - `pandas`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mahbub-hasan-abid/bangla_text_to_voice_script.git
   ```

2. Navigate to the project directory:

   ```bash
   cd bangla_text_to_voice_script
   ```

3. Install the required Python libraries:

   ```bash
   pip install pyttsx3 gtts langdetect pandas
   ```

## Usage

### Text to Voice

1. Open the `text_input.txt` file and enter the text you want to convert to audio.

2. Run the script:

   ```bash
   python text_to_voice.py
   ```

3. Select the mode:

   - `single`: Generates one audio file for the entire text.
   - `separate`: Generates individual audio files for each line.

### Excel Sheet to Voice

1. Prepare an Excel sheet with text data in one column.

2. Run the script:

   ```bash
   python excel_to_voice.py
   ```

3. The script will generate audio files for each row in the Excel sheet.

### Renaming Files

1. Run the renaming script:

   ```bash
   python rename_files.py
   ```

2. The script will rename all audio files sequentially.

## Example

### Text Input Example

#### Text Input

`text_input.txt`:

```plaintext
Hello, this is a test.
This is the second line.
```

#### Text Output

- In `single` mode: One audio file named `output_audio.mp3`.
- In `separate` mode: Two audio files named `line_1.mp3` and `line_2.mp3`.

### Excel Input Example

#### Excel Input

`text_input.xlsx`:

| Text       |
|------------|
| Hello, this is a test. |
| This is the second line. |

#### Excel Output

- Two audio files named `row_1.mp3` and `row_2.mp3`.

### Renaming Files Example

#### Renaming Input

Audio files:

- `row_1.mp3`
- `row_2.mp3`

#### Renaming Output

Renamed files:

- `audio_1.mp3`
- `audio_2.mp3`

## License

This project is licensed under the MIT License.

## Author

Mahbub Hasan Abid

## Contact

For any complications or issues, please contact:

Name: Mahbub Hasan Abid       
Email: [mahbubhasanabid00@gmail.com](mailto:mahbubhasanabid00@gmail.com)
