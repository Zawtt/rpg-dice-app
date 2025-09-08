from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QSpinBox, QComboBox, QLineEdit
from src.dice.dice import Dice
from src.utils.history import RollHistory
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dice Roller")
        self.setGeometry(100, 100, 400, 300)

        self.history = RollHistory()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # ComboBox para escolher tipo de dado
        self.dice_type = QComboBox()
        self.dice_type.addItems(["d4", "d6", "d8", "d10", "d12", "d20", "d100"])
        self.layout.addWidget(self.dice_type)

        # SpinBox para quantidade de dados
        self.quantity = QSpinBox()
        self.quantity.setMinimum(1)
        self.quantity.setMaximum(20)
        self.quantity.setValue(1)
        self.layout.addWidget(self.quantity)

        # Input para modificador
        self.modifier = QLineEdit()
        self.modifier.setPlaceholderText("Modifier (+/-)")
        self.layout.addWidget(self.modifier)

        # Botão de rolar
        self.roll_button = QPushButton("Roll Dice")
        self.roll_button.clicked.connect(self.roll_dice)
        self.layout.addWidget(self.roll_button)

        # Label para mostrar resultado
        self.result_label = QLabel("Result: ")
        self.layout.addWidget(self.result_label)

    def roll_dice(self):
        sides = int(self.dice_type.currentText()[1:])
        quantity = self.quantity.value()
        modifier_text = self.modifier.text()
        modifier = int(modifier_text) if modifier_text else 0

        dice = Dice(sides)
        results, total = dice.roll(quantity, modifier)

        self.history.add((results, total))
        self.result_label.setText(f"Rolls: {results} | Total: {total}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
