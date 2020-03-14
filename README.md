# Youtube_to_MP3_Converter

Written in Python

## Introduction
Convert youtube videos to mp4 files

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
- cd into `youtube-to-mp4` directory
- type `python3 downloader.py` in Terminal
- converted mp3 files are in `Videos` directory
