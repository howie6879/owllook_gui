#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/7.
"""
import asyncio
from PyQt5 import QtWidgets, QtGui

from owllook_gui.owl_resource import *
from owllook_gui.database import books, sql_insert_item
from owllook_gui.spider import get_latest_chapter, get_novels_info

from owllook_gui.wigdets.wigdets_tools import load_style_sheet, table_widget_item_center


class Search(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.event_loop = asyncio.get_event_loop()
        self.parent = parent
        self.table_widget = QtWidgets.QTableWidget()
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
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_search.clicked.connect(self.func_search_book)
        self.btn_search.setObjectName('btn_search')

        self.btn_end = QtWidgets.QPushButton('添加结束')
        self.btn_end.clicked.connect(self.func_end)
        self.btn_end.setObjectName('btn_end')

        self.h_box.addWidget(self.line_novels_name)
        self.h_box.addWidget(self.btn_search)

        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)
        self.resize(415, 115)

    def func_end(self):
        self.parent.func_refresh(refresh=False)
        self.hide()

    def func_line_clear(self):
        self.line_novels_name.setText('')

    def func_search_book(self):
        name = self.line_novels_name.text()

        async def sync_search_book(self):
            """
            开启异步函数进行书籍获取
            百度 demo: intitle:{} 小说 阅读  {} 目录 笔趣阁
            :return:
            """
            async_func_res = await get_novels_info(
                class_name='so',
                novels_name='{} 最新章节 阅读'.format(name)
            )

            if len(async_func_res):
                # 表格布局
                self.table_widget.clear()
                headers = ["标题", "来源"]
                self.table_widget.setColumnCount(len(headers))
                self.table_widget.setRowCount(len(async_func_res))
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
                # 设置header
                self.table_widget.setHorizontalHeaderLabels(headers)
                # 设置点击事件 双击插入
                self.table_widget.itemDoubleClicked.connect(self.func_table_item_click)

                for index, each in enumerate(async_func_res):
                    self.table_widget.setItem(index, 0, table_widget_item_center(each.get('title')))
                    self.table_widget.setItem(index, 1, table_widget_item_center(each.get('url')))

                self.v_box.addWidget(self.table_widget)
                self.v_box.addStretch()
                self.v_box.addWidget(self.btn_end)
                self.setWindowTitle(name + ' - 双击即可添加')
                self.resize(500, 300)

        if name:
            self.event_loop.create_task(sync_search_book(self))
        else:
            self.line_novels_name.setPlaceholderText('请输入小说名!')

    def func_table_item_click(self, item):
        # 获取某行数据
        title = self.table_widget.item(item.row(), 0).text()
        url = self.table_widget.item(item.row(), 1).text()
        values = {
            'title': self.line_novels_name.text() or title,
            'url': url
        }

        async def async_insert_item(self):
            await sql_insert_item(table_ins=books, engine=self.parent.engine, values=values)
            QtWidgets.QMessageBox.information(self, "Information",
                                              self.tr(self.line_novels_name.text() + " - 保存成功"))

        self.event_loop.create_task(async_insert_item(self))

    def closeEvent(self, event):
        self.hide()
        event.ignore()
