#!/usr/bin/env python
"""
 Created by howie.hu at 2018/5/23.
"""
import asyncio
import os
import sys

from PyQt5.QtWidgets import QApplication
from quamash import QEventLoop

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from owllook_gui.config import Config
from owllook_gui.wigdets.home import OwlHome

app = QApplication(sys.argv)

event_loop = QEventLoop(app)
asyncio.set_event_loop(event_loop)

try:
    with event_loop:
        main = OwlHome(event_loop)
        event_loop.run_forever()
    sys.exit(0)
except:
    Config.LOGGER.error("程序运行出错", exc_info=True)
