from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtCore import Qt, QDateTime

class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__series_euro = QLineSeries()
        self.__series_euro.setName("Goldpreis Euro")

        dates = [
            QDateTime(2024, 12, 15, 0, 0, 0),
            QDateTime(2024, 12, 18, 0, 0, 0),
            QDateTime(2025, 1, 7, 0, 0, 0),
            QDateTime(2025, 2, 2, 0, 0, 0)
        ]

        self.__series_euro.append(dates[0].toMSecsSinceEpoch(), 1500)
        self.__series_euro.append(dates[1].toMSecsSinceEpoch(), 1800)
        self.__series_euro.append(dates[2].toMSecsSinceEpoch(), 1900)
        self.__series_euro.append(dates[3].toMSecsSinceEpoch(), 2000)

        self.__series_dollar = QLineSeries()
        self.__series_dollar.setName("Goldpreis Dollar")

        self.__series_dollar.append(dates[0].toMSecsSinceEpoch(), 1600)
        self.__series_dollar.append(dates[1].toMSecsSinceEpoch(), 1850)
        self.__series_dollar.append(dates[2].toMSecsSinceEpoch(), 1950)
        self.__series_dollar.append(dates[3].toMSecsSinceEpoch(), 2200)

        z_axis = QValueAxis()
        z_axis.setRange(1000, 2500)
        z_axis.setTitleText("Preis in Dollar")

        x_axis = QDateTimeAxis()
        x_axis.setFormat("dd.MM.yyyy")
        x_axis.setTitleText("Datum")
        x_axis.setTickCount(5)

        y_axis = QValueAxis()
        y_axis.setRange(1000, 2500)
        y_axis.setTitleText("Preis in €")

        chart = QChart()
        chart.setWindowTitle("Goldpreis")

        chart.addSeries(self.__series_euro)
        chart.addSeries(self.__series_dollar)

        chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)
        chart.addAxis(z_axis, Qt.AlignmentFlag.AlignRight)

        self.__series_euro.attachAxis(x_axis)
        self.__series_euro.attachAxis(y_axis)
        self.__series_dollar.attachAxis(x_axis)
        self.__series_dollar.attachAxis(z_axis)

        self.setChart(chart)
