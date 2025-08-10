#!/usr/bin/env python3
"""
Simple script to play the generated jazz music
"""

import play

print("=== Playing Generated Jazz Music ===")
print("Playing test_output4.mid...")

try:
    play.play_midi('test_output4.mid')
    print("Music playback completed!")
except Exception as e:
    print(f"Error playing music: {e}")
    print("The generated MIDI file exists but couldn't be played.")
    print("You can manually open test_output4.mid in any MIDI player.")
