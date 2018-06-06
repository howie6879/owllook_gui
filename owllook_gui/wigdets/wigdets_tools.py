#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/6.
"""
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile

from owllook_gui.owl_resource import *


def load_style_sheet(sheet_name):
    file = QFile(':/resource/qss/%s.qss.css' % sheet_name.lower())
    file.open(QFile.ReadOnly)

    style_sheet = str(file.readAll(), encoding='utf8')
    QApplication.instance().setStyleSheet(style_sheet)
