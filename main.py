from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets, QtGui, QtPrintSupport

from rangeslider import QRangeSlider


class InsertDialog(QDialog):
    """Класс для добавления книги в базу данных"""

    def __init__(self, num, *args, **kwargs):
        """Окно интерфейса для добавления книги"""
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Зарегистрировать")

        self.setWindowTitle("Добавить книгу")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        self.QBtn.clicked.connect(self.addbook)

        layout = QVBoxLayout()

        self.genreinput = QComboBox()
        self.genreinput.addItem("Классическая литература")
        self.genreinput.addItem("Детективы")
        self.genreinput.addItem("Фэнтези")
        self.genreinput.addItem("Фантастика")
        self.genreinput.addItem("Ужасы, мистика")
        self.genreinput.addItem("Поэзия и драматургия")
        self.genreinput.addItem("Наука и техника")
        self.genreinput.addItem("Образование")
        self.genreinput.addItem("Книги на иностранных языках")
        layout.addWidget(self.genreinput)

        self.authorinput = QLineEdit()
        self.authorinput.setPlaceholderText("Автор")
        layout.addWidget(self.authorinput)

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Название")
        layout.addWidget(self.nameinput)

        self.quantityinput = QLineEdit()
        self.quantityinput.setPlaceholderText("Количество")
        layout.addWidget(self.quantityinput)

        self.priceinput = QLineEdit()
        self.priceinput.setPlaceholderText("Цена")
        layout.addWidget(self.priceinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

        if num:
            self.darkMode()
        else:
            self.lightMode()

    def darkMode(self):
        self.setStyleSheet("background-color: rgb(44, 49, 60, 255);"
                           "color: rgb(255, 255, 255);"
                           "alternate-background-color: rgb(55, 61, 75, 255);"
                           "selection-background-color: rgb(108, 120, 151);")

    def lightMode(self):
        self.setStyleSheet("")

    def addbook(self):
        """Функция для добавления книги в базу данных"""

        genre = ""
        author = ""
        name = ""
        quantity = -1
        price = -1

        genre = self.genreinput.itemText(self.genreinput.currentIndex())
        author = self.authorinput.text()
        name = self.nameinput.text()
        quantity = self.quantityinput.text()
        price = self.priceinput.text()

        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO books (genre, author, name, quantity, price) VALUES (?,?,?,?,?)",
                           (genre, author, name, quantity, price))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Успешно', 'Книга успешно добавлена.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Ошибка', 'Не удалось добавить книгу.')


class SearchDialog(QDialog):
    """Класс для поиска книги в базе данных"""

    def __init__(self, num, *args, **kwargs):
        """Окно интерфейса для поиска книги"""
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Поиск")

        self.setWindowTitle("Найти книгу")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchbook)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("ID")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

        if num:
            self.darkMode()
        else:
            self.lightMode()

    def darkMode(self):
        self.setStyleSheet("background-color: rgb(44, 49, 60, 255);"
                           "color: rgb(255, 255, 255);"
                           "alternate-background-color: rgb(55, 61, 75, 255);"
                           "selection-background-color: rgb(108, 120, 151);")

    def lightMode(self):
        self.setStyleSheet("")

    def searchbook(self):
        """Функция для поиска книги в базе данных"""
        searchrol = ""
        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from books WHERE roll=" + str(searchrol))
            row = result.fetchone()
            serachresult = "ID: " + str(row[0]) + '\n' + "Жанр: " + str(row[1]) + '\n' + "Автор: " + str(
                row[2]) + '\n' + "Название: " + str(row[3]) + '\n' + "Кол-во: " + str(row[4]) + '\n' + "Цена: " + str(
                row[5])
            QMessageBox.information(QMessageBox(), 'Успешно', serachresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Ошибка', 'Не удалось найти книгу.')


class DeleteDialog(QDialog):
    """Класс для удаления книги из базы данных"""

    def __init__(self, num, *args, **kwargs):
        """Окно интерфейса для удаления книги"""
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Удалить")

        self.setWindowTitle("Удалить книгу")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deletebook)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("ID")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

        if num:
            self.darkMode()
        else:
            self.lightMode()

    def darkMode(self):
        self.setStyleSheet("background-color: rgb(44, 49, 60, 255);"
                           "color: rgb(255, 255, 255);"
                           "alternate-background-color: rgb(55, 61, 75, 255);"
                           "selection-background-color: rgb(108, 120, 151);")

    def lightMode(self):
        self.setStyleSheet("")

    def deletebook(self):
        """Функция для удаления книги из базы данных"""
        delrol = ""
        delrol = self.deleteinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from books WHERE roll=" + str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Успешно', 'Книга успешно удалена.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Ошибка', 'Не удалось удалить книгу.')


