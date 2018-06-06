#!/usr/bin/env python
"""
 Created by howie.hu at 2018/5/23.
"""
import asyncio

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QHBoxLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, \
    QWidget

from owllook_gui.owl_resource import *
from owllook_gui.config import Config
from owllook_gui.spider import get_novels_info

from owllook_gui.wigdets import load_style_sheet, SystemTray

MAC = hasattr(QtGui, "qt_mac_set_native_menubar")


class OwlHome(QMainWindow):

    def __init__(self, event_loop=None, parents=None):
        super(OwlHome, self).__init__(parent=parents)
        self.icon_path = ':/resource/images/owl.png'

        self.system_tray_ins = SystemTray(icon_path=self.icon_path, parent=self)
        self.event_loop = event_loop if event_loop else asyncio.get_event_loop()
        self.init_ui()

    def init_ui(self):
        # 加载样式
        load_style_sheet('main')
        # 设置图标以及标题
        self.setWindowTitle(Config.APP_TITLE)
        self.setWindowIcon(QtGui.QIcon(self.icon_path))
        # 布局
        self.label = QLabel('书架暂无数据')
        self.label.setFont(QtGui.QFont('SansSerif', 13))
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.v_box = QVBoxLayout()
        self.v_box.addStretch()
        self.v_box.addWidget(self.label)
        self.v_box.addStretch()

        self.search_book = QPushButton("搜书")
        self.refresh = QPushButton("刷新")
        self.about = QPushButton("关于")

        self.search_book.clicked.connect(self.func_search_book)
        self.refresh.clicked.connect(self.func_refresh)
        self.about.clicked.connect(self.func_about)

        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.search_book)
        self.h_box.addWidget(self.refresh)
        self.h_box.addWidget(self.about)

        self.v_box.addLayout(self.h_box)

        main_frame = QWidget()
        main_frame.setLayout(self.v_box)
        self.setCentralWidget(main_frame)

        self.resize(300, 200)
        self.func_win_center()

    def func_about(self):
        pass

    def func_refresh(self):
        self.event_loop.create_task(get_novels_info(class_name='so', novels_name='intitle:雪中悍刀行 小说 阅读'))

    def func_search_book(self):
        self.event_loop.create_task(get_novels_info(class_name='baidu', novels_name='intitle:雪中悍刀行 小说 阅读'))

    def func_win_center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def closeEvent(self, event):
        self.hide()
        self.system_tray_ins.show()
        event.ignore()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    # 关闭所有窗口也不关闭应用程序
    # QApplication.setQuitOnLastWindowClosed(False)
    win = OwlHome()

    win.show()
    sys.exit(app.exec_())
