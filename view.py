# ... (existing code)

class GUI(QMainWindow):
    def __init__(self):
        # ... (existing code)

        self._createButtons()  # Update the button creation function

    # ... (existing code)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {
            # ... (existing buttons)
            'mm_to_cm': (4, 0),
            'cm_to_mm': (4, 1),
            'm_to_cm': (4, 2),
            'cm_to_m': (4, 3),
            'inch_to_cm': (4, 4),
            'cm_to_inch': (4, 5),
        }

        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(80, 40)  # Adjust the button size
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])

        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)
