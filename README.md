# 🗣️ Text to Speech Application

A Python-based **Text-to-Speech (TTS) application** that converts written text into natural-sounding audio. This project demonstrates audio processing, NLP integration, and speech synthesis technologies.

## 📋 Overview

This application provides:
- 📝 **Text Input** - Convert any text to audio
- 🎵 **Multiple Voices** - Different speaker options
- ⚙️ **Customization** - Speed, pitch, and volume control
- 💾 **Export** - Save audio in various formats (MP3, WAV, OGG)
- 🌐 **Multi-language Support** - Support for multiple languages

## 🎯 Features

✅ **Multiple TTS Engines**
- Google Text-to-Speech
- pyttsx3 (Offline)
- gTTS (Google Translate TTS)

✅ **Voice Customization**
- Gender selection (Male/Female)
- Speed control
- Pitch adjustment
- Volume control

✅ **Audio Export**
- MP3 format
- WAV format
- OGG format
- Streaming playback

✅ **User Interface**
- Command-line interface
- Simple and intuitive
- Real-time preview

## 🛠️ Technologies Used

**Python Libraries:**
- `pyttsx3` - Offline text-to-speech
- `gTTS` - Google Translate TTS
- `pygame` or `pydub` - Audio playback
- `argparse` - CLI argument parsing

**Core Concepts:**
- Speech synthesis
- Audio processing
- NLP integration

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/Imran-Ali-Soomro/Text_to_Speech.git
cd Text_to_Speech

# Install dependencies
pip install -r requirements.txt

# For offline TTS (pyttsx3), additional setup may be needed:
# On Windows: No additional setup needed
# On Linux: sudo apt-get install espeak
# On macOS: brew install espeak
```

## 🚀 Quick Start

### Basic Usage

```bash
# Convert text to speech
python tts.py "Hello, this is a text to speech demonstration!"

# Save to file
python tts.py "Convert this text" --output output.mp3

# Adjust speed
python tts.py "Speed test" --speed 0.8  # Slower
python tts.py "Speed test" --speed 1.5  # Faster

# Change voice
python tts.py "Hello world" --voice female
```

### Advanced Usage

```python
from text_to_speech import TextToSpeech

# Initialize
tts = TextToSpeech(engine='google')  # or 'offline'

# Convert and play
tts.speak("Hello, world!")

# Convert and save
tts.speak_to_file("Your text here", "output.mp3", speed=1.2)

# Change settings
tts.set_voice('female')
tts.set_speed(1.0)
tts.set_pitch(1.2)
```

## 📁 Project Structure

```
Text_to_Speech/
├── tts.py                   # Main TTS module
├── cli.py                   # Command-line interface
├── engine/
│   ├── google_tts.py       # Google TTS engine
│   └── offline_tts.py      # Offline pyttsx3 engine
├── audio/
│   └── output/             # Generated audio files
├── requirements.txt        # Dependencies
└── README.md
```

## 📚 Supported Languages

- English (US, UK, Indian, Australian)
- Spanish
- French
- German
- Chinese (Mandarin, Cantonese)
- Japanese
- Korean
- And 50+ more languages

## ⚙️ Configuration

Edit `config.py` for default settings:

```python
DEFAULT_ENGINE = 'google'      # 'google' or 'offline'
DEFAULT_LANGUAGE = 'en'        # Language code
DEFAULT_VOICE = 'male'         # 'male' or 'female'
DEFAULT_SPEED = 1.0            # 0.5 (slow) to 2.0 (fast)
DEFAULT_PITCH = 1.0            # 0.5 to 2.0
OUTPUT_FORMAT = 'mp3'          # 'mp3', 'wav', 'ogg'
```

## 📊 Use Cases

🎓 **Education**
- Audiobook creation
- Learning aid for students
- Pronunciation guidance

♿ **Accessibility**
- Assistive technology
- Screen reader alternative
- Accessibility compliance

📻 **Media Production**
- Podcast generation
- Voice-over creation
- Advertisement production

🤖 **Automation**
- Automated announcements
- Notification systems
- Virtual assistant integration

## 🎵 Audio Quality

| Engine | Quality | Speed | Offline | Language Support |
|--------|---------|-------|---------|------------------|
| Google TTS | High | Fast | No | 50+ |
| pyttsx3 | Medium | Medium | Yes | 10+ |
| Custom Voice | Very High | Slow | Yes | Limited |

## 🐛 Troubleshooting

**Issue:** Audio not playing
```bash
pip install pygame
```

**Issue:** Google TTS connection error
```bash
# Check internet connection
# Use offline mode with pyttsx3
```

**Issue:** No voice output on Linux
```bash
sudo apt-get install espeak ffmpeg
```

## 📧 Contact & Support

For questions or suggestions:
- **Email:** isoomro179@gmail.com
- **GitHub:** [Imran-Ali-Soomro](https://github.com/Imran-Ali-Soomro)
- **Issues:** Open GitHub issues for bug reports

## 📝 License

Open source - Educational use.

---

**Transform your text into natural speech!** 🎤

*Last Updated: September 2026*
