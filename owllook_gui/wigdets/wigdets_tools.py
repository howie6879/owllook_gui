#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/6.
"""
from PyQt5 import QtCore, QtWidgets

from owllook_gui.owl_resource import *


def load_style_sheet(instance, sheet_name):
    file = QtCore.QFile(':/resource/qss/%s.qss.css' % sheet_name.lower())
    file.open(QtCore.QFile.ReadOnly)

    style_sheet = str(file.readAll(), encoding='utf8')
    instance.setStyleSheet(style_sheet)


def table_widget_item_center(value):
    widget_item = QtWidgets.QTableWidgetItem(value)
    widget_item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    return widget_item
