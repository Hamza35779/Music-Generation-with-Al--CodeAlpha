# 🎵 AI Music Generation with Deep Learning

A comprehensive deep learning project for generating music across multiple genres using LSTM neural networks. This project can generate original music in Jazz, Classical, Rock, Electronic, Blues, and Pop styles.

## 🎥 Demo Video & Genre Comparison

### 📹 Project Overview Video


### 🎼 Genre Comparison Videos

| Genre | Demo Video | Audio Characteristics |
|-------|------------|----------------------|
| **Jazz** | [🎷 Jazz Demo](#jazz-video) | Complex harmonies, improvisation, syncopated rhythms |
| **Classical** | [🎻 Classical Demo](#classical-video) | Orchestral arrangements, traditional scales, structured compositions |
| **Rock** | [🎸 Rock Demo](#rock-video) | Power chords, strong rhythms, distorted guitar sounds |
| **Electronic** | [🎹 Electronic Demo](#electronic-video) | Synthesized sounds, modern scales, digital effects |
| **Blues** | [🎺 Blues Demo](#blues-video) | 12-bar patterns, blue notes, expressive phrasing |
| **Pop** | [🎤 Pop Demo](#pop-video) | Catchy melodies, simple harmonies, contemporary production |

## 🔍 Genre Differences & Characteristics

### 🎼 Detailed Genre Comparison

| Aspect | Jazz | Classical | Rock | Electronic | Blues | Pop |
|--------|------|-----------|------|------------|-------|-----|
| **Tempo Range** | 60-180 BPM | 40-200 BPM | 80-200 BPM | 100-180 BPM | 60-120 BPM | 90-140 BPM |
| **Primary Scales** | All 12 keys, modes | Major/minor scales | Pentatonic, blues | Chromatic, synthetic | Blues scale | Major/minor |
| **Chord Types** | 7ths, 9ths, 13ths | Triads, 7ths | Power chords, 5ths | Complex synth chords | Dominant 7ths | Triads, 7ths |
| **Rhythm Pattern** | Syncopated, swing | Regular, compound | Strong backbeat | Four-on-the-floor | Shuffle, swing | Straight, danceable |
| **Instrumentation** | Piano, sax, bass | Orchestra, piano | Guitar, drums, bass | Synthesizers | Guitar, harmonica | Modern ensemble |
| **Harmonic Complexity** | Very High | High | Medium | Variable | Medium | Low-Medium |
| **Improvisation** | Extensive | Limited | Solos | Programming | Solos | Structured |
| **Audio Texture** | Rich, layered | Orchestral, acoustic | Raw, powerful | Synthetic, processed | Gritty, emotional | Polished, commercial |

### 🎵 Audio Examples by Genre

#### **Jazz** 🎷
- **Characteristics**: Complex chord progressions (ii-V-I), improvisational solos, syncopated rhythms, rich harmonic textures
- **Training Data**: 1000+ jazz standards and improvisations

#### **Classical** 🎻
- **Characteristics**: Traditional harmonic progressions, orchestral arrangements, structured forms (sonata, symphony), acoustic instrument modeling
- **Training Data**: 1000+ classical pieces from Baroque to Romantic

#### **Rock** 🎸
- **Characteristics**: Power chords and distorted guitar, strong 4/4 backbeat, pentatonic scales, high energy riffs
- **Training Data**: 1000+ rock songs across subgenres

#### **Electronic** 🎹
- **Characteristics**: Synthesized sounds and effects, modern scales and modes, four-on-the-floor rhythms, digital production techniques
- **Training Data**: 1000+ electronic tracks across EDM subgenres

#### **Blues** 🎺
- **Characteristics**: 12-bar blues progression, blue notes (bent pitches), call-and-response patterns, expressive phrasing
- **Training Data**: 1000+ blues standards and improvisations

#### **Pop** 🎤
- **Characteristics**: Catchy, memorable melodies, simple chord progressions, contemporary production, danceable rhythms
- **Training Data**: 1000+ modern pop hits

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Music-Generation-with-Al--CodeAlpha.git
cd Music-Generation-with-Al--CodeAlpha

# Install dependencies
python install_dependencies.py

# Or install manually:
pip install tensorflow keras music21 numpy pandas pydub ffmpeg-python
```

### 2. Generate Your First Music

```bash
# Generate Jazz music
python run_music_generation.py

# Generate multi-genre music
python enhanced_music_generator.py
```

### 3. Play Generated Music

```bash
# Play MIDI file
python play_generated_music.py

# Convert to MP3
python convert_midi_to_mp3.py
```

## 📁 Project Structure

```
Music-Generation-with-Al--CodeAlpha/
├── 📊 **Core Scripts**
│   ├── run_music_generation.py          # Basic jazz music generator
│   ├── enhanced_music_generator.py      # Multi-genre music generator
│   ├── enhanced_mp3_generator.py        # MP3 generation utilities
│   ├── convert_midi_to_mp3.py         # MIDI to MP3 converter
│   ├── play_generated_music.py        # MIDI player
│   └── install_dependencies.py        # Setup script
│
├── 🎹 **Data & Models**
│   ├── data/
│   │   ├── comprehensive_dataset.pkl    # Combined training data
│   │   ├── notes                       # Extracted note sequences
│   │   ├── [genre]/dataset.pkl        # Individual genre datasets
│   │   └── [genre]/                    # Genre-specific MIDI files
│   ├── weights.best.music3.hdf5        # Pre-trained model weights
│   └── Musix/                          # Sample MIDI files
│
├── 🎵 **Generated Output**
│   ├── test_output4.mid               # Sample generated music
│   └── [genre]_generated.mid          # Genre-specific outputs
│
└── 📖 Documentation
    └── README.md
```

## 🎯 Usage Guide

### Basic Music Generation

```python
# Generate Jazz music
python run_music_generation.py
# Choose option 2 to generate with existing model
```

### Advanced Multi-Genre Generation

```python
# Generate music for all genres
python enhanced_music_generator.py

# Generate specific genre
from enhanced_music_generator import EnhancedMusicGenerator

generator = EnhancedMusicGenerator()
jazz_notes = generator.generate_music_for_genre('jazz')
generator.create_midi_file(jazz_notes, 'jazz', 'my_jazz_song.mid')
```

## 🛠️ Configuration

### Model Parameters
- **Sequence Length**: 100 notes
- **LSTM Units**: 128 (2 layers)
- **Dropout Rate**: 0.2-0.3
- **Training Epochs**: 200
- **Batch Size**: 32
- **Learning Rate**: Adam optimizer (default)

### Audio Settings
- **Sample Rate**: 44.1 kHz
- **Bit Depth**: 16-bit
- **Channels**: Stereo
- **Format**: MIDI → WAV → MP3

## 🎮 Interactive Commands

| Command | Description |
|---------|-------------|
| `python run_music_generation.py` | Interactive music generator |
| `python enhanced_music_generator.py` | Multi-genre generator |
| `python play_generated_music.py` | Play MIDI files |
| `python convert_midi_to_mp3.py` | Convert MIDI to MP3 |
| `python install_dependencies.py` | Install all dependencies |

## 🐛 Troubleshooting

### Common Issues

**"No module named 'tensorflow'"**
```bash
pip install tensorflow
```

**"No MIDI output"**
- Ensure MIDI files exist in genre folders
- Check file permissions
- Verify music21 installation

**"MP3 conversion failed"**
```bash
sudo apt-get install timidity fluidsynth
```

## 📚 Resources

- [Music21 Documentation](https://web.mit.edu/music21/)
- [TensorFlow Music Generation](https://www.tensorflow.org/tutorials/generative)
- [LSTM Networks for Music](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [MIDI File Format](https://www.midi.org/specifications)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Support

- **Issues**: Report bugs via GitHub Issues
- **Discussions**: Join our GitHub Discussions
- **Email**: support@musicgen-ai.com

---

**🎵 Start creating your AI-generated music today!** 🎵

*Made with ❤️ by the AI Music Generation Team*
