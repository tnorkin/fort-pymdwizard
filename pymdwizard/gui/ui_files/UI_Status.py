# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Status.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(310, 142)
        Form.setMinimumSize(QtCore.QSize(310, 0))
        Form.setMaximumSize(QtCore.QSize(310, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fgdc_status = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_status.sizePolicy().hasHeightForWidth())
        self.fgdc_status.setSizePolicy(sizePolicy)
        self.fgdc_status.setStyleSheet("")
        self.fgdc_status.setObjectName("fgdc_status")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fgdc_status)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.fgdc_status)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fgdc_progress = QtWidgets.QComboBox(self.fgdc_status)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.fgdc_progress.setFont(font)
        self.fgdc_progress.setInputMethodHints(QtCore.Qt.ImhNone)
        self.fgdc_progress.setEditable(False)
        self.fgdc_progress.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon
        )
        self.fgdc_progress.setObjectName("fgdc_progress")
        self.fgdc_progress.addItem("")
        self.fgdc_progress.addItem("")
        self.fgdc_progress.addItem("")
        self.horizontalLayout.addWidget(self.fgdc_progress)
        self.label_9 = QtWidgets.QLabel(self.fgdc_status)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(15, 0))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_9.setIndent(0)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.fgdc_status)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_36 = QtWidgets.QLabel(self.fgdc_status)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setStyleSheet("font: italic;")
        self.label_36.setObjectName("label_36")
        self.verticalLayout_2.addWidget(self.label_36)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fgdc_update = QtWidgets.QComboBox(self.fgdc_status)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_update.sizePolicy().hasHeightForWidth())
        self.fgdc_update.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.fgdc_update.setFont(font)
        self.fgdc_update.setEditable(True)
        self.fgdc_update.setObjectName("fgdc_update")
        self.fgdc_update.addItem("")
        self.fgdc_update.addItem("")
        self.fgdc_update.addItem("")
        self.fgdc_update.addItem("")
        self.fgdc_update.addItem("")
        self.fgdc_update.addItem("")
        self.fgdc_update.addItem("")
        self.fgdc_update.addItem("")
        self.fgdc_update.addItem("")
        self.horizontalLayout_2.addWidget(self.fgdc_update)
        self.label_10 = QtWidgets.QLabel(self.fgdc_status)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(15, 0))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_10.setIndent(0)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.fgdc_status)

        self.retranslateUi(Form)
        self.fgdc_update.setCurrentIndex(8)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fgdc_status.setTitle(_translate("Form", "Data Status and Update Plans"))
        self.label_2.setText(_translate("Form", "Status"))
        self.fgdc_progress.setCurrentText(_translate("Form", "Complete"))
        self.fgdc_progress.setItemText(0, _translate("Form", "Complete"))
        self.fgdc_progress.setItemText(1, _translate("Form", "In work"))
        self.fgdc_progress.setItemText(2, _translate("Form", "Planned"))
        self.label_9.setToolTip(_translate("Form", "Required"))
        self.label_9.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
        self.label_3.setText(_translate("Form", "Update Plans"))
        self.label_36.setText(
            _translate("Form", "Type directly in box below for items not in list.")
        )
        self.fgdc_update.setItemText(0, _translate("Form", "Continually"))
        self.fgdc_update.setItemText(1, _translate("Form", "Daily"))
        self.fgdc_update.setItemText(2, _translate("Form", "Weekly"))
        self.fgdc_update.setItemText(3, _translate("Form", "Monthly"))
        self.fgdc_update.setItemText(4, _translate("Form", "Annually"))
        self.fgdc_update.setItemText(5, _translate("Form", "Unknown"))
        self.fgdc_update.setItemText(6, _translate("Form", "As needed"))
        self.fgdc_update.setItemText(7, _translate("Form", "Irregular"))
        self.fgdc_update.setItemText(8, _translate("Form", "None planned"))
        self.label_10.setToolTip(_translate("Form", "Required"))
        self.label_10.setText(
            _translate(
                "Form",
                '<html><head/><body><p><span style=" font-size:18pt; color:#55aaff;">*</span></p></body></html>',
            )
        )
