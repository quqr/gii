# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/dev/pyQode/pyqode.core/forms/dlg_preferred_encodings_editor.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtWidgets, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(827, 600)
        Dialog.setMinimumSize(QtCore.QSize(700, 600))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidgetAvailable = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidgetAvailable.setObjectName("tableWidgetAvailable")
        self.tableWidgetAvailable.setColumnCount(0)
        self.tableWidgetAvailable.setRowCount(0)
        self.tableWidgetAvailable.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidgetAvailable.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetAvailable.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidgetAvailable, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setText("")
        icon = QtGui.QIcon.fromTheme("go-next")
        self.pushButtonAdd.setIcon(icon)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.verticalLayout.addWidget(self.pushButtonAdd)
        self.pushButtonRemove = QtWidgets.QPushButton(Dialog)
        self.pushButtonRemove.setText("")
        icon = QtGui.QIcon.fromTheme("go-previous")
        self.pushButtonRemove.setIcon(icon)
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.verticalLayout.addWidget(self.pushButtonRemove)
        self.line_2 = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidgetPreferred = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidgetPreferred.setObjectName("tableWidgetPreferred")
        self.tableWidgetPreferred.setColumnCount(0)
        self.tableWidgetPreferred.setRowCount(0)
        self.tableWidgetPreferred.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidgetPreferred.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetPreferred.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tableWidgetPreferred, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(_("Edit preferred encodings"))
        self.groupBox.setTitle(_("Available encodings"))
        self.pushButtonAdd.setToolTip(_("Add selected encoding to the list of preferred encodings"))
        self.groupBox_2.setTitle(_("Preferred encodings"))

from . import pyqode_core_rc