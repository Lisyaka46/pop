def Musicq():
	cls = lambda: os.system('cls')
	music_close = 0
	time1 = time()
	time2 = 0
	time_sec = 0
	number_music = randint(0, len(MP3_chill) - 1)
	while True:
		time1 = time()
		#cls()
		#print('Name: "%s"' % (MP3_chill[number_music]))
		mp3 = pygame.mixer.Sound(MP3_chill[number_music])
		channel.play(mp3)
		while time_sec != int(music_time_list[number_music]):
			if keyboard.is_pressed('Ctrl + Alt + Right') == True:
				music_close = 1
				break
			if keyboard.is_pressed('Ctrl + Alt + Left') == True:
				music_close = 2
				break
			time2 = time()
			if time2 - time1 >= 1:
				time1 = time()
				time_sec += 1
			#print('\rTime: "%s" >> "%s"' % (time_sec, int(music_time_list[number_music])), end = '')
		time_sec = 0
		if music_close == 0:
			if number_music != len(MP3_chill) - 1:
				number_music += 1
		else:
			if music_close == 1:
				if number_music != len(MP3_chill) - 1:
					number_music += 1
				else:
					number_music = 0
			elif music_close == 2:
				if number_music != 0:
					number_music -= 1
				else:
					number_music = len(MP3_chill) - 1
			music_close = 0
		while keyboard.is_pressed('Ctrl + Alt + Right') != False:
			pass
		while keyboard.is_pressed('Ctrl + Alt + Left') != False:
			pass
def save_vol():
	txt = None
	txting = ''
	file = open('Viu/0_4.viu')
	while True:
		txt = file.read(1)
		txting += txt
		if txt == ';':
			break
	file.close()
	file = open('Viu/0_4.viu', 'w')
	file.write('%s%s}!' % (txting, audio_vol))
	file.close()
def start():
	global audio_vol
	music = Thread(target = Musicq)
	while True:
		if keyboard.is_pressed('Ctrl + Alt + Up') == True:
				while keyboard.is_pressed('Ctrl + Alt + Up') != False:
					if audio_vol < 0.98:
						audio_vol += 0.01
						channel.set_volume(audio_vol)
						sleep(0.05)
				save_vol()
		if keyboard.is_pressed('Ctrl + Alt + Down') == True:
				while keyboard.is_pressed('Ctrl + Alt + Down') != False:
					if audio_vol > 0:
						audio_vol -= 0.01
						channel.set_volume(audio_vol)
						sleep(0.05)
				save_vol()
		if os.path.isfile('TF/ClosepanelQRTG.tf') == True:
			os.remove('TF/ClosepanelQRTG.tf')
			while audio_vol > 0.01:
				audio_vol -= 0.04
				channel.set_volume(audio_vol)
				sleep(0.05)
			audio_vol = 0
			channel.set_volume(0)
import os
import sys
import keyboard
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()
from threading import Thread
from mutagen.mp3 import MP3
from random import *
from time import *
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
number_music = None
global music_time_list
music_time_list = [215]
global MP3_chill
MP3_chill = ['Chill/8080.mp3']
os.chdir('Chill/local_music')
for root, dirs, files in os.walk(".", topdown = True):
	for name in files:
		if name.endswith('.mp3'):
			MP3_chill.append('Chill/local_music/%s' % (str(os.path.join(name))))
			music = MP3('%s' % (os.path.join(name)))
			music_time_list.append(int(music.info.length))
os.chdir('..'), os.chdir('..')
channel = pygame.mixer.find_channel()
global audio_vol
audio_vol = None
txt = None
txting = ''
file = open('Viu/0_4.viu')
while txt != ';':
	txt = file.read(1)
txt = None
while txt != '!':
	txt = file.read(1)
	if txt == '}':
		audio_vol = float(txting)
	else:
		if txt != '}':
			txting += txt
file.close()
channel.set_volume(audio_vol)
music, button = Thread(target = Musicq), Thread(target = start)
if __name__ == '__main__':
    music.start(), button.start()
    music.join(), button.join()