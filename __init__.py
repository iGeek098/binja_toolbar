"""
MIT License

Copyright (c) <2016> <NOP Developments LLC>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


"""

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from binaryninja import *
from widgets import BinjaWidget


class ToolbarWidget(BinjaWidget):
    """Sample Plugin. Displays some text.
    """
    def __init__(self, name):

        super(ToolbarWidget, self).__init__(name)
        self._button = QtWidgets.QPushButton('Demo', self)
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().addWidget(self._button)
        self.setObjectName('BNPlugin_Toolbar')

    @QtCore.pyqtSlot(list)
    def display(self, _):
        self._core.show()
        self._core.selectTab(self)
        self.show()

print("Initializing toolbar")
d = ToolbarWidget('Toolbar')
d.display(None)
