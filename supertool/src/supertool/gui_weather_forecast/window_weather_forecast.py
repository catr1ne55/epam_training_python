import sys
from PyQt5 import QtWidgets
import gui_weather_forecast
import weather


class MainApplication(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainApplication, self).__init__()

        self.ui = gui_weather_forecast.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.current_button.clicked.connect(self.current_pressed)
        self.ui.forecast_button.clicked.connect(self.forecast_pressed)

    def current_pressed(self):
        location = self.ui.textEdit.toPlainText()
        if location:
            [lat, lon] = weather.get_coordinates(location)
            self.ui.listWidget.addItem('Current weather in {}:\n'.format(location))
            data = weather.get_weather_by_coordinates(lat, lon)
            self.ui.listWidget.addItem("Weather conditions: {}".format(data['weather'][0]['description']))
            self.ui.listWidget.addItem("Temperature is {} C".format(data['main']['temp']))
            self.ui.listWidget.addItem("Pressure is {}".format(data['main']['pressure']))
            self.ui.listWidget.addItem("Humidity is {} %".format(data['main']['humidity']))
            self.ui.listWidget.addItem("Wind speed {} m/s".format(data['wind']['speed']))
        else:
            self.ui.listWidget.addItem("Please, try again! You have to enter the location!")
        self.ui.listWidget.addItem("=" * 10)

    def forecast_pressed(self):
        location = self.ui.textEdit.toPlainText()
        if location:
            [lat, lon] = weather.get_coordinates(location)
            self.ui.listWidget.addItem('Forecast for 5 days every 3 hour:\n')
            data = weather.get_5days_weather_by_coordinates(lat, lon)
            for d in data['list']:
                self.ui.listWidget.addItem("Forecast for {}:".format(d['dt_txt']))
                self.ui.listWidget.addItem("Weather conditions: {}".format(d['weather'][0]['description']))
                self.ui.listWidget.addItem("Temperature is {} C".format(d['main']['temp']))
                self.ui.listWidget.addItem("Pressure is {}".format(d['main']['pressure']))
                self.ui.listWidget.addItem("Humidity is {} %".format(d['main']['humidity']))
                self.ui.listWidget.addItem("Wind speed {} m/s".format(d['wind']['speed']))
                self.ui.listWidget.addItem('-' * 10)
        else:
            self.ui.listWidget.addItem("Please, try again! You have to enter the directory!")
        self.ui.listWidget.addItem("=" * 10)


app = QtWidgets.QApplication(sys.argv)
window = MainApplication()
window.show()

sys.exit(app.exec_())