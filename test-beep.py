# -*- coding: utf-8 -*-
#  _             _      
# | |__  ___  __| |_ __ 
# | '_ \/ __|/ _` | '__|
# | |_) \__ \ (_| | |   
# |_.__/|___/\__,_|_|   
#
# Created by wangquan on 16-12-18 下午11:27.
#

import os
import time


while 1:
    beep = os.popen("beep -f 1000 -l 460 -n")
    print beep.read(), 1
    beep.close()
    time.sleep(1)
    print '\07'
