# importing packages 
from pytube import YouTube, Playlist
from pydub import AudioSegment
from tqdm import tqdm
import os 

def download_playlist(url: str, num_tracks: int):
    # url input from user 
    p = Playlist(url)
    i = 0

    # extract only audio 
    for video in tqdm(p.videos, desc='Downloading', total=num_tracks):
        i += 1
        if i > num_tracks:
            break
        
        out_file = video.streams.filter(only_audio=True).first().download(output_path='audio')

        # save the file 
        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        os.rename(out_file, new_file) 

    # result of success 
    print("\n" + p.title + " has been successfully downloaded.\n")
    
# Function that takes the first 1 minute of each video in the playlist and saves it as an audio file
def crop_audio(in_path="audio", out_path="cropped_audio"):
    # create the directory if it does not exist
    if not os.path.exists(out_path):
        os.makedirs(out_path)
        
    # iterate over all files in the input directory
    for file in tqdm(os.listdir(in_path), desc="Cropping", total=len(os.listdir(in_path))):
        # get the file path
        file_path = os.path.join(in_path, file)
        
        # get the output file path
        out_file_path = os.path.join(out_path, file)
        
        # crop the audio file
        audio = AudioSegment.from_file(file_path)
        cropped_audio = audio[:30000]
        cropped_audio.export(out_file_path, format="mp3")

    print("\nAll files have been cropped successfully.\n")
    
# Function that collects all the audio files in the directory and merges them into a single audio file
def merge_audio(in_path="cropped_audio", out_path="merged_audio"):
    # create the directory if it does not exist
    if not os.path.exists(out_path):
        os.makedirs(out_path)
        
    # get the list of all audio files
    audio_files = [os.path.join(in_path, file) for file in os.listdir(in_path) if file.endswith(".mp3")]
    
    # get the output file path
    out_file_path = os.path.join(out_path, "klub100.mp3")
    
    # merge all audio files
    merged_audio = AudioSegment.empty()
    for audio_file in tqdm(audio_files, desc="Merging", total=len(audio_files)):
        audio = AudioSegment.from_file(audio_file)
        merged_audio += audio
        
    # export the merged audio file
    merged_audio.export(out_file_path, format="mp3")
    
    print("\nAll files have been merged successfully to file: klub100.mp3.\n")

if __name__ == '__main__':
    try:
        os.mkdir('audio')
        os.mkdir('cropped_audio')
        os.mkdir('merged_audio')
    except FileExistsError:
        pass
    
    try:
        # empty the directories
        for file in os.listdir('audio'):
            os.remove(os.path.join('audio', file))
        for file in os.listdir('cropped_audio'):
            os.remove(os.path.join('cropped_audio', file))
        for file in os.listdir('merged_audio'):
            os.remove(os.path.join('merged_audio', file))
    except FileNotFoundError:
        pass
    
    try:
        os.remove('klub100.mp3')
    except FileNotFoundError:
        pass
    
    # url of the playlist 
    url = input("Enter the URL of the youtube playlist: ")
    
    # check if the url is a youtube playlist
    if 'youtube' and 'playlist' not in url:
        print("Invalid URL. Please enter a valid youtube playlist URL.")
        exit()
    
    try:
        num_tracks = int(input("Enter the number of tracks to download: "))
    except ValueError:
        print("Invalid input. Deafaulting to 5 tracks.")
        num_tracks = 5
    
    download_playlist(url, num_tracks)
    crop_audio()
    merge_audio()