import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import csv
from PyQt5.QtCore import QDate


# перед запуском данной программы рекомендуется запустить программу "заполнение таблицы для примера"
# класс, в котором создаются элементы


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1179, 666)
        MainWindow.setStyleSheet("background-color: rgb(243, 232, 231);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(710, 20, 461, 451))
        '''self.listWidget.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                      "color: rgb(81, 63, 66);\n"
                                      "background-color: rgb(253, 245, 230);")'''

        self.listWidget.setObjectName("timetable")
        self.del_btn = QtWidgets.QToolButton(self.centralwidget)  # кнопка, которая удаляет все
        self.del_btn.setGeometry(QtCore.QRect(470, 270, 111, 34))
        '''self.del_btn.setStyleSheet("background-color: rgb(246, 223, 225);")'''
        self.del_btn.setObjectName("del_btn")
        self.add_btn = QtWidgets.QToolButton(self.centralwidget)  # кнопка, которая добавляет
        self.add_btn.setGeometry(QtCore.QRect(591, 270, 111, 34))
        '''self.add_btn.setStyleSheet("background-color: rgb(246, 223, 225);\n"
                                   "border-color: rgb(198, 186, 190);")'''
        self.add_btn.setObjectName("add_btn")
        self.main_text = QtWidgets.QTextBrowser(self.centralwidget)  # текст, который описывает в каком формате
        # выполнять ввод
        self.main_text.setGeometry(QtCore.QRect(361, 20, 341, 131))
        '''self.main_text.setStyleSheet("background-color: rgb(242, 188, 193);\n"
                                     "font: 12pt \"TeX Gyre Schola\";")'''
        '''self.main_text.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                     "color: rgb(241, 240, 232);\n"
                                     "background-color: rgb(81, 63, 66);")'''
        self.main_text.setObjectName("main_text")
        self.selected_event = QtWidgets.QTextBrowser(self.centralwidget)  # виджет, показывающий выбранное событие
        self.selected_event.setGeometry(QtCore.QRect(710, 540, 461, 111))
        '''self.selected_event.setStyleSheet("background-color: rgb(244, 201, 201);\n"
                                          "\n"
                                          "font: 12pt \"TeX Gyre Schola\";")'''
        self.selected_event.setObjectName("selected_event")
        self.input_text = QtWidgets.QLineEdit(self.centralwidget)  # виджет, который считывает дату и событие
        self.input_text.setGeometry(QtCore.QRect(361, 160, 341, 101))
        self.input_text.setAutoFillBackground(False)
        '''self.input_text.setStyleSheet("background-color: rgb(242, 188, 193);\n"
                                      "font: 12pt \"TeX Gyre Schola\";")'''
        self.input_text.setText("")
        self.input_text.setObjectName("input_text")
        self.soon_event = QtWidgets.QTextBrowser(self.centralwidget)  # виджет, показывающий ближайшее событие
        self.soon_event.setGeometry(QtCore.QRect(710, 450, 461, 81))
        '''self.soon_event.setStyleSheet("background-color: rgb(224, 235, 242);\n"
                                      "font: 12pt \"TeX Gyre Schola\";")'''
        self.soon_event.setObjectName("soon_event")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 160, 341, 240))
        '''self.calendarWidget.setStyleSheet("\n"
                                          "background-color: rgb(206, 224, 221);\n"
                                          "alternate-background-color: rgb(218, 234, 217);")'''
        self.calendarWidget.setObjectName("calendarWidget")
        self.del_btn_2 = QtWidgets.QToolButton(self.centralwidget)  # кнопка "Сделано"
        self.del_btn_2.setGeometry(QtCore.QRect(360, 270, 101, 34))
        # self.del_btn_2.setStyleSheet("background-color: rgb(246, 223, 225);")
        self.del_btn_2.setObjectName("del_btn_2")
        self.done_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.done_text.setGeometry(QtCore.QRect(10, 410, 341, 31))
        '''self.done_text.setStyleSheet("background-color: rgb(224, 235, 242);\n"
                                     "font: 12pt \"TeX Gyre Schola\";")'''
        self.done_text.setObjectName("done_text")
        self.under_done = QtWidgets.QTextBrowser(self.centralwidget)
        self.under_done.setGeometry(QtCore.QRect(10, 440, 341, 111))
        '''self.under_done.setStyleSheet("background-color: rgb(244, 201, 201);\n"
                                      "\n"
                                      "font: 12pt \"TeX Gyre Schola\";")'''
        self.under_done.setObjectName("under_done")
        self.light_look = QtWidgets.QToolButton(self.centralwidget)
        self.light_look.setGeometry(QtCore.QRect(10, 600, 161, 54))
        #self.light_look.setStyleSheet("background-color: rgb(206, 224, 221);\n""")
        self.light_look.setObjectName("light_look")
        self.dark_look = QtWidgets.QToolButton(self.centralwidget)
        self.dark_look.setGeometry(QtCore.QRect(190, 600, 161, 54))
        #self.dark_look.setStyleSheet("background-color: rgb(206, 224, 221);")
        self.dark_look.setObjectName("dark_look")
        self.del_btn_3 = QtWidgets.QToolButton(self.centralwidget)  # кнопка "Удалить все из раздела"Сделано"
        self.del_btn_3.setGeometry(QtCore.QRect(10, 560, 341, 34))
        #  self.del_btn_3.setStyleSheet("background-color: rgb(246, 223, 225);")
        self.del_btn_3.setObjectName("del_btn_3")

        self.listWidget.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                      "color: rgb(81, 63, 66);\n"
                                      "background-color: rgb(253, 245, 230);")
        self.del_btn.setStyleSheet("background-color: rgb(205, 183, 169);\n"
                                   "")
        self.add_btn.setStyleSheet("background-color: rgb(205, 183, 169);\n"
                                   "border-color: rgb(198, 186, 190);")
        self.main_text.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                     "color: rgb(81, 63, 66);\n"
                                     "background-color: rgb(238, 222, 206);")
        self.selected_event.setStyleSheet("background-color: rgb(226, 214, 206);\n"
                                          "font: 12pt \"TeX Gyre Schola\";")
        self.input_text.setStyleSheet("background-color: rgb(226, 214, 206);\n"
                                      "font: 12pt \"TeX Gyre Schola\";")
        self.soon_event.setStyleSheet("background-color: rgb(253, 245, 230);\n"
                                      "color: rgb(81, 63, 66);\n"
                                      "font: 12pt \"TeX Gyre Schola\";")
        self.calendarWidget.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                          "color: rgb(81, 63, 66);\n"
                                          "background-color: rgb(238, 222, 206);")
        self.done_text.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                     "background-color: rgb(81, 63, 66);\n"
                                     "color: rgb(226, 214, 206);")
        self.under_done.setStyleSheet("background-color: rgb(226, 214, 206);\n"
                                      "\n"
                                      "font: 12pt \"TeX Gyre Schola\";")
        self.del_btn_2.setStyleSheet("background-color: rgb(205, 183, 169);\n"
                                     "")
        self.del_btn_3.setStyleSheet("background-color: rgb(205, 183, 169);\n"
                                     "")
        self.light_look.setStyleSheet("background-color: rgb(170, 124, 114);")
        # self.classic_look.setStyleSheet("background-color: rgb(170, 124, 114);")
        self.dark_look.setStyleSheet("background-color: rgb(170, 124, 114);")
        # self.eatable_look.setStyleSheet("background-color: rgb(170, 124, 114);")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.del_btn.setText(_translate("MainWindow", "Удалить все"))
        self.add_btn.setText(_translate("MainWindow", "Добавить"))
        self.selected_event.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                               "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n""<html><head>"
                                               "<meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'TeX Gyre Schola\'; "
                                               "font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; "
                                               "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                               "text-indent:0px;\">"
                                               "<span style=\" font-family:\'Sans Serif\'; font-size:11pt; "
                                               "font-weight:72; font-style:italic;\">Выбранно событие:</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                                               "<span style=\" font-family:\'Sans Serif\'; font-size:11pt; "
                                               "font-weight:72; font-style:italic;\">пока ничего не выбрано</span>"
                                               "</p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                               "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                               "-qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; "
                                               "font-size:11pt; font-weight:72; font-style:italic;\"><br /></p></body>"
                                               "</html>"))
        self.del_btn_2.setText(_translate("MainWindow", "Сделано"))
        self.done_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                        "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" />"
                                                        "<style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:"
                                                        "\'TeX Gyre Schola\'; font-size:12pt; font-weight:400; "
                                                        "font-style:normal;\">\n""<p style=\" margin-top:0px; "
                                                        "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                        "-qt-block-indent:0; text-indent:0px;\">Сделано:</p></body>"
                                                        "</html>"))
        self.under_done.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                         "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" />"
                                                         "<style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n""</style>"
                                                         "</head><body style=\" font-family:\'TeX Gyre Schola\'; "
                                                         "font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                                         "margin-bottom:0px; margin-left:0px; margin-right:0px;"
                                                         " -qt-block-indent:0; text-indent:0px;\"><br />"
                                                         "</p></body></html>"))
        # self.classic_look.setText(_translate("MainWindow", "Классическая тема"))
        self.light_look.setText(_translate("MainWindow", "светлая тема"))
        self.dark_look.setText(_translate("MainWindow", "темная тема"))
        # self.eatable_look.setText(_translate("MainWindow", " \"Съедобная\" тема"))
        self.del_btn_3.setText(_translate("MainWindow", "Удалить все из раздела \"Сделано\""))


