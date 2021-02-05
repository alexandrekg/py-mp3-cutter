from Audio import Audio
from services.audio_service import export

if __name__ == "__main__":
    audio_name = input('Type your audio file name: ')
    start_minutes, start_seconds = input('Type your desired start_time: ').split(':')
    end_minutes, end_seconds = input('Type your desired end_time: ').split(':')

    audio = Audio(audio_name, start_minutes, start_seconds, end_minutes, end_seconds)
    export(audio)
