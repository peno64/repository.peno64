# -*- coding: utf-8 -*-
# original code borrowed from: https://github.com/ewwink/kodi-addon-subtitle-background/blob/master/resources/lib/srt2ass.py

import sys
import os
import re
import codecs
import xbmcaddon
import pysubs2

__addon__ = xbmcaddon.Addon()

def any2ass(input_file, font_size = 18, encodings = ["utf-8", "cp1252", "cp1250" ]):
    if not os.path.isfile(input_file):
        print input_file + ' does not exist'
        #print(input_file + ' does not exist')
        return

    #try to detect proper encoding
    for enc in encodings:
        try:
            with codecs.open(input_file, mode="rb", encoding=enc) as fd:
                tmp = fd.read()
                break
        except:
            #SubsceneUtilities.log('SRT2ASS: ', enc + ' failed', 2)
            #print enc + ' failed'
            continue

    #load input_file into pysubs2 library
    subs = pysubs2.load(input_file, encoding=enc, fps=23.976)

    #construct output_file name
    output_file = '.'.join(input_file.split('.')[:-1])
    output_file += '.ass'

    #change subs style
    subs.styles["Default"].primarycolor = pysubs2.Color(255, 255, 255, 0)
    subs.styles["Default"].secondarycolor = pysubs2.Color(255, 255, 255, 0)
    subs.styles["Default"].outlinecolor = pysubs2.Color(0, 0, 0, 0)
    subs.styles["Default"].backcolor = pysubs2.Color(0, 0, 0, 0)
    subs.styles["Default"].fontsize = int(float(font_size))
    subs.styles["Default"].bold = -1
    subs.styles["Default"].borderstyle = 3
    subs.styles["Default"].shadow = 0

    #save subs
    subs.save(output_file)

    return output_file

if len(sys.argv) > 1:
    if __addon__.getSetting( "OSbackground" ) == "true":
        fontsize = __addon__.getSetting( "OSfontsize" )
        name = sys.argv[1]
      #  encodinglist = sys.argv[3]
        any2ass(name, fontsize) #, encodinglist)
