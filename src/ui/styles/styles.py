MAIN_WINDOW_STYLE = """
    QWidget {
        background-color: #2b2b2b;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 12px;
    }
    
    QPushButton {
        background-color: #4a90e2;
        border: none;
        border-radius: 8px;
        padding: 12px;
        font-size: 14px;
        font-weight: bold;
        color: white;
        min-height: 20px;
    }
    
    QPushButton:hover {
        background-color: #5ba0f2;
        transform: translateY(-2px);
    }
    
    QPushButton:pressed {
        background-color: #3a80d2;
    }
    
    QComboBox {
        background-color: #404040;
        border: 2px solid #4a90e2;
        border-radius: 6px;
        padding: 8px;
        font-size: 13px;
        min-height: 15px;
    }
    
    QComboBox:hover {
        border-color: #5ba0f2;
    }
    
    QComboBox::drop-down {
        border: none;
        width: 20px;
    }
    
    QComboBox::down-arrow {
        image: none;
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        border-top: 5px solid #ffffff;
        margin-right: 5px;
    }
    
    QSpinBox {
        background-color: #404040;
        border: 2px solid #4a90e2;
        border-radius: 6px;
        padding: 8px;
        font-size: 13px;
        min-height: 15px;
    }
    
    QSpinBox:hover {
        border-color: #5ba0f2;
    }
    
    QLineEdit {
        background-color: #404040;
        border: 2px solid #4a90e2;
        border-radius: 6px;
        padding: 8px;
        font-size: 13px;
        min-height: 15px;
    }
    
    QLineEdit:hover {
        border-color: #5ba0f2;
    }
    
    QLineEdit:focus {
        border-color: #ffffff;
    }
    
    QLabel {
        background-color: transparent;
        font-size: 14px;
        padding: 5px;
    }
    
    .result-label {
        background-color: #404040;
        border: 2px solid #4a90e2;
        border-radius: 8px;
        padding: 15px;
        font-size: 16px;
        font-weight: bold;
        text-align: center;
        min-height: 30px;
    }
    
    .title-label {
        font-size: 24px;
        font-weight: bold;
        color: #4a90e2;
        text-align: center;
        margin: 10px 0;
    }
"""

HISTORY_WIDGET_STYLE = """
    QListWidget {
        background-color: #404040;
        border: 2px solid #4a90e2;
        border-radius: 6px;
        padding: 5px;
        font-size: 12px;
    }
    
    QListWidget::item {
        padding: 8px;
        border-bottom: 1px solid #555555;
        margin: 2px 0;
    }
    
    QListWidget::item:hover {
        background-color: #505050;
    }
    
    QListWidget::item:selected {
        background-color: #4a90e2;
    }
"""