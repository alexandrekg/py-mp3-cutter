from pydub import AudioSegment

# TODO: Create tests
def export(audio):
    _cut_audio(audio).export('audio.mp3', format="mp3")

# TODO: Create tests
def _cut_audio(audio):
    return _get_audio(audio)[audio.start_time:audio.end_time]

# TODO: Create tests
def _get_audio(audio):
    return AudioSegment.from_mp3(audio.audio_path)
