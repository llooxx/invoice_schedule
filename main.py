# 导入sys
from pathlib import Path
import sys
import os
import threading
from invoice import *
import webbrowser
import csv
from urllib.parse import urlparse
# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QListWidgetItem, QFileDialog
from PySide6.QtGui import QDragEnterEvent, QIcon
from PySide6.QtCore import Qt, QCoreApplication

# 导入我们生成的界面
from qtui import Ui_MainWindow
import sys
import os


# def resource_path(relative_path):
#     """获取资源文件的绝对路径，兼容开发和编译后的环境"""
#     if getattr(sys, "frozen", False):
#         # 在编译后的环境中
#         base_path = sys._MEIPASS  # Nuitka有类似的属性，如 sys.frozen
#     else:
#         # 在开发环境中
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)


zh_type = {
    "qiyou": "汽油费",
    "shineijiaotong": "市内交通费",
    "tongxun": "通讯费",
    "chongdianzhuang": "充电桩电费",
}


class CustomWidgetItem(QWidget):
    def __init__(self, text: str):
        super().__init__()
        self.text = text
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.label = QLabel(self.text)
        self.button = QPushButton("×")
        layout.addWidget(self.label)
        layout.addWidget(self.button)


# 继承QWidget类，以获取其属性和方法
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        myLabel = QLabel()
        myLabel.setText("作者：乱想乱想 E-mail:965035290@qq.com")
        self.ui.statusbar.addWidget(myLabel)


        self.ui.groupBox_qiyou.setAcceptDrops(True)
        self.ui.groupBox_shineijiaotong.setAcceptDrops(True)
        self.ui.groupBox_chongdianzhuang.setAcceptDrops(True)
        self.ui.groupBox_tongxun.setAcceptDrops(True)

        self.ui.groupBox_qiyou.dragEnterEvent = self.groupBox_dragEnterEvent
        self.ui.groupBox_shineijiaotong.dragEnterEvent = self.groupBox_dragEnterEvent
        self.ui.groupBox_chongdianzhuang.dragEnterEvent = self.groupBox_dragEnterEvent
        self.ui.groupBox_tongxun.dragEnterEvent = self.groupBox_dragEnterEvent

        self.ui.groupBox_qiyou.dropEvent = lambda e: self.groupBox_dropEvent(e, "qiyou")
        self.ui.groupBox_shineijiaotong.dropEvent = lambda e: self.groupBox_dropEvent(e, "shineijiaotong")
        self.ui.groupBox_chongdianzhuang.dropEvent = lambda e: self.groupBox_dropEvent(e, "chongdianzhuang")
        self.ui.groupBox_tongxun.dropEvent = lambda e: self.groupBox_dropEvent(e, "tongxun")
        # 只可读
        self.ui.lineEdit_code.setReadOnly(True)
        self.ui.lineEdit_check.setReadOnly(True)
        self.ui.lineEdit_number.setReadOnly(True)
        self.ui.lineEdit_date.setReadOnly(True)
        self.ui.lineEdit_price.setReadOnly(True)
        self.ui.lineEdit_tax.setReadOnly(True)
        self.ui.lineEdit_total.setReadOnly(True)
        self.ui.lineEdit_shuilv.setReadOnly(True)
        self.ui.lineEdit_type.setReadOnly(True)

        self.all_listWidget = {
            "qiyou": self.ui.listWidget_qiyou,
            "shineijiaotong": self.ui.listWidget_shineijiaotong,
            "chongdianzhuang": self.ui.listWidget_chongdianzhuang,
            "tongxun": self.ui.listWidget_tongxun,
        }
        self.all_count_label = {
            "qiyou": {
                "label": self.ui.label_qiyou_count,
                "count": 0,
            },
            "shineijiaotong": {
                "label": self.ui.label_shineijiaotong_count,
                "count": 0,
            },
            "chongdianzhuang": {
                "label": self.ui.label_chongdianzhuang_count,
                "count": 0,
            },
            "tongxun": {
                "label": self.ui.label_tongxun_count,
                "count": 0,
            },
        }
        # 列表item单击解析
        self.all_listWidget["qiyou"].itemClicked.connect(lambda item: self.handleClickedItem(item, "qiyou"))
        self.all_listWidget["shineijiaotong"].itemClicked.connect(lambda item: self.handleClickedItem(item, "shineijiaotong"))
        self.all_listWidget["chongdianzhuang"].itemClicked.connect(lambda item: self.handleClickedItem(item, "chongdianzhuang"))
        self.all_listWidget["tongxun"].itemClicked.connect(lambda item: self.handleClickedItem(item, "tongxun"))
        # 列表item双击删除
        self.all_listWidget["qiyou"].itemDoubleClicked.connect(lambda item: self.handleDoubleClickedItem(item, "qiyou"))
        self.all_listWidget["shineijiaotong"].itemDoubleClicked.connect(lambda item: self.handleDoubleClickedItem(item, "shineijiaotong"))
        self.all_listWidget["chongdianzhuang"].itemDoubleClicked.connect(lambda item: self.handleDoubleClickedItem(item, "chongdianzhuang"))
        self.all_listWidget["tongxun"].itemDoubleClicked.connect(lambda item: self.handleDoubleClickedItem(item, "tongxun"))
        # 按钮
        self.ui.btn_clear.clicked.connect(self.btn_clear_clicked)
        self.ui.btn_export_table.clicked.connect(self.export_table)
        self.ui.btn_web_check.clicked.connect(lambda: webbrowser.open("https://inv-veri.chinatax.gov.cn"))
        self.ui.btn_check.clicked.connect(lambda: QApplication.clipboard().setText(self.ui.lineEdit_check.text()))
        self.ui.btn_code.clicked.connect(lambda: QApplication.clipboard().setText(self.ui.lineEdit_code.text()))
        self.ui.btn_number.clicked.connect(lambda: QApplication.clipboard().setText(self.ui.lineEdit_number.text()))
        self.ui.btn_date.clicked.connect(lambda: QApplication.clipboard().setText(self.ui.lineEdit_date.text()))
        self.ui.btn_price.clicked.connect(lambda: QApplication.clipboard().setText(self.ui.lineEdit_price.text()))
        self.ui.btn_tax.clicked.connect(lambda: QApplication.clipboard().setText(self.ui.lineEdit_tax.text()))
        self.ui.btn_total.clicked.connect(lambda: QApplication.clipboard().setText(self.ui.lineEdit_total.text()))
        self.ui.btn_shuilv.clicked.connect(lambda: QApplication.clipboard().setText(self.ui.lineEdit_shuilv.text()))
        self.ui.btn_type.clicked.connect(lambda: QApplication.clipboard().setText(self.ui.lineEdit_type.text()))
        self.ui.btn_add_qiyou.clicked.connect(lambda: self.btn_add_clicked("qiyou"))
        self.ui.btn_add_shineijiaotong.clicked.connect(lambda: self.btn_add_clicked("shineijiaotong"))
        self.ui.btn_add_chongdianzhuang.clicked.connect(lambda: self.btn_add_clicked("chongdianzhuang"))
        self.ui.btn_add_tongxun.clicked.connect(lambda: self.btn_add_clicked("tongxun"))

    def btn_add_clicked(self, type: str):
        # 设置文件过滤器，允许选择 PDF 文件
        filter = "PDF Files (*.pdf)"
        file_paths = QFileDialog.getOpenFileNames(QMainWindow(), f"选择{zh_type[type]}发票", "", filter)[0]
        if len(file_paths) == 0:
            return
        for file_path in file_paths:
            self.add_file(Path(file_path), type)

    def btn_clear_clicked(self):
        for type in self.all_listWidget.keys():
            self.all_listWidget[type].clear()

    def handleClickedItem(self, item: QListWidgetItem, type: str):
        self.ui.lineEdit_code.clear()
        self.ui.lineEdit_check.clear()
        self.ui.lineEdit_number.clear()
        self.ui.lineEdit_date.clear()
        self.ui.lineEdit_price.clear()
        self.ui.lineEdit_tax.clear()
        self.ui.lineEdit_total.clear()
        self.ui.lineEdit_shuilv.clear()
        self.ui.lineEdit_type.clear()
        file_path = item.data(Qt.ItemDataRole.UserRole)
        invoice = readPDF(file_path)
        if invoice is not None:
            self.ui.lineEdit_code.setText(invoice.code if invoice.code is not None else "")
            self.ui.lineEdit_check.setText(invoice.check if invoice.check is not None else "")
            self.ui.lineEdit_number.setText(invoice.number if invoice.number is not None else "")
            self.ui.lineEdit_date.setText(invoice.date if invoice.date is not None else "")
            self.ui.lineEdit_price.setText(invoice.price if invoice.price is not None else "")
            self.ui.lineEdit_tax.setText(invoice.tax if invoice.tax is not None else "")
            self.ui.lineEdit_total.setText(invoice.total if invoice.total is not None else "")
            self.ui.lineEdit_shuilv.setText(str(invoice.max_shuilv) if invoice.max_shuilv is not None else "")
            self.ui.lineEdit_type.setText(invoice.type if invoice.type is not None else "")

            self.ui.textEdit_show.clear()
            self.ui.textEdit_show.append(f"文件路径：{file_path}\n")
            self.ui.textEdit_show.append(str(invoice))

    def handleDoubleClickedItem(self, item: QListWidgetItem, type: str):
        choose_listWidget = self.all_listWidget[type]
        choose_listWidget.takeItem(choose_listWidget.currentRow())
        self.all_count_label[type]["count"] -= 1
        self.all_count_label[type]["label"].setText(str(self.all_count_label[type]["count"]) + "张")

    def groupBox_dragEnterEvent(self, e: QDragEnterEvent):
        e.accept() if e.mimeData().hasText() else e.ignore()

    def groupBox_dropEvent(self, e: QDragEnterEvent, type: str):
        filePaths = [Path(urlparse(filePath).path) for filePath in e.mimeData().text().split("\n") if filePath and filePath.endswith(".pdf")]  # 去除文件地址前缀的特定字符
        for file_path in filePaths:
            self.add_file(file_path, type)

    def add_file(self, file_path: Path, type: str):
        choose_listWidget = self.all_listWidget[type]
        item = QListWidgetItem(file_path.name)
        item.setData(Qt.ItemDataRole.UserRole, str(file_path.absolute()))
        if len(choose_listWidget.findItems(file_path.name, Qt.MatchFlag.MatchExactly)) == 0:
            choose_listWidget.addItem(item)
            self.all_count_label[type]["count"] += 1
            self.all_count_label[type]["label"].setText(str(self.all_count_label[type]["count"]) + "张")

    def export_table(self):
        # 打开文件夹对话框
        folder_path = QFileDialog.getExistingDirectory(window, "选择文件夹")
        if folder_path == "":
            return
        self.ui.textEdit_show.clear()
        owner_name = self.ui.lineEdit_username.text()

        def copy_file(fapiao: Invoice, file_path: Path, output_dir: Path, type: str) -> Path:
            filename = f"{owner_name}_{fapiao.date}_{zh_type[type]}_{fapiao.total}.pdf"
            num = 1
            if Path(output_dir, filename).exists():
                while num:
                    filename = f"{owner_name}_{fapiao.date}_{zh_type[type]}_{fapiao.total}_{num}.pdf"
                    if Path(output_dir, filename).exists():
                        num += 1
                    else:
                        break
            Path(output_dir, filename).write_bytes(file_path.read_bytes())
            return Path(output_dir, filename)

        def do():
            manifest = open(os.path.join(folder_path, "电子发票清单.csv"), "w", encoding="utf-8", newline="")
            manifest_csv = csv.writer(
                manifest,
            )
            manifest_csv.writerow(["发票介质", "发票日期", "发票代码", "发票号码", "占用票额（发票票面全额）", "税率", "占用税额", "电子发票对应清单序号"])

            for type in self.all_listWidget.keys():
                choose_listWidget = self.all_listWidget[type]
                for i in range(choose_listWidget.count()):
                    item = choose_listWidget.item(i)
                    file_path = item.data(Qt.ItemDataRole.UserRole)
                    invoice = readPDF(file_path)
                    if invoice is not None:
                        self.ui.textEdit_show.append(f"文件路径：{file_path}\n")
                        self.ui.textEdit_show.append(f"{invoice}\n")
                        output_path: Path = copy_file(invoice, Path(file_path), Path(folder_path), type)

                        manifest_csv.writerow([invoice.type, invoice.date, invoice.code, invoice.number, invoice.total, invoice.max_shuilv, invoice.tax, output_path.name])
            manifest.close()

        threading.Thread(target=do).start()


# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = MyWidget()
    window.setWindowTitle(QCoreApplication.translate("widget", "发票清单", None))
    # window.setWindowIcon(QIcon(resource_path("img/invoice.ico")))
    window.show()

    # 结束QApplication
    sys.exit(app.exec())
