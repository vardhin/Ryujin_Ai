from pydub import generators, playback

# Function to generate a note with a given frequency and duration
def generate_note(frequency, duration_ms):
    # Generate a sine wave with the specified frequency
    sine_wave = generators.Sine(frequency)
    # Generate the audio segment for the note
    note_segment = sine_wave.to_audio_segment(duration=duration_ms)
    return note_segment

# Function to play a sequence of notes
def play_music(notes):
    # Concatenate the notes to form the music sequence
    music_sequence = sum(notes)
    # Play the music sequence
    playback.play(music_sequence)

# Dictionary mapping note names to frequencies (for simplicity, we'll use equal temperament tuning)
notes_freq = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88
}

# Example music notes sequence
music_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Duration of each note in milliseconds
note_duration = 500  # 0.5 seconds per note

# Generate notes based on the music sequence
generated_notes = [generate_note(notes_freq[note], note_duration) for note in music_notes]

# Play the generated music
while True:
    play_music(generated_notes)
