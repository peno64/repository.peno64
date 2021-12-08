import sys, urllib, os
import xbmc, xbmcvfs, xbmcplugin, xbmcgui, xbmcaddon

sysarg=str(sys.argv[1])
ADDON_ID='script.realdebrid'
addon=xbmcaddon.Addon(id=ADDON_ID)

try:
    translatePath = xbmcvfs.translatePath
except AttributeError:
    translatePath = xbmc.translatePath

home=translatePath(addon.getAddonInfo('path'))

# the main menu structure
mainMenu=[
    {
        "title":"Unrestrict Link",
        "url":"",
        "mode":5,
        "poster":"none",
        "icon":os.path.join(home, '', 'icon.png'),
        "fanart":os.path.join(home, '', 'fanart.jpg'),
        "type":"",
        "plot":"",
        "isFolder":True,
        "isPlayable":True
    },
    {
        "title":"Add Torrent File",
        "url":"",
        "mode":3,
        "poster":"none",
        "icon":os.path.join(home, '', 'icon.png'),
        "fanart":os.path.join(home, '', 'fanart.jpg'),
        "type":"",
        "plot":"",
        "isFolder":True,
    },
    {
        "title":"Add Magnet Link",
        "url":"",
        "mode":4,
        "poster":"none",
        "icon":os.path.join(home, '', 'icon.png'),
        "fanart":os.path.join(home, '', 'fanart.jpg'),
        "type":"",
        "plot":"",
        "isFolder":True,
    },
    {
        "title":"View Torrents",
        "url":"",
        "mode":1,
        "poster":"none",
        "icon":os.path.join(home, '', 'icon.png'),
        "fanart":os.path.join(home, '', 'fanart.jpg'),
        "type":"",
        "plot":"",
        "isFolder":True,
        "extras":{"offset":"0", "limit":"100"}
    },
    {
        "title":"View Unrestricted Links",
        "url":"",
        "mode":2,
        "poster":"none",
        "icon":os.path.join(home, '', 'icon.png'),
        "fanart":os.path.join(home, '', 'fanart.jpg'),
        "type":"",
        "plot":"",
        "isFolder":True,
        "extras":{"offset":"0", "limit":"100"}
    }
    ,
    {
        "title":"View Host Statuses",
        "url":"",
        "mode":7,
        "poster":"none",
        "icon":os.path.join(home, '', 'icon.png'),
        "fanart":os.path.join(home, '', 'fanart.jpg'),
        "type":"",
        "plot":"",
        "isFolder":True,
        "extras":{"offset":"0", "limit":"100"}
    }
    ,
    {
        "title":"VPN Info",
        "url":"",
        "mode":14,
        "poster":"none",
        "icon":os.path.join(home, '', 'icon.png'),
        "fanart":os.path.join(home, '', 'fanart.jpg'),
        "type":"",
        "plot":"",
        "isFolder":True,
        "extras":{"offset":"0", "limit":"100"}
    }
]