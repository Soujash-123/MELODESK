import pyaudio
import pygame
import wave
from pydub import AudioSegment

# Constants and variables
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
OUTPUT_FILENAME = "output.wav"
MUSIC_FILENAME = "background_music.mp3"
MERGED_FILENAME = "merged_output.mp3"

# Function to record audio
def record_audio():
    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    frames = []

    print("Recording started. Press Ctrl+C to stop recording.")

    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("Recording stopped.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    return frames

# Function to save audio to a WAV file
def save_audio(frames):
    audio = pyaudio.PyAudio()

    wave_file = wave.open(OUTPUT_FILENAME, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

    print("Audio saved to:", OUTPUT_FILENAME)

# Function to merge background music and recorded voice
def merge_audio(background_music, voice_recording):
    music = AudioSegment.from_file(background_music)
    voice = AudioSegment.from_file(voice_recording)

    merged_audio = music.overlay(voice)
    merged_audio.export(MERGED_FILENAME, format='mp3')

    print("Merged audio saved to:", MERGED_FILENAME)

# Initialize Pygame and load the background music
pygame.mixer.init()
pygame.mixer.music.load(MUSIC_FILENAME)

if __name__ == "__main__":
    try:
        pygame.mixer.music.play()
        audio_frames = record_audio()
        save_audio(audio_frames)
        merge_audio(MUSIC_FILENAME, OUTPUT_FILENAME)
    finally:
        pygame.mixer.music.stop()
