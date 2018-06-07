#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/6.
"""

from PyQt5 import QtWidgets, QtGui

from owllook_gui.config import Config
from owllook_gui.owl_resource import *

from owllook_gui.wigdets.wigdets_tools import load_style_sheet


class About(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.init_ui()

    def init_ui(self):
        # 加载样式
        load_style_sheet(self, 'about')

        self.setWindowTitle("关于")
        self.setObjectName('about')
        self.name_label = QtWidgets.QLabel("版本：owllook - v{}".format(Config.VERSION))
        self.img_label = QtWidgets.QLabel()
        self.img_label.setPixmap(QtGui.QPixmap(":/resource/images/lcxs.jpg"))
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.author_label = QtWidgets.QLabel(
            "作者：<a style='color:#78a5f1;' href='https://github.com/howie6879'>howie6879</a>")
        self.author_label.setOpenExternalLinks(True)
        self.home_label = QtWidgets.QLabel(
            "项目地址：<a style='color:#78a5f1;' href='https://github.com/howie6879/owllook_gui'>owllook_gui</a>")
        self.home_label.setOpenExternalLinks(True)
        self.dept_label = QtWidgets.QLabel("简介：简洁优雅的小说监控工具 🎉，喜欢就微信扫一扫一起交流吧")
        self.dept_label.setWordWrap(True)

        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.img_label)
        self.box.addWidget(self.name_label)
        self.box.addWidget(self.author_label)
        self.box.addWidget(self.home_label)
        self.box.addWidget(self.dept_label)

        self.setLayout(self.box)
        self.resize(300, 400)

    def closeEvent(self, event):
        self.hide()
        event.ignore()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = About()
    win.show()
    sys.exit(app.exec_())
