from functools import partial
from length_converter import LengthConverter
ERROR_MSG = 'ERROR'

class Calculator:
    def __init(self):
        self.length_converter = LengthConverter()

    def length_conversion(self, value, from_unit, to_unit):
        if from_unit == "mm" and to_unit == "cm":
            return self.length_converter.millimeter_to_centimeter(value)
        elif from_unit == "cm" and to_unit == "mm":
            return self.length_converter.centimeter_to_millimeter(value)
        elif from_unit == "m" and to_unit == "cm":
            return self.length_converter.meter_to_centimeter(value)
        elif from_unit == "cm" and to_unit == "m":
            return self.length_converter.centimeter_to_meter(value)
        elif from_unit == "inch" and to_unit == "cm":
            return self.length_converter.inch_to_centimeter(value)
        elif from_unit == "cm" and to_unit == "inch":
            return self.length_converter.centimeter_to_inch(value)
        else:
            raise ValueError("Invalid conversion")

class Controller:
    """PyCalc's Controller."""
    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.getDisplayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.getDisplayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.getDisplayText() + sub_exp
        self._view.setDisplayText(expression)

    def _lengthConversion(self, from_unit, to_unit):
        try:
            value = float(self._view.getDisplayText())
            result = self._evaluate.length_conversion(value, from_unit, to_unit)
            self._view.setDisplayText(str(result))
        except ValueError:
            self._view.setDisplayText(ERROR_MSG)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C', 'mm_to_cm', 'cm_to_mm', 'm_to_cm', 'cm_to_m', 'inch_to_cm', 'cm_to_inch'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
        self._view.buttons['mm_to_cm'].clicked.connect(partial(self._lengthConversion, "mm", "cm"))
        self._view.buttons['cm_to_mm'].clicked.connect(partial(self._lengthConversion, "cm", "mm"))
        self._view.buttons['m_to_cm'].clicked.connect(partial(self._lengthConversion, "m", "cm"))
        self._view.buttons['cm_to_m'].clicked.connect(partial(self._lengthConversion, "cm", "m"))
        self._view.buttons['inch_to_cm'].clicked.connect(partial(self._lengthConversion, "inch", "cm"))
        self._view.buttons['cm_to_inch'].clicked.connect(partial(self._lengthConversion, "cm", "inch"))
