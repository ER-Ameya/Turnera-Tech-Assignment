import sys
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtWidgets
import seaborn as sns
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import pandas as pd


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=15, height=14, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object, 
        # which defines a set of axes as self.axes.
        sc = MplCanvas(self, width=15, height=14, dpi=100)
        st = MplCanvas(self, width=15, height=14, dpi=100)

        # Create the pandas DataFrame.
        download_url = ("https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv")
        pd.set_option("display.max.columns", None) #So that pandas does not hide any columns

        df = pd.read_csv(download_url)

        # Line Graph Rank Vs Full time year round
        fig, ax = plt.subplots(figsize =(16, 9)) 
        plt.plot(df['Rank'], df['Full_time_year_round'], color='red', marker='o')
        plt.title('Rank Vs Full_time_year_round', fontsize=14)
        plt.xlabel('Rank', fontsize=14)
        plt.ylabel('Full_time_year_round', fontsize=14)
        plt.grid(True)
        plt.show()

        # Line Graph Part_time Vs Unemployment_rate
        fig, ax = plt.subplots(figsize =(16, 9)) 
        plt.plot(df['Part_time'], df['Unemployment_rate'], color='Blue', marker='o')
        plt.title('Part_time Vs Unemployment_rate', fontsize=14)
        plt.xlabel('Part_time', fontsize=14)
        plt.ylabel('Unemployment_rate', fontsize=14)
        plt.grid(True)
        plt.show()
+
        # plot the pandas DataFrame, passing in the 
        # matplotlib Canvas axes.
        # fig, ax = plt.subplots(figsize =(20, 20))
        # df.plot(ax=sc.axes)
        df[['Rank','Full_time_year_round']].plot(ax=sc.axes)
        df[['Part_time','Unemployment_rate']].plot(ax=st.axes)

        # bar graph between college rank and College jobs and Non College jobs.
        y = np.random.rand(10,3)
        y[:,0]= np.arange(10)

        ax = df.plot(x="Rank", y="College_jobs", kind="bar")
        df.plot(x="Rank", y="Non_college_jobs", kind="bar", ax=ax, color="C2")

        plt.xticks(np.arange(0, 173, 3), rotation=90)
        plt.title('Bar Plot', fontsize=14)
        plt.xlabel('Rank', fontsize=14)
        plt.ylabel('College Jobs vs Non College Jobs', fontsize=14)
        plt.grid(False)
        plt.show()

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc,st, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)
        layout.addWidget(st)
        

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