class Doing(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.ui = Ui_MainWindow()
        self.setupUi(self)

        self.setWindowTitle('do it')
        self.add_btn.clicked.connect(self.f_add_btn)
        self.del_btn.clicked.connect(self.f_del_btn)
        self.del_btn_2.clicked.connect(self.f_del_btn_2)
        self.calendarWidget.clicked[QDate].connect(self.showDate)

        # добавление данных в listWidget из data
        data = open('data.csv', encoding='utf-8').read().split('\n')[:-1]
        for row in data:
            if row != '':
                self.listWidget.addItem(' - '.join(row.split(';')))
            self.listWidget.sortItems(QtCore.Qt.DescendingOrder)

        # добавление данных в under_done из data_1

        data_1 = open('data_1.csv', encoding='utf-8').read().split('\n')[:-1]
        for row in data_1:
            if row != '':
                self.under_done.append(' - '.join(row.split(';')))

        self.listWidget.itemClicked.connect(self.listwidgetclicked)

        # настройка содержания soon_event и selected_event

        if self.listWidget:
            self.soon_event.setText(
                f'Ближайшие событие:\n{self.listWidget.item(int(self.listWidget.count()) - 1).text()}')
        self.main_text.setText('Для добавления введите название события в окне ниже и выбирете дату в календаре \
                               и нажмите "добавить".')
        if self.listWidget.count() == 0:
            self.selected_event.setText(f'Выбранно событие: Нет событий')

        self.main_image()
        self.ikon()
        self.light_look.clicked.connect(self.f_light_look)
        self.dark_look.clicked.connect(self.f_dark_look)
        self.selected_event.setText(f'Выбранно событие: Нет событий')
        self.del_btn_3.clicked.connect(self.f_del_btn_3)
        self.calendarWidget.clicked[QDate].connect(self.showDate)

    def f_light_look(self):  # функция, меняющая стиль
        self.listWidget.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                      "color: rgb(81, 63, 66);\n"
                                      "background-color: rgb(253, 245, 230);")
        self.del_btn.setStyleSheet("background-color: rgb(205, 183, 169);\n"
                                   "")
        self.add_btn.setStyleSheet("background-color: rgb(205, 183, 169);\n"
                                   "border-color: rgb(198, 186, 190);")
        self.main_text.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                          "color: rgb(81, 63, 66);\n"
                                          "background-color: rgb(238, 222, 206);")
        self.selected_event.setStyleSheet("background-color: rgb(226, 214, 206);\n"
                                          "font: 12pt \"TeX Gyre Schola\";")
        self.input_text.setStyleSheet("background-color: rgb(226, 214, 206);\n"
                                      "font: 12pt \"TeX Gyre Schola\";")
        self.soon_event.setStyleSheet("background-color: rgb(253, 245, 230);\n"
                                      "color: rgb(81, 63, 66);\n"
                                      "font: 12pt \"TeX Gyre Schola\";")
        self.calendarWidget.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                          "color: rgb(81, 63, 66);\n"
                                          "background-color: rgb(238, 222, 206);")
        self.done_text.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                     "background-color: rgb(81, 63, 66);\n"
                                     "color: rgb(226, 214, 206);")
        self.under_done.setStyleSheet("background-color: rgb(226, 214, 206);\n"
                                      "\n"
                                      "font: 12pt \"TeX Gyre Schola\";")
        self.del_btn_2.setStyleSheet("background-color: rgb(205, 183, 169);\n"
                                     "")
        self.del_btn_3.setStyleSheet("background-color: rgb(205, 183, 169);\n"
                                     "")
        self.light_look.setStyleSheet("background-color: rgb(170, 124, 114);")
        #self.classic_look.setStyleSheet("background-color: rgb(170, 124, 114);")
        self.dark_look.setStyleSheet("background-color: rgb(170, 124, 114);")
        #self.eatable_look.setStyleSheet("background-color: rgb(170, 124, 114);")

    def f_dark_look(self):  # функция, меняющая стиль
        self.listWidget.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                      "color: rgb(241, 240, 232);\n"
                                      "background-color: rgb(81, 63, 66);")
        self.del_btn.setStyleSheet("background-color: rgb(205, 183, 169);\n"
                                   "")
        self.add_btn.setStyleSheet("background-color: rgb(205, 183, 169);\n"
                                   "border-color: rgb(198, 186, 190);")
        self.main_text.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                     "color: rgb(241, 240, 232);\n"
                                     "background-color: rgb(81, 63, 66);")
        self.selected_event.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                      "color: rgb(241, 240, 232);\n"
                                      "background-color: rgb(81, 63, 66);")
        self.input_text.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                      "color: rgb(241, 240, 232);\n"
                                      "background-color: rgb(81, 63, 66);")
        self.soon_event.setStyleSheet("background-color: rgb(81, 63, 66);\n"
                                      "color: rgb(241, 240, 232);\n"
                                      "font: 12pt \"TeX Gyre Schola\";")
        self.calendarWidget.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                      "background-color: rgb(81, 63, 66);")
        self.done_text.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                     "background-color: rgb(81, 63, 66);\n"
                                     "color: rgb(226, 214, 206);")
        self.under_done.setStyleSheet("font: 12pt \"TeX Gyre Schola\";\n"
                                      "color: rgb(241, 240, 232);\n"
                                      "background-color: rgb(81, 63, 66);")
        self.del_btn_2.setStyleSheet("background-color: rgb(205, 183, 169);\n"
                                     "")
        self.del_btn_3.setStyleSheet("background-color: rgb(205, 183, 169);\n"
                                     "")
        # self.coffee_look.setStyleSheet("background-color: rgb(170, 124, 114);")
        # self.classic_look.setStyleSheet("background-color: rgb(170, 124, 114);")
        self.dark_look.setStyleSheet("background-color: rgb(170, 124, 114);")
        # self.eatable_look.setStyleSheet("background-color: rgb(170, 124, 114);")


    def ikon(self):  # функция для отображения иконки
        self.pixmap = QPixmap('ikon.jpg')
        self.image = QLabel(self)
        self.image.move(10, 20)
        self.image.resize(340, 130)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)

    def main_image(self):  # функция для отображения главной картинки ( в данном случае цветов)
        self.pixmap = QPixmap('orig1.jpg')
        self.image = QLabel(self)
        self.image.move(360, 315)
        self.image.resize(340, 340)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)

    def f_del_btn_2(self):  # функция для кнопки "Сделано"
        self.listWidget.takeItem(self.item)
        self.under_done.append(f'{" - ".join(self.item_el)}')

        # настройка содержимого soon_event
        if self.listWidget.count() != 0:
            self.soon_event.setText(
                f'Ближайшие событие:\n{self.listWidget.item(int(self.listWidget.count()) - 1).text()}')
        else:
            self.soon_event.setText(
                f'Ближайшие событие: Нет')
        self.selected_event.setText(f'Выбранно событие: Нет событий')

        # настройка содержимого data

        if self.listWidget.count() != 0:
            with open('data.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(self.listWidget.item(0).text())

            for i in range(self.listWidget.count() - 1):
                with open('data.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(self.listWidget.item(i + 1).text().split(' - '))
        # настройка содержимого data_1

        with open('data_1.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(self.item_el)

    def listwidgetclicked(self, item):  # функция, которая запускается при нажатие на один из элементов в listWidget
        if self.listWidget.count() != 0:
            self.item_el = item.text().split(' - ')
            self.selected_event.setText(f'Выбранно событие: \n{str(self.item_el[1])}\nДата:\n{str(self.item_el[0])}')
        else:
            self.selected_event.setText(f'Выбранно событие: Нет событий')
        self.item = int(self.listWidget.row(item))

    def f_add_btn(self):  # функция для кнопки "Добавить"
        text = self.input_text.text()
        if self.input_text.text() != '':
            self.listWidget.addItem(self.data + ' - ' + text)
            self.input_text.clear()
            self.listWidget.sortItems(QtCore.Qt.DescendingOrder)
        with open('data.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([self.data, text])
        if self.listWidget.count() != 0:
            self.soon_event.setText(
                f'Ближайшие событие:\n{self.listWidget.item(int(self.listWidget.count()) - 1).text()}')
        else:
            self.soon_event.setText(
                f'Ближайшие событие: Нет')

    def f_del_btn(self):  # функция для кнопки "Удалить все"
        self.listWidget.clear()
        if self.listWidget.count() == 0:
            self.selected_event.setText(f'Выбранно событие: Нет событий')
        self.soon_event.setText(
            f'Ближайшие событие: Нет событий')

        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            writer.writerow('')

        data_1 = open('data_1.csv', encoding='utf-8').read().split('\n')[:-1]
        for row in data_1:
            if row != '':
                self.under_done.append(' - '.join(row.split(';')))

    def f_del_btn_3(self):  # функция для кнопки "Удалить все из раздела "Сделано"
        with open('data_1.csv', 'w', newline='') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow('')
        self.under_done.clear()

    def showDate(self, date):
        self.data = str(date.toString('yyyy.MM.dd'))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Doing()  # Создаём объект класса Doing
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
