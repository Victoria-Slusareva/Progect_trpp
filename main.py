from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import sqlite3

class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Зарегистрировать")

        self.setWindowTitle("Добавить книгу")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        self.QBtn.clicked.connect(self.addbook)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Название")
        layout.addWidget(self.nameinput)

        self.genreinput = QComboBox()
        self.genreinput.addItem("Классическая литература")
        self.genreinput.addItem("Детективы")
        self.genreinput.addItem("Фэнтези")
        self.genreinput.addItem("Фантастика")
        self.genreinput.addItem("Ужасы, мистика")
        self.genreinput.addItem("Поэзия и драматургия")
        self.genreinput.addItem("Наука и образование")
        layout.addWidget(self.genreinput)

        self.priceinput = QLineEdit()
        self.priceinput.setPlaceholderText("Цена")
        layout.addWidget(self.priceinput)

        self.quantityinput = QLineEdit()
        self.quantityinput.setPlaceholderText("Количество")
        layout.addWidget(self.quantityinput)

        self.authorinput = QLineEdit()
        self.authorinput.setPlaceholderText("Автор")
        layout.addWidget(self.authorinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addbook(self):

        name = ""
        genre = ""
        price = -1
        quantity = -1
        author = ""

        name = self.nameinput.text()
        genre = self.genreinput.itemText(self.genreinput.currentIndex())
        price = self.priceinput.text()
        quantity = self.quantityinput.text()
        author = self.authorinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO books (name,genre,price,quantity,author) VALUES (?,?,?,?,?)",
                           (name, genre, price, quantity, author))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Успешно', 'Книга успешно добавлена.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Ошибка', 'Не удалось добавить книгу.')


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
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

    def searchbook(self):

        searchrol = ""
        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from students WHERE roll=" + str(searchrol))
            row = result.fetchone()
            serachresult = "ID: " + str(row[0]) + '\n' + "Жанр: " + str(row[1]) + '\n' + "Автор: " + str(
                row[2]) + '\n' + "Название: " + str(row[3]) + '\n' + "Кол-во: " + str(row[4]) + '\n' + "Цена: "
            QMessageBox.information(QMessageBox(), 'Успешно', serachresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Ошибка', 'Не удалось найти книгу.')


class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
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

    def deletebook(self):

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
    def __init__(self, *args, **kwargs):
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
        if self.passinput.text() == "123":
            self.accept()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Неверный пароль.')

class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(300)
        self.setFixedHeight(250)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.setFixedWidth(40)

        layout = QVBoxLayout()

        title = QLabel("Книжный магазин")
        font = title.font()
        font.setPointSize(16)
        title.setFont(font)

        labelpic = QLabel()
        pixmap = QPixmap('icons/logo.png')
        pixmap = pixmap.scaledToWidth(250)
        pixmap = pixmap.scaledToHeight(115)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(120)

        layout.addWidget(title)

        layout.addWidget(QLabel("Версия 1.0"))
        layout.addWidget(QLabel("Автор:\tСлюсарева В.А.\n2021 год"))
        layout.addWidget(labelpic)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute(
            "CREATE TABLE IF NOT EXISTS books(roll INTEGER PRIMARY KEY AUTOINCREMENT ,genre TEXT, author TEXT, name TEXT, quantity INTEGER,price INTEGER)")
        self.c.close()

        file_menu = self.menuBar().addMenu("&Файл")

        help_menu = self.menuBar().addMenu("&Информация")
        self.setWindowTitle("Информационная система книжного  магазина")

        self.setMinimumSize(800, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("ID", "Жанр", "Автор", "Название", "Кол-во", "Цена"))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_addbook = QAction(QIcon("icons/add.png"), "Добавить", self)
        btn_ac_addbook.triggered.connect(self.insert)
        btn_ac_addbook.setStatusTip("Добавить книгу")
        toolbar.addAction(btn_ac_addbook)

        btn_ac_refresh = QAction(QIcon("icons/refresh.png"), "Обновить", self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Обновить таблицу")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("icons/search.png"), "Поиск", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Найти книгу")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("icons/trash.png"), "Удалить", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Удалить книгу")
        toolbar.addAction(btn_ac_delete)

        addbook_action = QAction(QIcon("icons/add.png"), "Добавить книгу", self)
        addbook_action.triggered.connect(self.insert)
        file_menu.addAction(addbook_action)

        searchbook_action = QAction(QIcon("icons/search.png"), "Найти книгу", self)
        searchbook_action.triggered.connect(self.search)
        file_menu.addAction(searchbook_action)

        delbook_action = QAction(QIcon("icons/trash.png"), "Удалить книгу", self)
        delbook_action.triggered.connect(self.delete)
        file_menu.addAction(delbook_action)

        about_action = QAction(QIcon("icons/info.png"), "Владелец", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def loaddata(self):
        self.connection = sqlite3.connect("database.db")
        query = "SELECT * FROM books"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def handlePaintRequest(self, printer):
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
        dlg = InsertDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()


app = QApplication(sys.argv)
passdlg = LoginDialog()
if (passdlg.exec_() == QDialog.Accepted):
    window = MainWindow()
    window.show()
    window.loaddata()
sys.exit(app.exec_())
