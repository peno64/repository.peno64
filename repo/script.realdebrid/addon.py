# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 BigNoid
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import xbmc, xbmcgui

def main():
    parts=str(xbmc.getInfoLabel('ListItem.FileNameAndPath')).replace(xbmc.getInfoLabel('ListItem.Path')+"?", "").split("&")
    parts=parts[0].replace("url=", "")

    play = ("plugin://script.realdebrid/" +
        "?url=" + parts +
        "&mode=" + str(5) +
        "&poster="+""+
        "&fanart="+""+
        "&name=" + ""
    )
    xbmc.executebuiltin('RunPlugin("'+play+'")')


if __name__ == '__main__':
    main()