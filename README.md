# Audio Mashup Project

This project combines audio mashup creation and video processing functionalities, enabling users to process YouTube videos and compile customized audio mashups. The application supports downloading videos, converting them to audio, trimming clips, merging audio files, and emailing the final output.



## Features
- **Download Videos:** Fetch YouTube videos based on a singer’s name or keyword search.
- **Convert to Audio:** Extract audio tracks from downloaded videos.
- **Trim Audio:** Cut audio clips to a specified duration.
- **Merge Clips:** Combine trimmed audio clips into a single MP3 file.
- **Email Output:** Zip and email the final output to a specified email address.

## Requirements
Ensure the following are installed:
- **Python 3.x**
- Required Python libraries:
  - Flask
  - requests
  - pandas
  - matplotlib
  - scikit-learn
  - pytube
  - pydub
  - moviepy

Install the required libraries using:
```bash
pip install flask requests pandas matplotlib scikit-learn pytube pydub moviepy
```

## Setup
1. Clone or download this repository to your local machine.
2. Navigate to the project directory:
   ```bash
   cd path/to/project_directory
   ```
3. Ensure all scripts (e.g., `change.py`, `cutter.py`, `downloader.py`, `Merger.py`) are present in the same directory.

## Usage
### Using the Flask Application
1. **Run the Flask App:**
   ```bash
   python app.py
   ```
2. **Open Your Browser:**
   Navigate to `http://127.0.0.1:5000/` to access the input form.
3. **Fill Out the Form:** Provide the following details:
   - **Singer Name:** Name of the singer or a keyword for video search.
   - **Number of Videos:** Number of videos to process.
   - **Duration:** Duration (in seconds) for trimming each audio clip.
   - **Output File Name:** Name of the merged audio output file.
   - **Email ID:** Email address to send the final zipped output.
4. **Submit the Form:** Click "Submit" to start processing.

### Using the Mashup Script Directly
1. **Run the Script:**
   ```bash
   python youtube_mashup.py
   ```
2. **Provide Inputs:**
   - **Keyword:** A search term (e.g., "Lo-fi music").
   - **Number of Videos:** Number of videos to process (e.g., 5).
   - **Trim Duration:** Duration to trim from the start of each audio clip (e.g., 30 seconds).
   - **Output File Name:** Name of the final output file (e.g., "lofi_mashup").

## How It Works
1. User inputs are collected via a web form or directly through the script.
2. The `main.py` script orchestrates the execution of other scripts:
   - `downloadder.py`: Downloads YouTube videos.
   - `Converterr.py`: Converts videos to audio.
   - `cutter.py`: Trims audio clips to the specified duration.
   - `Merger.py`: Merges trimmed audio clips into a single file.
   - `zipsend.py`: Zips the final output and emails it to the user.

## Outputs
- The final audio mashup is saved as an MP3 file (e.g., `lofi_mashup.mp3`).
- A zipped folder containing the audio file is emailed to the user if an email is provided.

## Contributing
Contributions are welcome! If you'd like to enhance the project, feel free to submit a pull request or open an issue for discussion.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

