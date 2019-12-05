import sys
from functools import partial

from PySide2.QtWidgets import QApplication, QMainWindow

from controller import CalculatorController
from view import CalculatorUI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = CalculatorUI()
        self.ui.setupUi(self)
        self.controller = CalculatorController(self.ui)
        self.initialize_slots()

    def initialize_slots(self):
        # Initialize numeric digits
        self.ui.pushButton_one.clicked.connect(partial(self.controller.on_digit_click, '1'))
        self.ui.pushButton_two.clicked.connect(partial(self.controller.on_digit_click, '2'))
        self.ui.pushButton_three.clicked.connect(partial(self.controller.on_digit_click, '3'))
        self.ui.pushButton_four.clicked.connect(partial(self.controller.on_digit_click, '4'))
        self.ui.pushButton_five.clicked.connect(partial(self.controller.on_digit_click, '5'))
        self.ui.pushButton_six.clicked.connect(partial(self.controller.on_digit_click, '6'))
        self.ui.pushButton_seven.clicked.connect(partial(self.controller.on_digit_click, '7'))
        self.ui.pushButton_eight.clicked.connect(partial(self.controller.on_digit_click, '8'))
        self.ui.pushButton_nine.clicked.connect(partial(self.controller.on_digit_click, '9'))
        self.ui.pushButton_zero.clicked.connect(partial(self.controller.on_digit_click, '0'))

        # Initialize modifiers
        self.ui.pushButton_decimal.clicked.connect(self.controller.on_decimal_click)
        self.ui.pushButton_change_sign.clicked.connect(self.controller.on_change_sign_click)
        self.ui.pushButton_percentage.clicked.connect(self.controller.on_percent_click)

        # Initialize arithmatic operators
        self.ui.pushButton_add.clicked.connect(partial(self.controller.on_operator_click, '+'))
        self.ui.pushButton_subtract.clicked.connect(partial(self.controller.on_operator_click, '-'))
        self.ui.pushButton_multiply.clicked.connect(partial(self.controller.on_operator_click, '*'))
        self.ui.pushButton_division.clicked.connect(partial(self.controller.on_operator_click, '/'))

        # Initialize clear and equals buttons
        self.ui.pushButton_clear.clicked.connect(self.controller.on_clear_click)
        self.ui.pushButton_equals.clicked.connect(self.controller.on_equals_click)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
