# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
#ifndef Q_OS_MAC
        self.horizontalLayout_6.setSpacing(-1)
#endif
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(12, 12, -1, 0)
        self.verticalLayout1 = QVBoxLayout()
        self.verticalLayout1.setSpacing(0)
        self.verticalLayout1.setObjectName(u"verticalLayout1")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.lineEdit_username = QLineEdit(self.centralwidget)
        self.lineEdit_username.setObjectName(u"lineEdit_username")

        self.horizontalLayout_5.addWidget(self.lineEdit_username)


        self.verticalLayout1.addLayout(self.horizontalLayout_5)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_qiyou = QGroupBox(self.centralwidget)
        self.groupBox_qiyou.setObjectName(u"groupBox_qiyou")
        self.verticalLayout = QVBoxLayout(self.groupBox_qiyou)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget_qiyou = QListWidget(self.groupBox_qiyou)
        self.listWidget_qiyou.setObjectName(u"listWidget_qiyou")

        self.verticalLayout.addWidget(self.listWidget_qiyou)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_qiyou_count = QLabel(self.groupBox_qiyou)
        self.label_qiyou_count.setObjectName(u"label_qiyou_count")

        self.horizontalLayout.addWidget(self.label_qiyou_count)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_del_qiyou = QPushButton(self.groupBox_qiyou)
        self.btn_del_qiyou.setObjectName(u"btn_del_qiyou")
        self.btn_del_qiyou.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout.addWidget(self.btn_del_qiyou)

        self.btn_add_qiyou = QPushButton(self.groupBox_qiyou)
        self.btn_add_qiyou.setObjectName(u"btn_add_qiyou")
        self.btn_add_qiyou.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout.addWidget(self.btn_add_qiyou)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.groupBox_qiyou)

        self.groupBox_chongdianzhuang = QGroupBox(self.centralwidget)
        self.groupBox_chongdianzhuang.setObjectName(u"groupBox_chongdianzhuang")
        self.groupBox_chongdianzhuang.setToolTipDuration(-1)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_chongdianzhuang)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.listWidget_chongdianzhuang = QListWidget(self.groupBox_chongdianzhuang)
        self.listWidget_chongdianzhuang.setObjectName(u"listWidget_chongdianzhuang")

        self.verticalLayout_3.addWidget(self.listWidget_chongdianzhuang)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.label_chongdianzhuang_count = QLabel(self.groupBox_chongdianzhuang)
        self.label_chongdianzhuang_count.setObjectName(u"label_chongdianzhuang_count")

        self.horizontalLayout_7.addWidget(self.label_chongdianzhuang_count)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.btn_del_chongdianzhuang = QPushButton(self.groupBox_chongdianzhuang)
        self.btn_del_chongdianzhuang.setObjectName(u"btn_del_chongdianzhuang")
        self.btn_del_chongdianzhuang.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_7.addWidget(self.btn_del_chongdianzhuang)

        self.btn_add_chongdianzhuang = QPushButton(self.groupBox_chongdianzhuang)
        self.btn_add_chongdianzhuang.setObjectName(u"btn_add_chongdianzhuang")
        self.btn_add_chongdianzhuang.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_7.addWidget(self.btn_add_chongdianzhuang)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.verticalLayout_5.addWidget(self.groupBox_chongdianzhuang)

        self.groupBox_tongxun = QGroupBox(self.centralwidget)
        self.groupBox_tongxun.setObjectName(u"groupBox_tongxun")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_tongxun)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listWidget_tongxun = QListWidget(self.groupBox_tongxun)
        self.listWidget_tongxun.setObjectName(u"listWidget_tongxun")

        self.verticalLayout_2.addWidget(self.listWidget_tongxun)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_tongxun_count = QLabel(self.groupBox_tongxun)
        self.label_tongxun_count.setObjectName(u"label_tongxun_count")

        self.horizontalLayout_3.addWidget(self.label_tongxun_count)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_del_tongxun = QPushButton(self.groupBox_tongxun)
        self.btn_del_tongxun.setObjectName(u"btn_del_tongxun")
        self.btn_del_tongxun.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_3.addWidget(self.btn_del_tongxun)

        self.btn_add_tongxun = QPushButton(self.groupBox_tongxun)
        self.btn_add_tongxun.setObjectName(u"btn_add_tongxun")
        self.btn_add_tongxun.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_3.addWidget(self.btn_add_tongxun)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addWidget(self.groupBox_tongxun)

        self.groupBox_shineijiaotong = QGroupBox(self.centralwidget)
        self.groupBox_shineijiaotong.setObjectName(u"groupBox_shineijiaotong")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_shineijiaotong)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.listWidget_shineijiaotong = QListWidget(self.groupBox_shineijiaotong)
        self.listWidget_shineijiaotong.setObjectName(u"listWidget_shineijiaotong")

        self.verticalLayout_4.addWidget(self.listWidget_shineijiaotong)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_shineijiaotong_count = QLabel(self.groupBox_shineijiaotong)
        self.label_shineijiaotong_count.setObjectName(u"label_shineijiaotong_count")

        self.horizontalLayout_2.addWidget(self.label_shineijiaotong_count)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_del_shineijiaotong = QPushButton(self.groupBox_shineijiaotong)
        self.btn_del_shineijiaotong.setObjectName(u"btn_del_shineijiaotong")
        self.btn_del_shineijiaotong.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_2.addWidget(self.btn_del_shineijiaotong)

        self.btn_add_shineijiaotong = QPushButton(self.groupBox_shineijiaotong)
        self.btn_add_shineijiaotong.setObjectName(u"btn_add_shineijiaotong")
        self.btn_add_shineijiaotong.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_2.addWidget(self.btn_add_shineijiaotong)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.groupBox_shineijiaotong)


        self.verticalLayout1.addLayout(self.verticalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")

        self.horizontalLayout_4.addWidget(self.btn_clear)

        self.btn_web_check = QPushButton(self.centralwidget)
        self.btn_web_check.setObjectName(u"btn_web_check")

        self.horizontalLayout_4.addWidget(self.btn_web_check)

        self.btn_export_table = QPushButton(self.centralwidget)
        self.btn_export_table.setObjectName(u"btn_export_table")

        self.horizontalLayout_4.addWidget(self.btn_export_table)


        self.verticalLayout1.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout1)

        self.verticalLayout2 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout2.setSpacing(-1)
