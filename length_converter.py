class LengthConverter:
    def millimeter_to_centimeter(self, millimeters):
        return millimeters / 10

    def centimeter_to_millimeter(self, centimeters):
        return centimeters * 10

    def meter_to_centimeter(self, meters):
        return meters * 100

    def centimeter_to_meter(self, centimeters):
        return centimeters / 100

    def inch_to_centimeter(self, inches):
        return inches * 2.54

    def centimeter_to_inch(self, centimeters):
        return centimeters / 2.54
