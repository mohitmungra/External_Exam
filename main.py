import sys
from PyQt5.QtWidgets import QApplication
from view import GUI
from controller import Controller
from model import Calculator 


# Client code
def main():
    """Main function."""
    pycalc = QApplication(sys.argv)
    view = GUI()
    view.show()

    # Create instances of the model and the controller
    model = Calculator()  # Updated model initialization
    Controller(model=model, view=view)

    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()