class LoginDialog(QDialog):
    """Класс для входа в систему"""

    def __init__(self, *args, **kwargs):
        """Окно интерфейса для авторизации"""
        super(LoginDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(300)
        self.setFixedHeight(120)

        layout = QVBoxLayout()

        self.passinput = QLineEdit()
        self.passinput.setEchoMode(QLineEdit.Password)
        self.passinput.setPlaceholderText("Введите пароль")
        self.QBtn = QPushButton()
        self.QBtn.setText("Войти")
        self.setWindowTitle('Авторизация')
        self.QBtn.clicked.connect(self.login)

        title = QLabel("Вход")
        font = title.font()
        font.setPointSize(16)
        title.setFont(font)

        layout.addWidget(title)
        layout.addWidget(self.passinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def login(self):
        """Функция для входа в систему"""
        if self.passinput.text() == "123":
            self.accept()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Неверный пароль.')


class AboutDialog(QDialog):
    """Класс для показа информации о базе данных и владельце"""

    def __init__(self, num, *args, **kwargs):
        """Окно интерфейса для показа информации"""
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(300)
        self.setFixedHeight(250)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.setFixedWidth(50)

        layout = QVBoxLayout()

        title = QLabel("Книжный магазин")
        font = title.font()
        font.setPointSize(16)
        title.setFont(font)
        title.setAlignment(Qt.AlignCenter)

        labelpic = QLabel()
        pixmap = QPixmap('icons/logo.png')
        pixmap = pixmap.scaledToWidth(250)
        pixmap = pixmap.scaledToHeight(115)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(120)
        labelpic.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(QLabel("Версия 1.0"))
        layout.addWidget(QLabel("Автор:\tСлюсарева В.А.\n2021 год"))
        layout.addWidget(labelpic)
        layout.addWidget(self.buttonBox, alignment=QtCore.Qt.AlignRight)

        self.setLayout(layout)

        if num:
            self.darkMode()
        else:
            self.lightMode()

    def darkMode(self):
        self.setStyleSheet("background-color: rgb(44, 49, 60, 255);"
                           "color: rgb(255, 255, 255);"
                           "alternate-background-color: rgb(55, 61, 75, 255);"
                           "selection-background-color: rgb(108, 120, 151);")

    def lightMode(self):
        self.setStyleSheet("")


class MainWindow(QMainWindow):
    """Класс для реализации главного окна пользовательского интерфейса."""

    def __init__(self, *args, **kwargs):
        """Интерфейс главного окна разрабатываемого проекта.

        Функция, объединяющая функционал всей системы.
        В ней создаются:
        - интерактивная панель инструментов
        - строка меню
        В данном окне отображается таблица с данными и осуществляется работа с ней.

        """
        super(MainWindow, self).__init__(*args, **kwargs)

        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute(
            "CREATE TABLE IF NOT EXISTS books(roll INTEGER PRIMARY KEY AUTOINCREMENT, genre TEXT, "
            "author TEXT, name TEXT, quantity INTEGER,price INTEGER)")
        self.c.close()

        self.file_menu = self.menuBar().addMenu("&Файл")
        self.help_menu = self.menuBar().addMenu("&Информация")

        self.setWindowTitle("Информационная система книжного  магазина")

        self.setMinimumSize(800, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setStyleSheet("color: rgb(44, 49, 60, 255);")
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("ID", "Жанр", "Автор", "Название", "Кол-во", "Цена"))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        self.btn_ac_addbook = QAction(QIcon("icons/d_add.png"), "Добавить", self)
        self.btn_ac_addbook.triggered.connect(self.insert)
        self.btn_ac_addbook.setStatusTip("Добавить книгу")
        toolbar.addAction(self.btn_ac_addbook)

        self.btn_ac_refresh = QAction(QIcon("icons/d_refresh.png"), "Обновить", self)
        self.btn_ac_refresh.triggered.connect(self.loaddata)
        self.btn_ac_refresh.setStatusTip("Обновить таблицу")
        toolbar.addAction(self.btn_ac_refresh)

        self.btn_ac_search = QAction(QIcon("icons/d_search.png"), "Поиск", self)
        self.btn_ac_search.triggered.connect(self.search)
        self.btn_ac_search.setStatusTip("Найти книгу")
        toolbar.addAction(self.btn_ac_search)

        self.btn_ac_delete = QAction(QIcon("icons/d_trash.png"), "Удалить", self)
        self.btn_ac_delete.triggered.connect(self.delete)
        self.btn_ac_delete.setStatusTip("Удалить книгу")
        toolbar.addAction(self.btn_ac_delete)

        about_action = QAction("О программе", self)
        about_action.triggered.connect(self.about)
        self.help_menu.addAction(about_action)

        self.tableWidgetHeader = self.tableWidget.horizontalHeader()
        self.tableWidgetHeader.sectionClicked.connect(self.columnfilterclicked)
        self.keywords = dict([(i, []) for i in range(self.tableWidget.columnCount())])
        self.checkBoxs = []
        self.col = None

        toolbar.addSeparator()

        self.search = QLineEdit(self)
        self.search.textChanged.connect(self.findName)
        self.search.setPlaceholderText("Введите текст")
        self.search.setFixedWidth(150)
        toolbar.addWidget(self.search)

        self.btn_cb = QComboBox()
        self.btn_cb.addItems(["{}".format(self.tableWidget.horizontalHeaderItem(x).text()) for x in
                              range(self.tableWidget.columnCount())])
        toolbar.addWidget(self.btn_cb)

        toolbar.addSeparator()

        pdf = QAction("Сохранить PDF", self,
                      priority=QAction.LowPriority,
                      shortcut=Qt.CTRL + Qt.Key_D)
        pdf.triggered.connect(self.to_pdf)

        self.file_menu.addAction(pdf)

        dtheme = QAction("Тёмная тема", self,
                         priority=QAction.LowPriority,
                         shortcut=Qt.CTRL + Qt.Key_N)
        dtheme.triggered.connect(self.darkTheme)

        ltheme = QAction("Светлая тема", self,
                         priority=QAction.LowPriority,
                         shortcut=Qt.CTRL + Qt.Key_L)
        ltheme.triggered.connect(self.dayTheme)

        switchTheme = QMenu('Поменять тему', self)
        switchTheme.addAction(dtheme)
        switchTheme.addAction(ltheme)
        self.file_menu.addMenu(switchTheme)

        self.price1 = QAction("В наличии", self)
        self.price1.triggered.connect(self.inshop)
        self.price1.setCheckable(True)

        self.price2 = QAction("Все книги", self)
        self.price2.triggered.connect(self.allshop)
        self.price2.setCheckable(True)
        self.price2.setChecked(True)

        menu = QtWidgets.QMenu(self)
        button = QtWidgets.QPushButton()
        button.setText("Фильтр")
        button.setMenu(menu)
        toolbar.addWidget(button)

        text = QLabel()
        text.setText("    Наличие в магазине")
        action = QtWidgets.QWidgetAction(menu)
        action.setDefaultWidget(text)
        menu.addAction(action)

        menu.addSeparator()
        menu.addAction(self.price1)
        menu.addAction(self.price2)
        menu.addSeparator()

        self.scrll = QRangeSlider()
        self.scrll.startValueChanged.connect(self.priceSort)
        self.scrll.endValueChanged.connect(self.priceSort)
        self.scrll.setFixedWidth(250)
        self.scrll.setFixedHeight(25)

        txt = QLabel()
        txt.setText("    Диапазон цен")
        action = QtWidgets.QWidgetAction(menu)
        action.setDefaultWidget(txt)
        menu.addAction(action)
        menu.addSeparator()

        Action = QtWidgets.QWidgetAction(menu)
        Action.setDefaultWidget(self.scrll)
        menu.addAction(Action)

        btn = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
                                         QtCore.Qt.Horizontal, menu)
        Action = QtWidgets.QWidgetAction(menu)
        Action.setDefaultWidget(btn)
        menu.addSeparator()
        menu.addAction(Action)

        btn.accepted.connect(menu.close)
        btn.rejected.connect(menu.close)

        self.num = False

    def filt(self):
        if self.tableWidget.rowCount()!=0:
            data_unique = []
            for i in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(i, 5)
                if int(item.text()) not in data_unique:
                    data_unique.append(int(item.text()))
            data_unique.sort()
            min = int(data_unique.__getitem__(0)) - 50
            max = int(data_unique.__getitem__(len(data_unique) - 1)) + 50
            self.scrll.setMin(min)
            self.scrll.setMax(max)
            self.scrll.setRange(min, max)

    def darkTheme(self):
        self.help_menu.setStyleSheet("background-color: rgb(55, 61, 75, 255);"
                                     "selection-background-color: rgb(108, 120, 151);")
        self.file_menu.setStyleSheet("background-color: rgb(55, 61, 75, 255);"
                                     "selection-background-color: rgb(108, 120, 151);")
        self.window().setStyleSheet("background-color: rgb(44, 49, 60, 255);"
                                    "color: rgb(255, 255, 255);"
                                    "alternate-background-color: rgb(44, 49, 60, 255);"
                                    "selection-background-color: rgb(108, 120, 151);")
        self.setStyleSheet("background-color: rgb(44, 49, 60, 255);"
                           "color: rgb(255, 255, 255);"
                           "alternate-background-color: rgb(44, 49, 60, 255);"
                           "selection-background-color: rgb(108, 120, 151);")
        self.tableWidget.horizontalHeader().setStyleSheet("::section{Background-color: rgb(66, 73, 90, 255)}")
        self.tableWidget.setStyleSheet("background-color:  rgb(55, 61, 75, 255);"
                                       "color: rgb(255, 255, 255);"
                                       "alternate-background-color: rgb(44, 49, 60, 255);"
                                       "selection-background-color: rgb(108, 120, 151);"
                                       "border-color: rgb(0, 0, 0, 255);")
        self.btn_ac_addbook.setIcon(QIcon("icons/cil-library-add.png"))
        self.btn_ac_search.setIcon(QIcon("icons/cil-zoom-in.png"))
        self.btn_ac_refresh.setIcon(QIcon("icons/cil-reload.png"))
        self.btn_ac_delete.setIcon(QIcon("icons/cil-trash.png"))
        self.scrll.setStyleSheet("QRangeSlider #Span:active { background: rgb(108, 120, 151);}"
                                 "QRangeSlider #Head {background: rgb(55, 61, 75, 255);}"
                                 "QRangeSlider #Tail {background: rgb(55, 61, 75, 255);}")
        self.num = True

    def dayTheme(self):
        self.help_menu.setStyleSheet("")
        self.file_menu.setStyleSheet("")
        self.window().setStyleSheet("")
        self.setStyleSheet("")
        self.tableWidget.horizontalHeader().setStyleSheet("")
        self.tableWidget.setStyleSheet("")
        self.btn_ac_addbook.setIcon(QIcon("icons/d_add.png"))
        self.btn_ac_search.setIcon(QIcon("icons/d_search.png"))
        self.btn_ac_refresh.setIcon(QIcon("icons/d_refresh.png"))
        self.btn_ac_delete.setIcon(QIcon("icons/d_trash.png"))
        self.scrll.setStyleSheet("QRangeSlider #Span:active { background: #3B99FC;}"
                                 "QRangeSlider #Head {background: #E3DEE2;}"
                                 "QRangeSlider #Tail {background: #E3DEE2;}")
        self.num = False

    def findName(self):
        name = self.search.text().lower()
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, self.btn_cb.currentIndex())
            self.tableWidget.setRowHidden(row, name not in item.text().lower())

    def inshop(self):
        self.price1.setChecked(True)
        self.price2.setChecked(False)
        name = "0"
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 4)
            self.tableWidget.setRowHidden(row, name in item.text())

    def priceSort(self):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, 5)
            self.tableWidget.setRowHidden(row, int(item.text()) not in range(self.scrll.start(), self.scrll.end()))

    def allshop(self):
        self.price2.setChecked(True)
        self.price1.setChecked(False)
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHidden(i, False)

    def to_pdf(self):
        w = self.tableWidget
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', ".pdf(*.pdf)")
        model = w.model()

        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterResolution)
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setPaperSize(QtPrintSupport.QPrinter.A4)
        printer.setOrientation(QtPrintSupport.QPrinter.Landscape)
        printer.setOutputFileName(filename)

        doc = QtGui.QTextDocument()

        html = """<html>
        <head>
        <style>
        table, th, td {
          border: 1px solid black;
          border-collapse: collapse;
        }
        </style>
        </head>"""
        html += "<table><thead>"
        html += "<tr>"
        for c in range(model.columnCount()):
            html += "<th>\t{}\t</th>".format(model.headerData(c, QtCore.Qt.Horizontal))
        html += "</tr></thead>"
        html += "<tbody>"
        for r in range(model.rowCount()):
            html += "<tr>"
            for c in range(model.columnCount()):
                html += "<td> {} </td>".format(model.index(r, c).data() or "")
            html += "</tr>"
        html += "</tbody></table>"
        doc.setHtml(html)
        doc.setPageSize(QtCore.QSizeF(printer.pageRect().size()))
        doc.print(printer)

    def loaddata(self):
        """Функция, осуществляющая загрузку уже имеющейся базы данных"""
        self.connection = sqlite3.connect("database.db")
        query = "SELECT * FROM books"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()
        self.filt()

    def handlePaintRequest(self, printer):
        """Функция, отвечающая за корректное отображение таблицы"""
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(
            model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
        document.print_(printer)

    def insert(self):
        """Функция, обращающаяся к классу добавления книги"""
        dlg = InsertDialog(self.num)
        dlg.exec_()

    def delete(self):
        """Функция, обращающаяся к классу удаления книги"""
        dlg = DeleteDialog(self.num)
        dlg.exec_()

    def search(self):
        """Функция, обращающаяся к классу поиска книги"""
        dlg = SearchDialog(self.num)
        dlg.exec_()

    def about(self):
        """Функция, обращающаяся к классу показа информации о владельце"""
        dlg = AboutDialog(self.num)
        dlg.exec_()

    def slotSelect(self, state):
        for checkbox in self.checkBoxs:
            checkbox.setChecked(QtCore.Qt.Checked == state)

    def menuClose(self):
        self.keywords[self.col] = []
        for element in self.checkBoxs:
            if element.isChecked():
                self.keywords[self.col].append(element.text())
        self.filterdata()
        self.menu.close()

    def clearFilter(self):
        if self.tableWidget.rowCount() > 0:
            for i in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHidden(i, False)

    def filterdata(self):
        columnsShow = dict([(i, True) for i in range(self.tableWidget.rowCount())])

        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(i, j)
                if self.keywords[j]:
                    if item.text() not in self.keywords[j]:
                        columnsShow[i] = False
        for key in columnsShow:
            self.tableWidget.setRowHidden(key, not columnsShow[key])

    def Scrll(self, data_unique):
        data_unique.sort()
        self.min = data_unique.__getitem__(0)
        self.max = data_unique.__getitem__(len(data_unique) - 1)
        self.scrll.setMin(self.min)
        self.scrll.setMax(self.max)

    def columnfilterclicked(self, index):
        self.menu = QtWidgets.QMenu(self)
        self.menu.setStyleSheet("QMenu { menu-scrollable: true; }")
        self.col = index

        data_unique = []
        self.checkBoxs = []

        checkBox = QtWidgets.QCheckBox("Select all", self.menu)
        checkableAction = QtWidgets.QWidgetAction(self.menu)

        checkableAction.setDefaultWidget(checkBox)
        self.menu.addAction(checkableAction)
        checkBox.setChecked(True)
        checkBox.stateChanged.connect(self.slotSelect)

        for i in range(self.tableWidget.rowCount()):
            if not self.tableWidget.isRowHidden(i):
                item = self.tableWidget.item(i, index)
                if item.text() not in data_unique:
                    data_unique.append(item.text())
                    checkBox = QtWidgets.QCheckBox(item.text(), self.menu)
                    checkBox.setChecked(True)
                    checkableAction = QtWidgets.QWidgetAction(self.menu)
                    checkableAction.setDefaultWidget(checkBox)
                    self.menu.addAction(checkableAction)
                    self.checkBoxs.append(checkBox)

        btn = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
                                         QtCore.Qt.Horizontal, self.menu)
        btn.accepted.connect(self.menuClose)
        btn.rejected.connect(self.menu.close)
        checkableAction = QtWidgets.QWidgetAction(self.menu)
        checkableAction.setDefaultWidget(btn)
        self.menu.addAction(checkableAction)

        headerPos = self.tableWidget.mapToGlobal(self.tableWidgetHeader.pos())

        posY = headerPos.y() + self.tableWidgetHeader.height()
        posX = headerPos.x() + self.tableWidgetHeader.sectionPosition(index)
        self.menu.exec_(QtCore.QPoint(posX, posY))


app = QApplication(sys.argv)
passdlg = LoginDialog()
if (passdlg.exec_() == QDialog.Accepted):
    window = MainWindow()
    window.show()
    window.loaddata()
sys.exit(app.exec_())
