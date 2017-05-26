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
from widgets import BinjaButtonHolderWidget
from functools import partial

toolbar = BinjaButtonHolderWidget()

def get_binary_view():
    print(locals().keys())
    try:
        return bv
    except NameError:
        print("BV has not yet been defined")

def add_text_button(name, fun=None, tooltip=None):
    button = QtWidgets.QPushButton(name, toolbar)
    if fun is not None:
        button.clicked.connect(partial(fun, get_binary_view()))
    if tooltip is not None:
        button.setToolTip(tooltip)
    toolbar.add_widget(button)

def add_image_button(filename, size, fun=None, tooltip=None):
    button = QtWidgets.QPushButton('', toolbar)
    button.setIcon(QtGui.QIcon(filename))
    if fun is not None:
        button.clicked.connect(partial(fun, get_binary_view()))
    if tooltip is not None:
        button.setToolTip(tooltip)
    button.setIconSize(QtCore.QSize(size[0], size[1]))
    toolbar.add_widget(button)

toolbar.show()
