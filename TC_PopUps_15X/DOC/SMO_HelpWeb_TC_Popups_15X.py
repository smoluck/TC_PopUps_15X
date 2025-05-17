#python
#---------------------------------------
# Name:         SMO_HelpWeb_TC_Popups_14X.py
# Version:      1.0
#
# Purpose:      This script is designed to:
#               open the TC_Popups_Help Website
#
# Author:       Franck ELISABETH
# Website:      http://www.smoluck.com
#
# Created:      16/05/2020
# Copyright:    (c) Franck Elisabeth 2017-2021
#---------------------------------------
import lx
filePathToOpen = lx.eval("query platformservice alias ? {kit_TC_Popups_15X:DOC/TC_Popups_Help.htm}")
lx.eval('file.open {%s}' % filePathToOpen)
