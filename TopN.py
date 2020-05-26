# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TopN.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import SplitWords
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("TopN词频统计")
        Form.resize(554, 392)
        self.deal = QtWidgets.QPushButton(Form)
        self.deal.setGeometry(QtCore.QRect(240, 310, 81, 41))
        self.deal.setObjectName("deal")
        self.input = QtWidgets.QTextEdit(Form)
        self.input.setGeometry(QtCore.QRect(20, 70, 241, 191))
        self.input.setObjectName("input")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.output = QtWidgets.QTextEdit(Form)
        self.output.setGeometry(QtCore.QRect(290, 70, 241, 191))
        self.output.setObjectName("output")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(390, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.init()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.deal.setText(_translate("Form", "词频统计"))
        self.input.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">万络给止痛药市场带来的阴霾久久仍未散去，但这丝毫不能说明该市场的需求在减少。在既定的需求现实下，ＣＯＸ－２抑制剂的衰落，必然引来趁虚而入者。不久前我国河南帅克制药和贵州益佰先后宣称将倚靠新的止痛药进入该领域，一场“分羹”之战显然已经急促展开。</p></body></html>"))
        self.label.setText(_translate("Form", "数据"))
        self.label_2.setText(_translate("Form", "TopN"))


    def init(self):
        print("init")
        self.deal.clicked.connect(self.deal_click)

    def deal_click(self):
        data = self.input.toPlainText()
        data1 = SplitWords.split(data)
        print("123::",data1)
        val = ''
        for v in data1:
            print(v[0] + "::" + str(v[1]))
            val += v[0] + "::" + str(v[1]) + '\n'

        self.output.setPlainText(val)

    def closeEvent(self, event):
        ok = QtWidgets.QPushButton()
        cacel = QtWidgets.QPushButton()

        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"关闭", u"是否关闭！")

        msg.addButton(ok,QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cacel.setText(u'取消')
        # msg.setDetailedText('sdfsdff')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            #             self.socket_client.send_command(self.socket_client.current_user_command)
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(qt)
    qt.show()
    sys.exit(app.exec_())