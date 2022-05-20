import sys

import serial
from qtpy import QtWidgets as QtW
from qtpy.QtCore import Qt
import numpy as np

class FakeLaser:
    def __init__(self, port, baudrate=115200):
        self._arduino = serial.Serial(port, baudrate=baudrate)

    def set_brightness(self, brightness:np.uint8):
        """
        Set the brightness of the LED.

        Parameters
        ----------
        brightness : uint8
            Between 0 and 255
        """
        self.write_serial(str(np.uint8(brightness)))

    def write_serial(self, msg: str):
        self._arduino.write(msg.encode())


class LaserWidget(QtW.QWidget):
    def __init__(self, laser: FakeLaser, parent=None):
        super(LaserWidget, self).__init__(parent)
        self.laser = laser
        layout = QtW.QVBoxLayout()
        self.l1 = QtW.QLabel("LED Brightness (0-255)")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

        self.sb = QtW.QSpinBox()
        self.sb.setMinimum(0)
        self.sb.setMaximum(255)
        self.sb.setValue(125)
        self.sb.setKeyboardTracking(False)

        layout.addWidget(self.sb)
        self.sb.valueChanged.connect(lambda val: self.laser.write_serial(str(val)))
        # self.sb.valueChanged.connect(lambda val: print(val))
        self.setLayout(layout)
        self.setWindowTitle("Demo Custom Widget")


if __name__ == "__main__":
    app = QtW.QApplication(sys.argv)
    led = FakeLaser("/dev/ttyACM0")
    slider = LaserWidget(led)
    slider.show()
    sys.exit(app.exec_())
