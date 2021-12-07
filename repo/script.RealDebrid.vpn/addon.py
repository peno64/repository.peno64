import xbmcaddon
import xbmcgui
import xbmcplugin
import re
import sys

try:  # Python 3
    import urllib.parse
    import urllib.request
    p3 = True
except ImportError:
    import urllib2
    p3 = False

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

url = "https://real-debrid.com/vpn"

if p3:
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
else:
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)

lines = response.readlines()

line1 = ""
line2 = ""
line3 = ""

vpnInfo = False
for l in lines:
    if p3:
        line = bytes.decode(l)
    else:
        line = l

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
    if p3:
        li = xbmcgui.ListItem(line.strip())
    else:
        li = xbmcgui.ListItem(line.strip(), iconImage='DefaultFolder.png')

    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url="", listitem=li, isFolder=False)

  if p3:
      li = xbmcgui.ListItem(line2)
  else:
      li = xbmcgui.ListItem(line2, iconImage='DefaultFolder.png')

  xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url="", listitem=li, isFolder=False)

  if p3:
      li = xbmcgui.ListItem(line3)
  else:
      li = xbmcgui.ListItem(line3, iconImage='DefaultFolder.png')

  xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url="", listitem=li, isFolder=False)

  xbmcplugin.setContent(int(sys.argv[1]), 'files')
  xbmcplugin.endOfDirectory(int(sys.argv[1]))
