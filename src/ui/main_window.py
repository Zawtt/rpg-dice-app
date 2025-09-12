from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QSpinBox, QComboBox, QLineEdit,
                             QListWidget, QFrame, QSizePolicy)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
from src.dice.dice import Dice
from src.utils.history import RollHistory
from src.ui.styles.styles import MAIN_WINDOW_STYLE, HISTORY_WIDGET_STYLE
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎲 Dice Roller Pro")
        self.setGeometry(200, 200, 600, 500)
        self.setMinimumSize(500, 400)

        self.history = RollHistory()
        
        # Aplicar estilos
        self.setStyleSheet(MAIN_WINDOW_STYLE)
        
        self.setup_ui()

    def setup_ui(self):
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(main_layout)

        # Título
        title_label = QLabel("🎲 DICE ROLLER PRO")
        title_label.setObjectName("title-label")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #4a90e2; margin: 10px 0;")
        main_layout.addWidget(title_label)

        # Seção de controles
        controls_frame = QFrame()
        controls_frame.setStyleSheet("QFrame { background-color: #353535; border-radius: 10px; padding: 15px; }")
        controls_layout = QVBoxLayout(controls_frame)
        controls_layout.setSpacing(12)

        # Linha 1: Tipo de dado
        dice_layout = QHBoxLayout()
        dice_label = QLabel("Tipo de Dado:")
        dice_label.setStyleSheet("font-weight: bold;")
        self.dice_type = QComboBox()
        self.dice_type.addItems(["d4", "d6", "d8", "d10", "d12", "d20", "d100"])
        self.dice_type.setCurrentText("d20")
        self.dice_type.setFixedHeight(40)
        
        dice_layout.addWidget(dice_label)
        dice_layout.addWidget(self.dice_type, 1)
        controls_layout.addLayout(dice_layout)

        # Linha 2: Quantidade
        quantity_layout = QHBoxLayout()
        quantity_label = QLabel("Quantidade:")
        quantity_label.setStyleSheet("font-weight: bold;")
        self.quantity = QSpinBox()
        self.quantity.setMinimum(1)
        self.quantity.setMaximum(20)
        self.quantity.setValue(1)
        self.quantity.setFixedHeight(40)
        
        quantity_layout.addWidget(quantity_label)
        quantity_layout.addWidget(self.quantity, 1)
        controls_layout.addLayout(quantity_layout)

        # Linha 3: Modificador
        modifier_layout = QHBoxLayout()
        modifier_label = QLabel("Modificador:")
        modifier_label.setStyleSheet("font-weight: bold;")
        self.modifier = QLineEdit()
        self.modifier.setPlaceholderText("Ex: +5, -2 (opcional)")
        self.modifier.setFixedHeight(40)
        
        modifier_layout.addWidget(modifier_label)
        modifier_layout.addWidget(self.modifier, 1)
        controls_layout.addLayout(modifier_layout)

        main_layout.addWidget(controls_frame)

        # Botão de rolar (maior e mais chamativo)
        self.roll_button = QPushButton("🎲 ROLAR DADOS")
        self.roll_button.clicked.connect(self.roll_dice)
        self.roll_button.setFixedHeight(50)
        self.roll_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                          stop: 0 #4a90e2, stop: 1 #357abd);
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
            }
            QPushButton:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                          stop: 0 #5ba0f2, stop: 1 #4a90e2);
            }
        """)
        main_layout.addWidget(self.roll_button)

        # Resultado
        self.result_label = QLabel("Clique em 'Rolar Dados' para começar!")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("""
            QLabel {
                background-color: #404040;
                border: 2px solid #4a90e2;
                border-radius: 10px;
                padding: 20px;
                font-size: 18px;
                font-weight: bold;
                min-height: 60px;
            }
        """)
        main_layout.addWidget(self.result_label)

        # Histórico
        history_label = QLabel("📜 Histórico de Rolagens:")
        history_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 10px;")
        main_layout.addWidget(history_label)

        self.history_list = QListWidget()
        self.history_list.setMaximumHeight(120)
        self.history_list.setStyleSheet(HISTORY_WIDGET_STYLE)
        main_layout.addWidget(self.history_list)

        # Botão para limpar histórico
        clear_history_btn = QPushButton("🗑️ Limpar Histórico")
        clear_history_btn.clicked.connect(self.clear_history)
        clear_history_btn.setFixedHeight(35)
        clear_history_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        main_layout.addWidget(clear_history_btn)

    def roll_dice(self):
        try:
            sides = int(self.dice_type.currentText()[1:])
            quantity = self.quantity.value()
            modifier_text = self.modifier.text().strip()
            modifier = int(modifier_text) if modifier_text else 0

            dice = Dice(sides)
            results, total = dice.roll(quantity, modifier)

            # Adicionar ao histórico
            self.history.add((results, total, sides, quantity, modifier))
            
            # Criar texto do resultado
            dice_text = f"{quantity}d{sides}"
            if modifier != 0:
                dice_text += f"{modifier:+d}"
            
            result_text = f"🎲 {dice_text}\n"
            result_text += f"Resultados: {results}\n"
            result_text += f"✨ Total: {total}"
            
            self.result_label.setText(result_text)
            
            # Adicionar ao histórico visual
            history_item = f"{dice_text} → {results} = {total}"
            self.history_list.insertItem(0, history_item)
            
            # Manter apenas os últimos 10 itens
            if self.history_list.count() > 10:
                self.history_list.takeItem(self.history_list.count() - 1)
            
            # Efeito visual no botão
            self.animate_button()
            
        except ValueError:
            self.result_label.setText("❌ Erro: Modificador inválido!")

    def animate_button(self):
        # Pequena animação no botão após rolar
        self.roll_button.setText("🎉 ROLADO!")
        QTimer.singleShot(500, lambda: self.roll_button.setText("🎲 ROLAR DADOS"))

    def clear_history(self):
        self.history_list.clear()
        self.history.history.clear()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())