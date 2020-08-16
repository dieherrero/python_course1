import sys
import math
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *
from PyQt5.QtWidgets import *


class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))  # b attribute is the button
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handleinput(self.text))

    def handleinput(self, v):
        if v == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v == "AC":
            self.results.setText("")
        elif v == "C":
            self.results.setText("0")
        elif v == "√":
            temp_value = float(self.results.text())
            self.results.setText(str(math.sqrt(temp_value)))
        elif v == "DEL":
            current_value = self.results.text()
            self.results.setText(current_value[:-1])
        else:
            current_value = self.results.text()
            new_value = current_value + str(v)
            self.results.setText(new_value)


class APPLICATION(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.createAPP()

    def createAPP(self):
        grid = QGridLayout()
        results = QLineEdit()

#        btn1 = QPushButton("B1")
        btns = ["AC", "√", "/", "DEL",
                7, 8, 9, "*",
                4, 5, 6, "-",
                1, 2, 3, "+",
                0, ".", "="]

        grid.addWidget(results, 0, 0, 1, 4)
        row = 1
        col = 0

# addwidget(object, row, column, row_spaces, column_spaces) : posicion y espacio que ocupa el objeto
        for button in btns:
            if col > 3:
                col = 0
                row += 1

            btn_object = Button(button, results)

            if button == 0:
                grid.addWidget(btn_object.b, row, col, 1, 2)   #remember that b attrib is the button
                col += 1
            else:
                grid.addWidget(btn_object.b, row, col, 1, 1)

            col += 1

        self.setLayout(grid)
        self.show()


if __name__ == '__main__':
    # Create the application instance.
    app = QApplication(sys.argv)
    window = APPLICATION()
    window.show()
    sys.exit(app.exec_())
