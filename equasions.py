import sys
import random
import webbrowser
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class EquationDisplay(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFont(QFont("Segoe UI", 28, QFont.Weight.Bold))
        self.setStyleSheet("color: #34495e; margin: 20px;")

class InstructionLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFont(QFont("Segoe UI", 20, QFont.Weight.Normal))
        self.setStyleSheet("color: #7f8c8d; margin-bottom: 10px;")

class EasyLinearEquationGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Уравнения!")
        self.setFixedSize(700, 350)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.equation_label = EquationDisplay()
        self.layout.addWidget(self.equation_label)

        self.instruction_label = InstructionLabel()
        self.instruction_label.setText("Намерете x")
        self.layout.addWidget(self.instruction_label)

        self.answer_label = QLabel("")
        self.answer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.answer_label.setFont(QFont("Segoe UI", 18, QFont.Weight.Normal))
        self.answer_label.setStyleSheet("color: #27ae60; margin-bottom: 20px;")
        self.layout.addWidget(self.answer_label)

        button_layout = QHBoxLayout()

        self.generate_btn = QPushButton("🎲 Генерирай уравнение")
        self.generate_btn.setFont(QFont("Segoe UI", 16))
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #2980b9;
                color: white;
                padding: 12px;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #3498db;
            }
        """)
        self.generate_btn.clicked.connect(self.generate_equation)
        button_layout.addWidget(self.generate_btn)

        self.show_answer_btn = QPushButton("Покажи отговора")
        self.show_answer_btn.setFont(QFont("Segoe UI", 16))
        self.show_answer_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                padding: 12px;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
        """)
        self.show_answer_btn.clicked.connect(self.show_answer)
        button_layout.addWidget(self.show_answer_btn)

        self.view_code_btn = QPushButton("Виж кода")
        self.view_code_btn.setFont(QFont("Segoe UI", 16))
        self.view_code_btn.setStyleSheet("""
            QPushButton {
                background-color: #8e44ad;
                color: white;
                padding: 12px;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #9b59b6;
            }
        """)
        self.view_code_btn.clicked.connect(self.open_code_link)
        button_layout.addWidget(self.view_code_btn)

        self.layout.addLayout(button_layout)

        self.current_solution = None

    def generate_equation(self):
        a = random.randint(1, 12)
        x = random.randint(-10, 10)
        b = random.randint(-20, 20)
        c = a * x + b

        left = ""
        if a == 1:
            left = "x"
        else:
            left = f"{a}x"

        if b > 0:
            left += f" + {b}"
        elif b < 0:
            left += f" - {abs(b)}"

        equation = f"{left} = {c}"

        self.equation_label.setText(equation)
        self.answer_label.setText("")
        self.current_solution = x

    def show_answer(self):
        if self.current_solution is not None:
            self.answer_label.setText(f"x = {self.current_solution}")

    def open_code_link(self):
        url = "website"
        webbrowser.open(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EasyLinearEquationGenerator()
    window.show()
    sys.exit(app.exec())
