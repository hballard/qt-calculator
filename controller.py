from typing import List, Optional, Union

from view import CalculatorUI


def convert_string_to_num(s: str) -> Union[int, float]:
    try:
        return int(s)
    except ValueError:
        return float(s)


class CalculatorController:
    current_value: Optional[str] = None
    current_expression: List = []
    clear_all: bool = False

    def __init__(self, view: CalculatorUI):
        self.view = view

    def on_digit_click(self, digit: str) -> None:
        if self.current_value:
            self.current_value = self.current_value + digit
        self.current_value = digit
        self.view.set_display_text(self.current_value)

    def on_decimal_click(self) -> None:
        if self.current_value:
            if "." not in self.current_value:
                self.current_value = self.current_value + "."
        else:
            self.current_value = "."
        self.view.set_display_text(self.current_value)

    def on_percent_click(self) -> None:
        if self.current_value:
            num = convert_string_to_num(self.current_value)
            self.current_value = str(num / 100)
            self.view.set_display_text(self.current_value)

    def on_change_sign_click(self) -> None:
        if self.current_value:
            num = convert_string_to_num(self.current_value)
            self.current_value = str(-num)
            self.view.set_display_text(self.current_value)

    def on_clear_click(self) -> None:
        if self.current_value:
            self.current_value = None
            self.clear_all = True
        elif self.clear_all:
            self.current_expression = []
            self.current_value = None
            self.clear_all = False
        else:
            self.clear_all = True
        self.view.clear_display()

    def on_operator_click(self, operator: str) -> None:
        if not self.current_value and self.current_expression:
            self.current_expression.pop()
            self.current_expression.append(operator)
        elif not self.current_value and not self.current_expression:
            return
        elif self.current_value and not self.current_expression:
            self.current_expression.append(self.current_value)
            self.current_expression.append(operator)
            self.current_value = None
        elif self.current_value and self.current_expression:
            if operator in ["*", "/"] and self.current_expression[:-1] in ["+", "-"]:
                self.current_expression.append(self.current_value)
                self.current_expression.append(operator)
            else:
                self.current_expression.append(self.current_value)
                try:
                    self.current_value = str(eval("".join(self.current_expression)))
                except ZeroDivisionError:
                    self.current_value = "Not a Number"
                self.view.set_display_text(self.current_value)

    def on_equals_click(self) -> None:
        if self.current_value:
            self.current_expression.append(self.current_value)
            try:
                self.current_value = str(eval("".join(self.current_expression)))
            except ZeroDivisionError:
                self.current_value = "Not a Number"
        else:
            self.current_expression.append(self.current_expression[0])
            try:
                self.current_value = str(eval("".join(self.current_expression)))
            except ZeroDivisionError:
                self.current_value = "Not a Number"
        self.current_expression = []
        self.view.set_display_text(self.current_value)
