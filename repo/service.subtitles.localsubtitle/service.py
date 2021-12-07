# -*- coding: utf-8 -*-

import os
import shutil
import sys
import urllib
import xbmc
import xbmcaddon
import xbmcgui,xbmcplugin
import xbmcvfs
import uuid

if sys.version_info[0] == 3:
    p3 = True
else:
    p3 = False

__addon__ = xbmcaddon.Addon()
__author__     = __addon__.getAddonInfo('author')
__scriptid__   = __addon__.getAddonInfo('id')
__scriptname__ = __addon__.getAddonInfo('name')
__version__    = __addon__.getAddonInfo('version')
__language__   = __addon__.getLocalizedString

try:
    translatePath = xbmcvfs.translatePath
except AttributeError:
    translatePath = translatePath

__cwd__        = translatePath( __addon__.getAddonInfo('path') )
if not p3:
    __cwd__ = __cwd__.decode("utf-8")

__resource__   = translatePath( os.path.join( __cwd__, 'resources', 'lib' ) )
if not p3:
    __resource__ = __resource__.decode("utf-8")

__msg_box__       = xbmcgui.Dialog()

__subtitlepath__  = translatePath("special://subtitles")

if __subtitlepath__ == None:
  __subtitlepath__ = ""

#__subtitlepath__ = ""

#if __subtitlepath__ == None or __subtitlepath__ == '':
#  __msg_box__.ok('LocalSubtitle', __language__(32008))

__subtitle__      = ""
if __subtitlepath__ != "":
  __subtitle__      = __subtitlepath__ + "subtitle.srt"


sys.path.append (__resource__)


def Search():
  if __subtitle__ != "":
    if xbmcvfs.exists(__subtitle__):
      if p3:
        listitem = xbmcgui.ListItem(label          = "",
                                    label2         = __subtitle__
                                    )
      else:
        listitem = xbmcgui.ListItem(label          = "",
                                    label2         = __subtitle__,
                                    iconImage      = "5",
                                    thumbnailImage = ""
                                    )

      listitem.setProperty( "sync", "false" )
      listitem.setProperty( "hearing_imp", "false" )

      url = "plugin://%s/?action=download" % (__scriptid__)

      xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=listitem,isFolder=False)


  if p3:
    listitem = xbmcgui.ListItem(label          = "",
                                label2         = __language__(32010)
                                )
  else:
    listitem = xbmcgui.ListItem(label          = "",
                                label2         = __language__(32010),
                                iconImage      = "0",
                                thumbnailImage = ""
                                )

  listitem.setProperty( "sync", "false" )
  listitem.setProperty( "hearing_imp", "false" )

  url = "plugin://%s/?action=browse" % (__scriptid__)

  xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=listitem,isFolder=False)


def Download():
  subtitle_list = [ __subtitle__ ]

  if xbmcvfs.exists(subtitle_list[0]):
    return subtitle_list

def get_params(string=""):
  param=[]
  if string == "":
    paramstring=sys.argv[2]
  else:
    paramstring=string
  if len(paramstring)>=2:
    params=paramstring
    cleanedparams=params.replace('?','')
    if (params[len(params)-1]=='/'):
      params=params[0:len(params)-2]
    pairsofparams=cleanedparams.split('&')
    param={}
    for i in range(len(pairsofparams)):
      splitparams={}
      splitparams=pairsofparams[i].split('=')
      if (len(splitparams))==2:
        param[splitparams[0]]=splitparams[1]

  return param

params = get_params()


if params['action'] == 'manualsearch':
  __msg_box__.ok('LocalSubtitle', __language__(32009))
  Search()

elif params['action'] == 'search':
  Search()

elif params['action'] == 'download':
  subs = Download()
  for sub in subs:
    listitem = xbmcgui.ListItem(label=sub)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=sub,listitem=listitem,isFolder=False)

elif params['action'] == 'browse':
  subtitlefile = xbmcgui.Dialog().browse(1, __language__(32011), "video", ".srt|.sub|.ssa|.ass|.idx|.smi|.aqt|.scc|.jss|.ogm|.pjs|.rt|.smi", False, False, __subtitlepath__, False)
  if subtitlefile != __subtitlepath__:
    listitem = xbmcgui.ListItem(label=subtitlefile)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=subtitlefile,listitem=listitem,isFolder=False)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
