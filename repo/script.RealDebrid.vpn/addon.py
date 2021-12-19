import xbmcaddon
import xbmcgui
import xbmcplugin
import re
import sys

try:  # Python 3
    import urllib.parse
    import urllib.request
    p2 = False
except ImportError:
    import urllib2
    p2 = True

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

url = "https://real-debrid.com/vpn"

if p2:
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
else:
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)

lines = response.readlines()

line1 = ""
line2 = ""
line3 = ""

vpnInfo = False
for l in lines:
    if p2:
        line = l
    else:
        line = bytes.decode(l)

    line = line.strip(' \t\n\r')

    x = re.search("VPN Information", line)
    if not x == None:
       vpnInfo = True
    else:
       if vpnInfo and line != "":
         line1 = re.sub(r"\<[^>]+\>", "", line)
         vpnInfo = False

    x = re.search("Your IP Address:", line)
    if not x == None:
      line2 = re.sub(r"\<[^>]+\>", "", line)

    x = re.search("Your IP Reverse:", line)
    if not x == None:
      line3 = re.sub(r"\<[^>]+\>", "", line)

    if line1 != "" and line2 != "" and line3 != "":
      break

if False:
  xbmcgui.Dialog().ok(url, line2, line3, line1)
else:
  lines = line1.split('.')
  for line in lines:
    if p2:
        li = xbmcgui.ListItem(line.strip(), iconImage='DefaultFolder.png')
    else:
        li = xbmcgui.ListItem(line.strip())

    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url="", listitem=li, isFolder=False)

  if p2:
      li = xbmcgui.ListItem(line2, iconImage='DefaultFolder.png')
  else:
      li = xbmcgui.ListItem(line2)

  xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url="", listitem=li, isFolder=False)

  if p2:
      li = xbmcgui.ListItem(line3, iconImage='DefaultFolder.png')
  else:
      li = xbmcgui.ListItem(line3)

  xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url="", listitem=li, isFolder=False)

  xbmcplugin.setContent(int(sys.argv[1]), 'files')
  xbmcplugin.endOfDirectory(int(sys.argv[1]))
