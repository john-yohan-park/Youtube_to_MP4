# Youtube_to_MP4

Convert any youtube video to an mp4 file

## System Requirements
Name       | Terminal Command
---        | ---
Homebrew   | `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
Python 3   | `brew install python`
youtube_dl | `pip3 install youtube_dl` (download youtube video by URL)
libav      | `brew install libav` (strips audio from youtube videos)

## Instructions

Download multiple songs from list of URLs in `urls.txt`
- open `urls.txt`
- copy & paste URLs (1 per line)
- open Terminal
- cd into `Youtube-to-MP4` directory
- type `python3 downloader.py` in Terminal
- converted mp4 files are in `Videos` directory

https://github.com/john-yohan-park/Youtube_to_MP4
