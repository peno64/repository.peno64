pysubs2 library Kodi plugin
===========================

KODI plugin that implements pysubs2 library for subtitle conversion.

All pysubs2 code is written by Tomas Karabela.
https://github.com/tkarabela/pysubs2

any2ass.py is a modified version of: 
https://github.com/ewwink/kodi-addon-subtitle-background/blob/master/resources/lib/srt2ass.py

All credits go to their authors.


Plugin is issued from within customized service.subtitles.xxxxxx plugin and allows to convert
any type of subtitle file (if supported by pysubs2 library) into SubStation Alpha format (.ass).
The style of converted subtitles file is changed to include solid black background that easies
reading subtitles displayed on top of the movie.


Installation in KODI:
=====================
- download plugin
- open KODI -> System -> Settings -> Add-ons -> Install from zip file
- navigate to the file you downloaded


Usage:
======
reference this plugin in your subtitle addon by:
```  
  <requires>
    <import addon="script.module.pysubs2" version="0.1.0"/>
  </requires>
```


Import any2ass function in your script:

```
from lib.any2ass import any2ass
```

Call the plugin's any2ass function:
```
sub = any2ass(sub)
```
where:
- sub = filename of chosen subtitle file



The complete code for subtitle addon looks like this:
```
...
elif params['action'] == 'download':
    subs = Download(params["ID"], params["link"],params["format"])
    for sub in subs:
        sub = any2ass(sub)
    
    listitem = xbmcgui.ListItem(label=sub)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=sub,listitem=listitem,isFolder=False)
```



Changelog:
==========

0.1.0
- settings moved from subtitle plugin to this plugin

0.0.2
- added support for TMP subtitle format
- pysubs2 library forked to verion 0.2.3 (statically linked)

0.0.1
- initial plugin version
- pysubs2 library version: 0.2.2 (statically linked)
