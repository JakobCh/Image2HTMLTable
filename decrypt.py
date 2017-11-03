#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, time, sys, random
from PIL import Image
from HTMLParser import HTMLParser

_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}

height = 0
width = 0
colorarray = []

def rgb(triplet):
    return _HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]

class SizeParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == "tr":
			global height
			height += 1
		elif tag == "td":
			if height < 2:
				global width
				width += 1
			
			#print(attrs[1][1])
			colorarray.append(rgb(attrs[1][1].replace("#", "")))
	
		#print "Encountered a start tag:", tag
		

def doit(path):
	sizeparser = SizeParser()
	f = open(path, "r").read()
	sizeparser.feed(f)
	
	print(height)
	print(width)
	
	#print(colorarray)
	
	newpath = path + ".png"
	
	image = Image.new("RGB", (width, height))
	pixels = image.load()
	
	counter = 0
	
	for y in xrange(image.size[1]): #from the top to the bottom
		for x in xrange(image.size[0]): #from the left to the right
			pixels[x,y] = colorarray[counter]
			counter += 1
			
	image.save(newpath, "PNG")



if len(sys.argv) == 2:
	doit(sys.argv[1])
else:
	print("Usage " + sys.argv[0] + " <htmlpath>")