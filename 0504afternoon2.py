from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()

widget.setWindowTitle('Hello QT6')
widget.resize(400,300)

grid = QtWidgets.QGridLayout(widget)

label = QtWidgets.QLabel(widget)
label.setText('TEST')
# label.move(30,30)
grid.addWidget(label,0,0)

label2 = QtWidgets.QLabel(widget)
label2.setText('POIUY')
# label2.move(30,50)
grid.addWidget(label2,1,0)

input1 = QtWidgets.QLineEdit(widget)
# input1.move(60, 30)
grid.addWidget(input1,0,1)

text1 = QtWidgets.QTextEdit(widget)
# text1.move(100, 100)
grid.addWidget(text1,1,1)

showLabel = QtWidgets.QLabel(widget)
grid.addWidget(showLabel,3,0)

def test():
    # print('hello')
    # print(input1.text())
    # print(text1.toPlainText())
    showLabel.setText(input1.text())

btn = QtWidgets.QPushButton(widget)
btn.setText('按我按我')
grid.addWidget(btn, 2, 0)
btn.clicked.connect(test)


widget.show()

sys.exit(app.exec())