#endif
        self.verticalLayout2.setObjectName(u"verticalLayout2")
        self.verticalLayout2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_shuilv = QLineEdit(self.centralwidget)
        self.lineEdit_shuilv.setObjectName(u"lineEdit_shuilv")
        self.lineEdit_shuilv.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_shuilv, 9, 1, 1, 1)

        self.lineEdit_price = QLineEdit(self.centralwidget)
        self.lineEdit_price.setObjectName(u"lineEdit_price")
        self.lineEdit_price.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_price, 7, 1, 1, 1)

        self.lineEdit_total = QLineEdit(self.centralwidget)
        self.lineEdit_total.setObjectName(u"lineEdit_total")
        self.lineEdit_total.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_total, 6, 1, 1, 1)

        self.lineEdit_number = QLineEdit(self.centralwidget)
        self.lineEdit_number.setObjectName(u"lineEdit_number")
        self.lineEdit_number.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_number, 2, 1, 1, 1)

        self.lineEdit_check6 = QLineEdit(self.centralwidget)
        self.lineEdit_check6.setObjectName(u"lineEdit_check6")
        self.lineEdit_check6.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_check6, 5, 1, 1, 1)

        self.lineEdit_check = QLineEdit(self.centralwidget)
        self.lineEdit_check.setObjectName(u"lineEdit_check")
        self.lineEdit_check.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_check, 4, 1, 1, 1)

        self.btn_company = QPushButton(self.centralwidget)
        self.btn_company.setObjectName(u"btn_company")

        self.gridLayout_2.addWidget(self.btn_company, 10, 0, 1, 1)

        self.btn_date = QPushButton(self.centralwidget)
        self.btn_date.setObjectName(u"btn_date")

        self.gridLayout_2.addWidget(self.btn_date, 3, 0, 1, 1)

        self.btn_price = QPushButton(self.centralwidget)
        self.btn_price.setObjectName(u"btn_price")

        self.gridLayout_2.addWidget(self.btn_price, 7, 0, 1, 1)

        self.btn_type = QPushButton(self.centralwidget)
        self.btn_type.setObjectName(u"btn_type")

        self.gridLayout_2.addWidget(self.btn_type, 0, 0, 1, 1)

        self.btn_check6 = QPushButton(self.centralwidget)
        self.btn_check6.setObjectName(u"btn_check6")

        self.gridLayout_2.addWidget(self.btn_check6, 5, 0, 1, 1)

        self.btn_total = QPushButton(self.centralwidget)
        self.btn_total.setObjectName(u"btn_total")

        self.gridLayout_2.addWidget(self.btn_total, 6, 0, 1, 1)

        self.btn_taxpayer_id = QPushButton(self.centralwidget)
        self.btn_taxpayer_id.setObjectName(u"btn_taxpayer_id")

        self.gridLayout_2.addWidget(self.btn_taxpayer_id, 11, 0, 1, 1)

        self.btn_shuilv = QPushButton(self.centralwidget)
        self.btn_shuilv.setObjectName(u"btn_shuilv")

        self.gridLayout_2.addWidget(self.btn_shuilv, 9, 0, 1, 1)

        self.btn_check = QPushButton(self.centralwidget)
        self.btn_check.setObjectName(u"btn_check")

        self.gridLayout_2.addWidget(self.btn_check, 4, 0, 1, 1)

        self.btn_code = QPushButton(self.centralwidget)
        self.btn_code.setObjectName(u"btn_code")

        self.gridLayout_2.addWidget(self.btn_code, 1, 0, 1, 1)

        self.lineEdit_type = QLineEdit(self.centralwidget)
        self.lineEdit_type.setObjectName(u"lineEdit_type")
        self.lineEdit_type.setEnabled(True)
        self.lineEdit_type.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_type, 0, 1, 1, 1)

        self.btn_tax = QPushButton(self.centralwidget)
        self.btn_tax.setObjectName(u"btn_tax")

        self.gridLayout_2.addWidget(self.btn_tax, 8, 0, 1, 1)

        self.lineEdit_taxpayer_id = QLineEdit(self.centralwidget)
        self.lineEdit_taxpayer_id.setObjectName(u"lineEdit_taxpayer_id")
        self.lineEdit_taxpayer_id.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_taxpayer_id, 11, 1, 1, 1)

        self.lineEdit_company = QLineEdit(self.centralwidget)
        self.lineEdit_company.setObjectName(u"lineEdit_company")
        self.lineEdit_company.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_company, 10, 1, 1, 1)

        self.lineEdit_tax = QLineEdit(self.centralwidget)
        self.lineEdit_tax.setObjectName(u"lineEdit_tax")
        self.lineEdit_tax.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_tax, 8, 1, 1, 1)

        self.btn_number = QPushButton(self.centralwidget)
        self.btn_number.setObjectName(u"btn_number")

        self.gridLayout_2.addWidget(self.btn_number, 2, 0, 1, 1)

        self.lineEdit_date = QLineEdit(self.centralwidget)
        self.lineEdit_date.setObjectName(u"lineEdit_date")
        self.lineEdit_date.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_date, 3, 1, 1, 1)

        self.lineEdit_code = QLineEdit(self.centralwidget)
        self.lineEdit_code.setObjectName(u"lineEdit_code")
        self.lineEdit_code.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_code, 1, 1, 1, 1)


        self.verticalLayout2.addLayout(self.gridLayout_2)

        self.textEdit_show = QTextEdit(self.centralwidget)
        self.textEdit_show.setObjectName(u"textEdit_show")
        sizePolicy.setHeightForWidth(self.textEdit_show.sizePolicy().hasHeightForWidth())
        self.textEdit_show.setSizePolicy(sizePolicy)
        self.textEdit_show.setMinimumSize(QSize(300, 100))

        self.verticalLayout2.addWidget(self.textEdit_show)

        self.img_label = QLabel(self.centralwidget)
        self.img_label.setObjectName(u"img_label")
        sizePolicy.setHeightForWidth(self.img_label.sizePolicy().hasHeightForWidth())
        self.img_label.setSizePolicy(sizePolicy)
        self.img_label.setMinimumSize(QSize(300, 0))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout2.addWidget(self.img_label)

        self.verticalLayout2.setStretch(1, 1)

        self.horizontalLayout_6.addLayout(self.verticalLayout2)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d:", None))
        self.groupBox_qiyou.setTitle(QCoreApplication.translate("MainWindow", u"\u6c7d\u6cb9\u8d39", None))
        self.label_qiyou_count.setText(QCoreApplication.translate("MainWindow", u"0\u5f20", None))
        self.btn_del_qiyou.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_add_qiyou.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.groupBox_chongdianzhuang.setTitle(QCoreApplication.translate("MainWindow", u"\u5145\u7535\u6869\u7535\u8d39", None))
        self.label_chongdianzhuang_count.setText(QCoreApplication.translate("MainWindow", u"0\u5f20", None))
        self.btn_del_chongdianzhuang.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_add_chongdianzhuang.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.groupBox_tongxun.setTitle(QCoreApplication.translate("MainWindow", u"\u901a\u8baf\u8d39", None))
        self.label_tongxun_count.setText(QCoreApplication.translate("MainWindow", u"0\u5f20", None))
        self.btn_del_tongxun.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_add_tongxun.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.groupBox_shineijiaotong.setTitle(QCoreApplication.translate("MainWindow", u"\u5e02\u5185\u4ea4\u901a\u8d39", None))
        self.label_shineijiaotong_count.setText(QCoreApplication.translate("MainWindow", u"0\u5f20", None))
        self.btn_del_shineijiaotong.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_add_shineijiaotong.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.btn_web_check.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u9875\u67e5\u9a8c", None))
        self.btn_export_table.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u6e05\u5355", None))
        self.btn_company.setText(QCoreApplication.translate("MainWindow", u"\u9500\u65b9\u540d\u79f0", None))
        self.btn_date.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u7968\u65e5\u671f", None))
        self.btn_price.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u989d", None))
        self.btn_type.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u7968\u7c7b\u578b", None))
        self.btn_check6.setText(QCoreApplication.translate("MainWindow", u"\u6821\u9a8c\u7801\u540e6\u4f4d", None))
        self.btn_total.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u7a0e\u5408\u8ba1", None))
        self.btn_taxpayer_id.setText(QCoreApplication.translate("MainWindow", u"\u7eb3\u7a0e\u4eba\u8bc6\u522b\u53f7", None))
        self.btn_shuilv.setText(QCoreApplication.translate("MainWindow", u"\u7a0e\u7387", None))
        self.btn_check.setText(QCoreApplication.translate("MainWindow", u"\u6821\u9a8c\u7801", None))
        self.btn_code.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u7968\u4ee3\u7801", None))
        self.btn_tax.setText(QCoreApplication.translate("MainWindow", u"\u7a0e\u989d", None))
        self.btn_number.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u7968\u53f7\u7801", None))
        self.img_label.setText("")
    # retranslateUi

