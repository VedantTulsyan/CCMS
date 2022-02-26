import sys
import time
from colorit import *
init_colorit


def progressBar():
	animation     = ["[□□□□□□□□□□]","[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]"]
	progress_anim = 0
	save_anim     = animation[progress_anim % len(animation)]
	percent       = 0
	while True:
		for i in range(10):
			percent += 1
			sys.stdout.write(   '\33[91m' + "\r        Loading...  " + save_anim + f" {percent}%" + '\33[0m' +  '\33[0m')
			sys.stdout.flush()
			time.sleep(0.015)
		progress_anim += 1
		save_anim = animation[progress_anim % len(animation)]
		if percent == 100:
			sys.stdout.write(   '\33[96m'+ "\r        Load completed... [■■■■■■■■■■] 100%" +  '\33[0m')
			break
		
		
def Quit():
	animation     = ["[□□□□□□□□□□]","[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]"]
	progress_anim = 0
	save_anim     = animation[progress_anim % len(animation)]
	percent       = 0
	while True:
		for i in range(10):
			percent += 1
			sys.stdout.write(   '\33[33m' + "\r        Quiting...  " + save_anim + f" {percent}%" + '\33[0m' +  '\33[0m')
			sys.stdout.flush()
			time.sleep(0.015)
		progress_anim += 1
		save_anim = animation[progress_anim % len(animation)]
		if percent == 100:
			sys.stdout.write(   '\33[96m'+ "\r        Thank You               :)    " +  '\33[0m')
			break
		
def Start():
	animation     = ["[□□□□□□□□□□]","[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]"]
	progress_anim = 0
	save_anim     = animation[progress_anim % len(animation)]
	percent       = 0
	while True:
		for i in range(10):
			percent += 1
			sys.stdout.write(color("\r        Starting...  " + save_anim + f" {percent}%", (255,0,0)))
			sys.stdout.flush()
			time.sleep(0.015)
		progress_anim += 1
		save_anim = animation[progress_anim % len(animation)]
		if percent == 100:
			sys.stdout.write(color("\r          Starting in 3..2..1....     " , Colors.green))
			time.sleep(3)
			break


