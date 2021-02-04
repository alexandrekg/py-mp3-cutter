import os
from conf import AUDIOS_TO_CUT_PATH
from pydub import AudioSegment

# TODO: Create tests
def _get_audio_file_name(audio_file):
    return audio_file.split('.')[0]

# TODO: Create tests
def _get_audios_to_cut_path(audio_file):
    audio_file_name = _get_audio_file_name(audio_file)

    return f'{os.path.dirname(os.path.abspath(__file__))}{AUDIOS_TO_CUT_PATH}{audio_file_name}.mp3'

# TODO: Create tests
def _get_extracted_song(audio_file):
    return AudioSegment.from_mp3(audio_file)

# TODO: Create tests
def _get_song(audio_file):
    audio_to_cut_path = _get_audios_to_cut_path(audio_file)
    return _extract_song(audio_to_cut_path)

# TODO: Create tests
def _convert_time_to_miliseconds(start_minutes, start_seconds, end_minutes, end_seconds):
    start_time = start_minutes * 60 * 1000 + start_seconds * 1000
    end_time = end_minutes * 60 * 1000 + end_minutes * 1000
    return start_time, end_time

def _export_song(audio):
    song = _get_song(audio)
    

audio = input('Type your audio file name: ')
start_minutes, start_seconds = input('Type your desired start_time: ').split(':')
end_minutes, end_seconds = input('Type your desired end_time: ').split(':')
print(start_minutes)