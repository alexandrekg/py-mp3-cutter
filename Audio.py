import os
from conf import AUDIOS_TO_CUT_PATH

class Audio:
    def __init__(self, audio_name, start_minutes, start_seconds, end_minutes, end_seconds):
        self.audio_name = audio_name
        self.start_minutes = int(start_minutes)
        self.start_seconds = int(start_seconds)
        self.end_minutes = int(end_minutes)
        self.end_seconds = int(end_seconds)

    # TODO: Create tests
    def _parse_audio_name(self):
        return self.audio_name.split('.')[0]

    # TODO: Create tests
    @property
    def audio_path(self):
        return f'{os.path.dirname(os.path.abspath(__file__))}{AUDIOS_TO_CUT_PATH}{self._parse_audio_name()}.mp3'

    # TODO: Create tests
    @property
    def start_time(self):
        return self.start_minutes * 60 * 1000 + self.start_seconds * 1000

    # TODO: Create tests
    @property
    def end_time(self):
        return self.end_minutes * 60 * 1000 + self.end_seconds * 1000

    # TODO: Create tests
    @property
    def save_path(self):
        return f'{os.path.dirname(os.path.abspath(__file__))}{AUDIOS_TO_CUT_PATH}'
