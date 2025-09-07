import xml.etree.ElementTree as ET

class TemperatureConverter:
    # def __init__(self):
    #     self.converter = TemperatureConverter()

    def convert_celsius_to_fahrenheit (self,celsius):
        #converts the temperature from Celsius to Fahrenheit using F = 9/5 * C + 32
        return round((((9/5) * celsius) + 32), 1)


class ForecastXmlParser:
    def parse(self,converter):
        tree = ET.parse('forecast.xml')
        root = tree.getroot()
        for child in root:
            print(child[0].text,": ",child[1].text , " Celsius, ", converter.convert_celsius_to_fahrenheit(float(child[1].text)), " Fahrenheit")

temp_converter = TemperatureConverter()
forecast = ForecastXmlParser()
forecast.parse(temp_converter)