#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PIL import Image


def doit(path):
	outpath = path + ".html"
	outfile = open(outpath, "w")

	img1 = Image.open(path)
	pixels1 = img1.load()
	
	#write the start things
	outfile.write('<html><body bgcolor=#0F0F0F>')
	
	#style
	outfile.write('<style>body{margin:0 auto;} table{border-collapse: collapse;}</style>')
	
	outfile.write('<table align="center" style="width:' + str(img1.size[0]) + 'px; height:' + str(img1.size[1]) + 'px;">')
	
	#write pixels
	for y in xrange(img1.size[1]): #from the top to the bottom
		outfile.write('<tr height=1>')
		for x in xrange(img1.size[0]): #from the left to the right
			#print pixels1[x,y]
			temp = '#%02x%02x%02x' % (pixels1[x,y][0], pixels1[x,y][1], pixels1[x,y][2])
			outfile.write('<td width=1 bgcolor=' + temp + '></td>')
			
		outfile.write('</tr>')
	
	#end table
	outfile.write('</table>')
	
	#write the end things
	outfile.write('</body></html>')
	
if len(sys.argv) == 2:
	doit(sys.argv[1])
else:
	print("Usage " + sys.argv[0] + " <imagepath>")