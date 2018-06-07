## owllook_gui

owllook的客户端小工具，目的是为了监控喜欢的小说是否有更新，目前提供版本：

- 网页版：[owllook](https://github.com/howie6879/owllook)
- 公众号：[粮草小说](http://oe7yjec8x.bkt.clouddn.com/howie/2018-03-13-%E7%B2%AE%E8%8D%89%E5%B0%8F%E8%AF%B4.jpg-blog.howie)
- 终端版：[NIYT](https://github.com/howie6879/NIYT)

ps：在看QT，同样是练手项目~

### 概述

为什么会出这个版本呢？为了更方便监控小说是否更新，为了让owllook更完美，目标是提供跨平台的小说监控工具：

- Mac
- Windows
- Linux

具体下载地址请看[releases](https://github.com/howie6879/owllook_gui/releases)，下载好就可以直接使用，欢迎提交`PR`和`issue`

### 安装

如果想使用还在开发的最新功能，可以自行安装，`owllook_gui`由`PyQt5`编写，下面是安装步骤：

```python
# 下载源码
git clone https://github.com/howie6879/owllook_gui.git
# 保证环境3.5+
pip install requirements.txt
cd owllook_gui
python owllook.py
```

### 特性&截图

#### 特性

- 小说监控
- 小说检索
- 最新章节搜索阅读


#### 截图

**托盘**

![sys_tray](./docs/images/sys_tray.jpg)

**主界面**

![home](/Users/howie/Documents/work/pyqt/git/owllook_gui/docs/images/home.jpg)

### 协议

owllook is offered under the Apache 2 license.