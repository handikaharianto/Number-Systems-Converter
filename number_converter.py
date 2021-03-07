from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QComboBox, QLineEdit, QPushButton, QStyledItemDelegate
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

import qdarkstyle

from conversion import Conversion

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        convert = Conversion() # create an instance of class Conversion()

        self.setWindowTitle("Number Systems Converter")
        self.setFixedSize(420, 420)

        self.v_layout = QVBoxLayout(self)    # set vertical layout

        delegate = QStyledItemDelegate()    # to resolve expanded combo box

        label_text = QLabel("SELECT YOUR NUMBER SYSTEM:")
        label_text.setFont(QFont("Helvetica", 20))

        label_from = QLabel("From:")
        label_from.setFont(QFont("Helvetica", 17))

        # items for combo box
        options = ["Binary (Base 2)", "Decimal (Base 10)", "Hexademical (Base 16)", "Octal (Base 8)"]

        combo_box_from = QComboBox(self)
        combo_box_from.addItems(options)
        combo_box_from.setItemDelegate(delegate)

        self.entry_field = QLineEdit(self)
        self.entry_field.setText("")

        label_to = QLabel("To:")
        label_to.setFont(QFont("Helvetica", 17))

        combo_box_to = QComboBox(self)
        combo_box_to.addItems(options)
        combo_box_to.setItemDelegate(delegate)

        button = QPushButton("Convert", clicked = lambda: button_clicked())
        button.setFixedHeight(50)

        self.label_result = QLabel("Result:")
        self.label_result.setFont(QFont("Helvetica", 25))
        self.label_result.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        self.v_layout.addWidget(label_text)
        self.v_layout.addWidget(label_from)
        self.v_layout.addWidget(combo_box_from)
        self.v_layout.addWidget(self.entry_field)
        self.v_layout.addWidget(label_to)
        self.v_layout.addWidget(combo_box_to)
        self.v_layout.addWidget(button)
        self.v_layout.addWidget(self.label_result)

        def button_clicked():
            # binary to decimal, hexadecimal, octal
            if combo_box_from.currentText() == options[0] and combo_box_to.currentText() == options[1]:
                result = convert.binary_to_decimal(self.entry_field.text())
                self.label_result.setText(f"Result: {result}")
            
            elif combo_box_from.currentText() == options[0] and combo_box_to.currentText() == options[2]:
                result = convert.binary_to_hexa(self.entry_field.text())
                self.label_result.setText(f"Result: {result}")

            elif combo_box_from.currentText() == options[0] and combo_box_to.currentText() == options[3]:
                result = convert.binary_to_octal(self.entry_field.text())
                self.label_result.setText(f"Result: {result}")

            # decimal to binary, hexadecimal, octal
            elif combo_box_from.currentText() == options[1] and combo_box_to.currentText() == options[0]:
                result = convert.decimal_to_binary(self.entry_field.text())
                self.label_result.setText(f"Result: {result}")
            
            elif combo_box_from.currentText() == options[1] and combo_box_to.currentText() == options[2]:
                result = convert.decimal_to_hexa(self.entry_field.text())
                self.label_result.setText(f"Result: {result}")

            elif combo_box_from.currentText() == options[1] and combo_box_to.currentText() == options[3]:
                result = convert.decimal_to_octal(self.entry_field.text())
                self.label_result.setText(f"Result: {result}")

            # hexadecimal to binary, decimal, octal
            elif combo_box_from.currentText() == options[2] and combo_box_to.currentText() == options[0]:
                result = convert.hexa_to_binary(self.entry_field.text())
                self.label_result.setText(f"Result: {result}")

            elif combo_box_from.currentText() == options[2] and combo_box_to.currentText() == options[1]:
                result = convert.hexa_to_decimal(self.entry_field.text())
                self.label_result.setText(f"Result: {result}")

            elif combo_box_from.currentText() == options[2] and combo_box_to.currentText() == options[3]:
                result = convert.hexa_to_octal(self.entry_field.text())
                self.label_result.setText(f"Result: {result}")

            # octal to binary, decimal, hexadecimal
            elif combo_box_from.currentText() == options[3] and combo_box_to.currentText() == options[0]:
                result = convert.octal_to_binary(self.entry_field.text())
                self.label_result.setText(f"Result: {result}")

            elif combo_box_from.currentText() == options[3] and combo_box_to.currentText() == options[1]:
                result = convert.octal_to_decimal(self.entry_field.text())
                self.label_result.setText(f"Result: {result}")

            elif combo_box_from.currentText() == options[3] and combo_box_to.currentText() == options[2]:
                result = convert.octal_to_hexa(self.entry_field.text())
                self.label_result.setText(f"Result: {result}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    w = Window()
    w.show()
    app.exec_()