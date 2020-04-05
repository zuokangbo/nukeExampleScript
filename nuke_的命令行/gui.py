# _*_ coding: utf-8 _*_
# @Time      : 4/1/2020 11:09 PM
# @author    : zuokangbo
# @eamil     : 1156298563@qq.com
# @File      : gui.py
# @software  : PyCharm

import sys

sys.path.append(r'Y:\Program Files\Nuke10.0v1\pythonextensions\site-packages')

from PySide2 import QtWidgets


app = QtGui.QApplication.instance()

w = QtGui.QWidget()
w.show()
sys.exit(app.exec_())


