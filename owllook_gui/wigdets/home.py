#!/usr/bin/env python
"""
 Created by howie.hu at 2018/5/23.
"""
import asyncio

from PyQt5 import QtGui, QtWidgets

from owllook_gui.owl_resource import *
from owllook_gui.config import Config
from owllook_gui.spider import get_novels_info

from owllook_gui.wigdets import About, Search, SystemTray, table_widget_item_center, load_style_sheet

MAC = hasattr(QtGui, "qt_mac_set_native_menubar")


class OwlHome(QtWidgets.QMainWindow):

    def __init__(self, event_loop=None, parents=None):
        super(OwlHome, self).__init__(parent=parents)
        self.icon_path = ':/resource/images/owl.png'
        self.system_tray_ins = SystemTray(icon_path=self.icon_path, parent=self)
        self.event_loop = event_loop if event_loop else asyncio.get_event_loop()

        self.system_tray_ins.show()
        self.init_ui()

    def init_ui(self):
        # 加载样式
        load_style_sheet(self, 'main')
        # 设置图标以及标题
        self.setWindowTitle(Config.APP_TITLE)
        self.setWindowIcon(QtGui.QIcon(self.icon_path))
        # 布局
        self.bookshelf = QtWidgets.QLabel('书架暂无数据')
        self.bookshelf.setFont(QtGui.QFont('SansSerif', 13))
        self.bookshelf.setAlignment(QtCore.Qt.AlignCenter)

        all_data = ''

        if all_data:
            # 表格布局
            self.table_widget = QtWidgets.QTableWidget()
            self.table_widget.setColumnCount(3)
            self.table_widget.setRowCount(1)
            self.table_widget.setObjectName('books_table')
            # 表格100%填满窗口
            self.table_widget.horizontalHeader().setStretchLastSection(True)
            self.table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            # 设置选中表格整行
            self.table_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            # 设置表格不可编辑
            self.table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            # 设置字体
            self.table_widget.setFont(QtGui.QFont('SansSerif', 12))

            self.table_widget.setHorizontalHeaderLabels(["小说名", "目录", "最新章节"])

            # for index in range(self.table_widget.columnCount()):
            #     head_item = self.table_widget.horizontalHeaderItem(index)
            #     # 设置字体
            #     head_item.setFont(QtGui.QFont('SansSerif', 12, QtGui.QFont.Bold))
            #     head_item.setForeground(QtGui.QBrush(QtCore.Qt.gray))
            #     head_item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.table_widget.setItem(0, 0, table_widget_item_center('牧神记'))
            self.table_widget.setItem(0, 1, table_widget_item_center("查看目录"))
            self.table_widget.setItem(0, 2, table_widget_item_center("第100章：Hello World"))

            self.middle_widget = self.table_widget
            self.resize(420, 200)
        else:
            self.middle_widget = self.bookshelf
            self.resize(300, 200)

        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addStretch()
        self.v_box.addWidget(self.middle_widget)
        self.v_box.addStretch()

        self.btn_search_book = QtWidgets.QPushButton("搜书")
        self.btn_refresh = QtWidgets.QPushButton("刷新")
        self.btn_about = QtWidgets.QPushButton("关于")

        self.btn_search_book.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_about.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.btn_search_book.clicked.connect(self.func_search)
        self.btn_refresh.clicked.connect(self.func_refresh)
        self.btn_about.clicked.connect(self.func_about)

        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addWidget(self.btn_search_book)
        self.h_box.addWidget(self.btn_refresh)
        self.h_box.addWidget(self.btn_about)

        self.v_box.addLayout(self.h_box)

        main_frame = QtWidgets.QWidget()
        main_frame.setObjectName('home')
        main_frame.setLayout(self.v_box)
        self.setCentralWidget(main_frame)

        self.func_win_center()

    def func_about(self):
        self.about_ins = About()
        self.about_ins.setWindowIcon(QtGui.QIcon(self.icon_path))
        self.about_ins.show()

    def func_check_version(self):
        pass

    def func_refresh(self):
        self.event_loop.create_task(get_novels_info(class_name='so', novels_name='intitle:雪中悍刀行 小说 阅读'))

    def func_search(self):
        self.search_ins = Search()
        self.search_ins.setWindowIcon(QtGui.QIcon(self.icon_path))
        self.search_ins.show()

    def func_win_center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def closeEvent(self, event):
        self.hide()
        event.ignore()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # 关闭所有窗口也不关闭应用程序
    # QApplication.setQuitOnLastWindowClosed(False)
    win = OwlHome()

    win.show()
    sys.exit(app.exec_())
