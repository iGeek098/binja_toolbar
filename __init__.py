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
from binaryninja import BinaryView as bv
from widgets import BinjaButtonHolderWidget
from functools import partial

toolbar = BinjaButtonHolderWidget()

def add_text_button(name, fun=None):
    button = QtWidgets.QPushButton(name, toolbar)
    if fun is not None:
        button.clicked.connect(partial(fun, bv))
    toolbar.add_widget(button)

from binaryninja import log
def show_toolbar_message(_view):
    log.log(4, "You haven't created any toolbar buttons yet!")

add_text_button("Demo", show_toolbar_message)

toolbar.show()
