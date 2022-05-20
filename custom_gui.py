
from __future__ import annotations
import sys
from arduino_widget import FakeLaser, LaserWidget
import qdarktheme
from pymmcore_plus import CMMCorePlus

from qtpy import QtWidgets as QtW
from qtpy.QtCore import Qt
from superqt import QCollapsible

# from ._camera_widget import MMCameraWidget

from micromanager_gui._gui_objects._xyz_stages import MMStagesWidget
from micromanager_gui._core_widgets._exposure_widget import DefaultCameraExposureWidget
# from ._config_widget import MMConfigurationWidget
# from ._mda_widget import MultiDWidget
# from ._objective_widget import MMObjectivesWidget
# from ._sample_explorer_widget import ExploreSample
# from ._shutters_widget import MMShuttersWidget
# from ._slider_dialog import SliderDialog
# from ._tab_widget import MMTabWidget
# from ._xyz_stages import MMStagesWidget


class CustomControls(QtW.QWidget):
    def __init__(self):
        super().__init__()

        # main widget
        self.main_layout = QtW.QVBoxLayout()
        self.main_layout.setContentsMargins(10, 0, 10, 0)
        self.main_layout.setSpacing(3)
        self.main_layout.setAlignment(Qt.AlignCenter)

        coll_sizepolicy = QtW.QSizePolicy(
            QtW.QSizePolicy.Minimum, QtW.QSizePolicy.Fixed
        )
        # sub_widgets
        self.stage_wdg = MMStagesWidget()

        # add stages collapsible
        self.stages_group = QtW.QGroupBox()
        self.stages_group_layout = QtW.QVBoxLayout()
        self.stages_group_layout.setSpacing(0)
        self.stages_group_layout.setContentsMargins(1, 0, 1, 1)

        self.stages_coll = QCollapsible(title="Stages")
        self.stages_coll.setSizePolicy(coll_sizepolicy)
        self.stages_coll.layout().setSpacing(0)
        self.stages_coll.layout().setContentsMargins(0, 0, 0, 0)
        self.stages_coll.addWidget(self.stage_wdg)
        self.stages_coll.expand(animate=False)
        self.stages_group_layout.addWidget(self.stages_coll)
        self.stages_group.setLayout(self.stages_group_layout)
        self.main_layout.addWidget(self.stages_group)

        # self.laser = LaserWidget(FakeLaser("/dev/ttyACM0"))
        # self.main_layout.addWidget(self.laser)
        self.exp = DefaultCameraExposureWidget()
        self.main_layout.addWidget(self.exp)
        self.setLayout(self.main_layout)

if __name__ == "__main__":
    app = QtW.QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet())
    core = CMMCorePlus.instance()
    core.loadSystemConfiguration()
    # stg = MMStagesWidget()
    # stg.show()
    # print(core.getLoadedDevices())
    controls = CustomControls()
    controls.show()
    sys.exit(app.exec_())
