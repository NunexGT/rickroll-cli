import argparse
from multiprocessing.connection import wait
from threading import current_thread
import webbrowser
import pytube
import os
import time

rickroll_official_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
current_directory = os.getcwd()

def rickroll():
    webbrowser.open(rickroll_official_url, new=2)

def rickroll_download_video():
    yt = pytube.YouTube(rickroll_official_url)
    yt.streams.filter(res="720p").first().download()
    print('Videoclip Downloaded, Happy Rickroll!')


def rickroll_download_music():
    yt = pytube.YouTube(rickroll_official_url)
    mp3rick=yt.streams.filter(only_audio=True).first()
    mp3rick.download()
    print('Rickroll song Downloaded, Happy Rickroll!')

def rickroll_spam(amount_of_spam):
    for i in range(amount_of_spam):
        rickroll()
        time.sleep(4)

def wait_for_rick(wait):
    time.sleep(wait)
    rickroll()



parser = argparse.ArgumentParser(description='It´s Rickrolling Time!')
parser.add_argument('-start',action='store_true',help='Imediatly starts Rickrolling, use this if you are going to use any other flags')
parser.add_argument('--download','-d', action='store_true',
                    help='Downloads you the Rickroll videoclip and saves it to your current directory')
parser.add_argument('--audio','-a',action='store_true',help='Downloads the RickRoll song and save it to your current directory')
parser.add_argument('--spam','-s',type=int,required=False,help='Specify how much rickroll you want to open at the same time')
parser.add_argument('--wait','-w',type=int,required=False,help="Specify a certain amount of time for the rickroll to happear. Use your caution, your friends might not be prepared for a SURPRISE RICKROLL [RISK OF HEART ATTACK]")
args = parser.parse_args()

if __name__ == '__main__':
    if args.start:
        rickroll()
    if args.download:
        rickroll_download_video()
    if args.audio:
        rickroll_download_music()
    if args.spam:
        rickroll_spam(args.spam)
    if args.wait:
        wait_for_rick(args.wait)
    else:
        rickroll()