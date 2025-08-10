#!/usr/bin/env python3
"""
Convert MIDI to MP3 format
"""

import os
from pydub import AudioSegment
from pydub.playback import play
import subprocess

def convert_midi_to_mp3(midi_file, mp3_file):
    """Convert MIDI file to MP3 using timidity or fluidsynth"""
    
    # Check if timidity is available
    try:
        subprocess.run(['timidity', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        use_timidity = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        use_timidity = False
    
    # Check if fluidsynth is available
    try:
        subprocess.run(['fluidsynth', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        use_fluidsynth = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        use_fluidsynth = False
    
    if use_timidity:
        print("Using timidity for MIDI to WAV conversion...")
        # Convert MIDI to WAV using timidity
        wav_file = midi_file.replace('.mid', '.wav')
        subprocess.run(['timidity', midi_file, '-Ow', '-o', wav_file], check=True)
        
        # Convert WAV to MP3
        print("Converting WAV to MP3...")
        audio = AudioSegment.from_wav(wav_file)
        audio.export(mp3_file, format="mp3")
        
        # Clean up WAV file
        os.remove(wav_file)
        
    elif use_fluidsynth:
        print("Using fluidsynth for MIDI to WAV conversion...")
        # Convert MIDI to WAV using fluidsynth
        wav_file = midi_file.replace('.mid', '.wav')
        subprocess.run(['fluidsynth', '-ni', '/usr/share/sounds/sf2/FluidR3_GM.sf2', midi_file, '-F', wav_file, '-r', '44100'], check=True)
        
        # Convert WAV to MP3
        print("Converting WAV to MP3...")
        audio = AudioSegment.from_wav(wav_file)
        audio.export(mp3_file, format="mp3")
        
        # Clean up WAV file
        os.remove(wav_file)
        
    else:
        print("Neither timidity nor fluidsynth found. Installing timidity...")
        # Try to install timidity
        try:
            subprocess.run(['sudo', 'apt-get', 'update'], check=True)
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'timidity'], check=True)
            
            # Convert MIDI to WAV using timidity
            wav_file = midi_file.replace('.mid', '.wav')
            subprocess.run(['timidity', midi_file, '-Ow', '-o', wav_file], check=True)
            
            # Convert WAV to MP3
            audio = AudioSegment.from_wav(wav_file)
            audio.export(mp3_file, format="mp3")
            
            # Clean up WAV file
            os.remove(wav_file)
            
        except Exception as e:
            print(f"Error: {e}")
            print("Please install timidity or fluidsynth manually:")
            print("sudo apt-get install timidity")
            print("or")
            print("sudo apt-get install fluidsynth")

if __name__ == "__main__":
    midi_file = 'test_output4.mid'
    mp3_file = 'test_output4.mp3'
    
    print("=== MIDI to MP3 Conversion ===")
    print(f"Converting {midi_file} to {mp3_file}...")
    
    try:
        convert_midi_to_mp3(midi_file, mp3_file)
        print(f"Successfully converted {midi_file} to {mp3_file}")
        print("You can now play the MP3 file on any audio player!")
    except Exception as e:
        print(f"Conversion failed: {e}")
        print("The MIDI file test_output4.mid is available for manual conversion.")
