#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/7.
"""
import asyncio
from PyQt5 import QtCore, QtWidgets, QtGui

from owllook_gui.config import Config
from owllook_gui.owl_resource import *
from owllook_gui.spider import get_novels_info

from owllook_gui.wigdets.wigdets_tools import load_style_sheet, table_widget_item_center


class Search(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.event_loop = asyncio.get_event_loop()
        self.init_ui()

    def init_ui(self):
        # 加载样式
        load_style_sheet(self, 'search')

        self.setWindowTitle("小说搜索")
        self.setObjectName('search')

        self.h_box = QtWidgets.QHBoxLayout()
        self.line_novels_name = QtWidgets.QLineEdit()
        self.line_novels_name.setPlaceholderText('输入小说名')
        self.line_novels_name.setObjectName('line_novels_name')
        self.line_novels_name.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        action = QtWidgets.QAction(self)
        action.setIcon(QtGui.QIcon(':/resource/images/clean.png'))
        action.triggered.connect(self.func_line_clear)
        self.line_novels_name.addAction(action, QtWidgets.QLineEdit.TrailingPosition)

        self.btn_search = QtWidgets.QPushButton('搜索')
        self.btn_search.clicked.connect(self.func_search_book)
        self.btn_search.setObjectName('btn_search')

        self.btn_add = QtWidgets.QPushButton('添加源')
        self.btn_add.clicked.connect(self.func_add_book)
        self.btn_add.setObjectName('btn_search')

        self.h_box.addWidget(self.line_novels_name)
        self.h_box.addWidget(self.btn_search)

        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addLayout(self.h_box)
        self.v_box.addStretch()

        self.setLayout(self.v_box)
        self.resize(380, 260)

    def func_add_book(self):
        pass

    def func_line_clear(self):
        self.line_novels_name.setText('')

    def func_search_book(self):
        name = self.line_novels_name.text()

        # 表格布局
        self.table_widget = QtWidgets.QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setRowCount(1)
        self.table_widget.setObjectName('search_books_table')
        # 表格100%填满窗口
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 设置选中表格整行
        self.table_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # 设置表格不可编辑
        self.table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # 设置字体
        self.table_widget.setFont(QtGui.QFont('SansSerif', 12))

        self.table_widget.setHorizontalHeaderLabels(["标题", "来源", "操作"])

        self.table_widget.setItem(0, 0, table_widget_item_center('牧神记'))
        self.table_widget.setItem(0, 1, table_widget_item_center("笔趣阁"))
        self.table_widget.setItem(0, 2, table_widget_item_center("添加"))

        self.v_box.addWidget(self.table_widget)
        self.v_box.addWidget(self.btn_add)
        self.v_box.addStretch()
        if name:
            self.event_loop.create_task(get_novels_info(
                class_name='so',
                novels_name='{} 全文阅读 笔趣阁'.format(name)
            ))

    def closeEvent(self, event):
        self.hide()
        event.ignore()
