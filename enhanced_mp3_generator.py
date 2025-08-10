#!/usr/bin/env python3
"""
Enhanced Multi-Genre Music Generator with Direct MP3 Output
"""

import os
import sys
import numpy as np
import pickle
import random
import subprocess
from collections import defaultdict

# Import Keras components
try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import LSTM, Dense, Dropout, Input
    from tensorflow.keras.callbacks import ModelCheckpoint
    from tensorflow.keras.utils import to_categorical
except ImportError:
    from keras.models import Sequential
    from keras.layers import LSTM, Dense, Dropout, Input
    from keras.callbacks import ModelCheckpoint
    from keras.utils import to_categorical

from music21 import converter, instrument, note, chord, stream
from pydub import AudioSegment

class EnhancedMP3Generator:
    def __init__(self):
        self.genres = {
            'jazz': {
                'folder': 'Jazz',
                'characteristics': {
                    'tempo_range': (80, 160),
                    'scales': ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C#', 'F#', 'Bb', 'Eb', 'Ab'],
                    'chords': ['Cmaj7', 'Dm7', 'Em7', 'Fmaj7', 'G7', 'Am7', 'Bm7b5', 'C7', 'F7', 'Bb7', 'Eb7', 'Ab7'],
                    'rhythms': ['swing', 'bossa', 'bebop'],
                    'patterns': ['ii-V-I', 'blues', 'rhythm changes'],
                    'instruments': ['Piano', 'Bass', 'Drums', 'Saxophone', 'Trumpet'],
                    'complexity': 'high',
                    'syncopation': True,
                    'blue_notes': True
                }
            },
            'classical': {
                'folder': 'Classical',
                'characteristics': {
                    'tempo_range': (60, 180),
                    'scales': ['C', 'G', 'D', 'F', 'Bb', 'A', 'E', 'D'],
                    'chords': ['C', 'G', 'D', 'A', 'F', 'Bb', 'C', 'G', 'D', 'A'],
                    'rhythms': ['common time', 'waltz', 'march'],
                    'patterns': ['Alberti bass', 'arpeggios', 'counterpoint', 'canon'],
                    'instruments': ['Piano', 'Violin', 'Cello', 'Flute', 'Oboe'],
                    'complexity': 'medium',
                    'syncopation': False,
                    'ornaments': ['trill', 'mordent', 'grace note']
                }
            },
            'rock': {
                'folder': 'Rock',
                'characteristics': {
                    'tempo_range': (100, 180),
                    'scales': ['A', 'E', 'G', 'D', 'B', 'F#', 'C', 'G'],
                    'chords': ['A5', 'E5', 'D5', 'G5', 'C5', 'F5', 'Am', 'Em', 'Dm', 'G', 'C', 'F'],
                    'rhythms': ['4/4', 'shuffle', 'straight'],
                    'patterns': ['power chords', 'riffs', 'solos', 'verse-chorus'],
                    'instruments': ['Electric Guitar', 'Bass Guitar', 'Drums', 'Keyboard'],
                    'complexity': 'medium',
                    'distortion': True,
                    'power_chords': True
                }
            },
            'electronic': {
                'folder': 'Electronic',
                'characteristics': {
                    'tempo_range': (120, 160),
                    'scales': ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C#', 'D#', 'F#'],
                    'chords': ['Cm', 'Dm', 'Em', 'Fm', 'Gm', 'Am', 'Bm', 'Cmaj7', 'Dmaj7', 'Emaj7'],
                    'rhythms': ['4/4', 'syncopated', 'dotted'],
                    'patterns': ['arpeggios', 'pads', 'leads', 'basslines'],
                    'instruments': ['Synthesizer', 'Drum Machine', 'Bass', 'Pad'],
                    'complexity': 'high',
                    'synthesized': True,
                    'electronic': True
                }
            },
            'blues': {
                'folder': 'Blues',
                'characteristics': {
                    'tempo_range': (60, 120),
                    'scales': ['A', 'E', 'B', 'G', 'D', 'C', 'F', 'Bb'],
                    'chords': ['A7', 'D7', 'E7', 'B7', 'G7', 'C7', 'F7', 'Bb7', 'Eb7', 'Ab7'],
                    'rhythms': ['12/8', 'shuffle', 'swing'],
                    'patterns': ['12-bar blues', 'turnarounds', 'blue notes'],
                    'instruments': ['Piano', 'Guitar', 'Bass', 'Harmonica'],
                    'complexity': 'medium',
                    'blue_notes': True,
                    'bent_notes': True
                }
            },
            'pop': {
                'folder': 'Pop',
                'characteristics': {
                    'tempo_range': (90, 130),
                    'scales': ['C', 'G', 'D', 'A', 'F', 'Bb', 'E', 'B'],
                    'chords': ['C', 'G', 'D', 'A', 'F', 'Bb', 'Am', 'Em', 'Dm', 'Fmaj7', 'G7', 'Cmaj7'],
                    'rhythms': ['4/4', '2/4', 'waltz'],
                    'patterns': ['verse-chorus', 'bridge', 'hook', 'catchy melody'],
                    'instruments': ['Piano', 'Guitar', 'Bass', 'Drums'],
                    'complexity': 'low',
                    'catchy': True,
                    'simple': True
                }
            }
        }
        
        # Check for required dependencies
        self._check_dependencies()

    def _check_dependencies(self):
        """Check if required dependencies are available"""
        try:
            subprocess.run(['timidity', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.converter = 'timidity'
        except (subprocess.CalledProcessError, FileNotFoundError):
            try:
                subprocess.run(['fluidsynth', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.converter = 'fluidsynth'
            except (subprocess.CalledProcessError, FileNotFoundError):
                print("Warning: Neither timidity nor fluidsynth found. Please install one of them.")
                self.converter = None

    def create_genre_datasets(self):
        """Create comprehensive datasets for all genres"""
        print("Creating comprehensive genre datasets...")
        
        datasets = {}
        
        for genre, info in self.genres.items():
            print(f"Creating {genre} dataset...")
            dataset = self.create_genre_specific_dataset(genre, info)
            datasets[genre] = dataset
            
            # Save individual genre dataset
            os.makedirs(f'data/{genre}', exist_ok=True)
            with open(f'data/{genre}/dataset.pkl', 'wb') as f:
                pickle.dump(dataset, f)
        
        return datasets

    def create_genre_specific_dataset(self, genre, info):
        """Create dataset for a specific genre"""
        notes = []
        characteristics = info['characteristics']
        scales = characteristics['scales']
        chords = characteristics['chords']
        
        # Generate 1000 notes/chords for each genre
        for _ in range(1000):
            if random.random() < 0.7:
                notes.append(random.choice(scales))
            else:
                chord_notes = random.sample(scales, random.randint(2, 4))
                notes.append('.'.join(chord_notes))
        
        return {
            'notes': notes,
            'genre': genre,
            'characteristics': characteristics
        }

    def generate_music_for_genre(self, genre, length=200):
        """Generate music for a specific genre"""
        if genre not in self.genres:
            print(f"Genre '{genre}' not supported. Available genres: {list(self.genres.keys())}")
            return None
        
        print(f"Generating {genre} music...")
        
        info = self.genres[genre]
        characteristics = info['characteristics']
        
        notes = []
        scales = characteristics['scales']
        chords = characteristics['chords']
        
        for _ in range(length):
            if random.random() < 0.6:
                notes.append(random.choice(scales))
            else:
                chord_notes = random.sample(scales, random.randint(2, 4))
                notes.append('.'.join(chord_notes))
        
        return notes

    def create_mp3_file(self, notes, genre, filename=None):
        """Create MP3 file directly from generated notes"""
        if filename is None:
            filename = f"{genre}_generated.mp3"
        
        # First create MIDI file
        midi_filename = f"{genre}_temp.mid"
        self.create_midi_file(notes, genre, midi_filename)
        
        # Convert MIDI to MP3
        self.convert_midi_to_mp3(midi_filename, filename)
        
        # Clean up temporary MIDI file
        if os.path.exists(midi_filename):
            os.remove(midi_filename)
        
        return filename

    def create_midi_file(self, notes, genre, filename=None):
        """Create MIDI file from generated notes (internal use)"""
        if filename is None:
            filename = f"{genre}_generated.mid"
        
        offset = 0
        output_notes = []
        
        for pattern in notes:
            if ('.' in pattern) or pattern.isdigit():
                notes_in_chord = pattern.split('.')
                chord_notes = []
                for current_note in notes_in_chord:
                    try:
                        new_note = note.Note(int(current_note))
                    except ValueError:
                        new_note = note.Note(current_note)
                    new_note.storedInstrument = instrument.Piano()
                    chord_notes.append(new_note)
                new_chord = chord.Chord(chord_notes)
                new_chord.offset = offset
                output_notes.append(new_chord)
            else:
                new_note = note.Note(pattern)
                new_note.offset = offset
                new_note.storedInstrument = instrument.Piano()
                output_notes.append(new_note)
            
            offset += 0.5
        
        midi_stream = stream.Stream(output_notes)
        midi_stream.write('midi', fp=filename)
        
        return filename

    def convert_midi_to_mp3(self, midi_file, mp3_file):
        """Convert MIDI to MP3 using available tools"""
        if not self.converter:
            print("Error: No MIDI converter available. Please install timidity or fluidsynth.")
            return False
        
        try:
            if self.converter == 'timidity':
                print("Using timidity for MIDI to WAV conversion...")
                wav_file = midi_file.replace('.mid', '.wav')
                subprocess.run(['timidity', midi_file, '-Ow', '-o', wav_file], check=True)
                
                audio = AudioSegment.from_wav(wav_file)
                audio.export(mp3_file, format="mp3")
                os.remove(wav_file)
                
            elif self.converter == 'fluidsynth':
                print("Using fluidsynth for MIDI to WAV conversion...")
                wav_file = midi_file.replace('.mid', '.wav')
                subprocess.run(['fluidsynth', '-ni', '/usr/share/sounds/sf2/FluidR3_GM.sf2', 
                              midi_file, '-F', wav_file, '-r', '44100'], check=True)
                
                audio = AudioSegment.from_wav(wav_file)
                audio.export(mp3_file, format="mp3")
                os.remove(wav_file)
            
            return True
            
        except Exception as e:
            print(f"Error during conversion: {e}")
            return False

    def generate_all_genres_mp3(self):
        """Generate sample music for all available genres in MP3 format"""
        print("=== Generating MP3 Music for All Genres ===")
        
        generated_files = {}
        
        for genre in self.genres.keys():
            notes = self.generate_music_for_genre(genre)
            if notes:
                filename = self.create_mp3_file(notes, genre)
                generated_files[genre] = filename
                print(f"Generated {genre} music: {filename}")
        
        return generated_files

    def list_genres(self):
        """List all available music genres"""
        return list(self.genres.keys())

    def get_genre_info(self, genre):
        """Get detailed information about a genre"""
        if genre in self.genres:
            return self.genres[genre]
        return None

if __name__ == "__main__":
    generator = EnhancedMP3Generator()
    
    print("=== Enhanced Multi-Genre MP3 Music Generator ===")
    print("Available genres:", generator.list_genres())
    
    # Create datasets
    datasets = generator.create_genre_datasets()
    
    # Generate music for all genres
    generated_files = generator.generate_all_genres_mp3()
    
    print("\n=== Generated MP3 Files ===")
    for genre, filename in generated_files.items():
        print(f"{genre.title()}: {filename}")
    
    print("\nMulti-genre MP3 music generation complete!")
    print("You can now play the MP3 files on any audio player!")
