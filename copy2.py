#!/usr/bin/python

import shutil
import os

def copyInTo(dirIn, dirOut):
	fileList = os.listdir(dirIn)  
	dest = dirOut 
	for i in fileList:  
		src = dirIn + '/' + i  
		shutil.move(src,dest)

copyInTo('test', 'to')