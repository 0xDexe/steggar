import os
import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class App(QWidget):
    
    def initImage(self, filepath):
        # Load the image in grayscale mode
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        fshift = np.fft.fftshift(np.fft.fft2(img))
        magnitude_spectrum = 20*np.log(np.abs(fshift))


    def __init__(self):
        super().__init__()
        self.title = 'FFT'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('image.jpeg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

