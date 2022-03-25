import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import subprocess
import warnings
from time import *
from random import *
try:
	from selenium import webdriver # Библиотека для браузера
except ModuleNotFoundError:
	os.system('pip install selenium')
	from selenium import webdriver
try:
	import pygame # Библиотека для звуков
except ModuleNotFoundError:
	os.system('pip install pygame')
	import pygame
try:
	import keyboard # Библиотека для горячих клавиш
except ModuleNotFoundError:
	os.system('pip install keyboard')
	import keyboard