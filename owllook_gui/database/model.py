#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/11.
 https://github.com/RazerM/sqlalchemy_aio
"""
import os

from sqlalchemy_aio import ASYNCIO_STRATEGY

from sqlalchemy import Column, Integer, MetaData, Table, VARCHAR, create_engine

from owllook_gui.config import Config

path = os.path.join(Config.BASE_DIR, 'database')
db_path = os.path.join(path, 'owllook_gui.db')

metadata = MetaData()

books = Table(
    'books', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', VARCHAR(100)),
    Column('url', VARCHAR(200)),
    Column('latest_chapter_name', VARCHAR(50), default=None),
    Column('latest_chapter_url', VARCHAR(200), default=None),
)

engine = create_engine(
    # In-memory sqlite database cannot be accessed from different
    # threads, use file.
    'sqlite:///' + '/tmp/owllook_gui.db', strategy=ASYNCIO_STRATEGY
)
metadata.create_all(engine._engine)
