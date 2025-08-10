#!/usr/bin/env python3
"""
Music Generation Script - Run the Jazz Music Generation with Direct MP3 Output
"""

import sys
import os
from enhanced_mp3_generator import EnhancedMP3Generator

def main():
    print("=== Enhanced MP3 Music Generation with AI ===")
    
    generator = EnhancedMP3Generator()
    
    print("\nAvailable genres:", generator.list_genres())
    
    print("\n1. Generate music for all genres (MP3 format)")
    print("2. Generate music for specific genre (MP3 format)")
    print("3. List available genres")
    
    choice = input("\nEnter your choice (1/2/3): ").strip()
    
    if choice == "1":
        print("\n=== Generating MP3 music for all genres ===")
        generated_files = generator.generate_all_genres_mp3()
        
        print("\n=== Generated MP3 Files ===")
        for genre, filename in generated_files.items():
            print(f"{genre.title()}: {filename}")
            
    elif choice == "2":
        print("\nAvailable genres:", generator.list_genres())
        genre = input("Enter genre name: ").strip().lower()
        
        if genre in generator.list_genres():
            print(f"\n=== Generating {genre} music (MP3 format) ===")
            notes = generator.generate_music_for_genre(genre)
            if notes:
                filename = generator.create_mp3_file(notes, genre)
                print(f"Generated {genre} music: {filename}")
        else:
            print(f"Genre '{genre}' not supported.")
            
    elif choice == "3":
        print("\nAvailable genres:")
        for genre in generator.list_genres():
            info = generator.get_genre_info(genre)
            print(f"- {genre.title()}: {info['characteristics']['tempo_range'][0]}-{info['characteristics']['tempo_range'][1]} BPM")
            
    else:
        print("Invalid choice. Please run again.")

if __name__ == "__main__":
    main()
