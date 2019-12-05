from view.calculator_ui import Ui_MainWindow


class CalculatorUI(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def clear_display(self):
        self.label_output.setText('0')

    def set_display_text(self, text: str):
        self.label_output.setText(text)

    def set_button_text(self, text: str):
        self.pushButton_clear.setText(text)
