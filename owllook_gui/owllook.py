#!/usr/bin/env python
"""
 Created by howie.hu at 2018/5/23.
"""
import asyncio
import sys

from PyQt5.QtWidgets import QApplication
from quamash import QEventLoop

from owllook_gui.config import Config
from owllook_gui.wigdets import OwlHome

app = QApplication(sys.argv)

event_loop = QEventLoop(app)
asyncio.set_event_loop(event_loop)


async def start(event_loop):
    main = OwlHome(event_loop)
    main.show()


try:
    with event_loop:
        event_loop.run_until_complete(start(event_loop))
        event_loop.run_forever()
    sys.exit(0)
except:
    Config.LOGGER.error("程序运行出错", exc_info=True)
