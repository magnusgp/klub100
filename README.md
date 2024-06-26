# 🍻 Klub 100 🍻

## Overview

Welcome to the Klub 100 project! This tool is designed to help you create a custom audio file for your own Klub 100. The tool will download audio from a given YouTube link, crop the audio into 1-minute segments, and merge them into a single file with the specified number of tracks.

## Features

- **Easy Input**: Simply provide a YouTube link and the number of 1-minute tracks you want.
- **Automated Processing**: The tool automatically downloads, crops, and merges the audio.
- **Custom Output**: Create an audio file tailored to your preferences for the Klub 100.

## Prerequisites

- Python 3.x
- `pytube` library for downloading YouTube videos
- `pydub` library for audio processing
- `tqdm` library for progress bars

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/magnusgp/klub100.git
   cd klub100
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Script**

   ```bash
   python klub100.py
   ```

2. **Provide Input**

   When prompted, enter the YouTube link and the number of 1-minute tracks you want in the final audio file.

## Example

Here's an example of how to run the script:

```bash
python klub100.py
```

```
Enter the URL of the youtube playlist: https://youtube.com/playlist?list=PLDIoUOhQQPlXr63I_vwF9GD8sAKh77dWU&si=1ZFCsSiyjHmMfhm5
Enter the number of tracks to download: 100
```

This will create an audio file with 100 tracks, each 1 minute long, merged into a single file.

## Important Note

This guide assumes you'll use the following methods to download copyright-free material as well. **Do not use this information to infringe on any copyrights!** Always ensure that you have the right to download and use the content you are processing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to open an issue on the GitHub repository.

---

Cheers!