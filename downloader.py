'''
Name    John Park
Github  john-yohan-park
Date    3/13/2020
'''
# import libraries
from __future__ import unicode_literals # turn every string into unicode
import youtube_dl                       # download youtube video by URL
import os                               # create & navigate directories
from   sys import argv				    # accept command line arguments

# set up download configurations
config = {
	'format'              : 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
	'outtmpl'             : '%(title)s.%(ext)s',
	'nocheckcertificate'  : True
}

# manage & navigate file
if not os.path.exists('Videos'): # if 'Songs' directory does not exist,
    os.mkdir('Videos')           # create it
os.chdir('Videos')               # make 'Songs' current working directory

# download
if len(argv)>1:										# if URL is provided as cmd line arg
	with youtube_dl.YoutubeDL(config) as dl:		# set up configs
		dl.download([argv[1]]) 				        # download song from URL
else:												# if not, get URLs from songs.txt
	with youtube_dl.YoutubeDL(config) as dl:        # instantiate youtube_dl with preset configs
		with open('../urls.txt', 'r') as txt_file: # open and read text file (../ moves us up one directory) ('r' for reading)
			for song_url in txt_file:               # for every song URL in text file
				dl.download([song_url])             # download song from URL
