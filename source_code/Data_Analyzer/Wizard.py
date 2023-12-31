import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QCoreApplication, pyqtSignal
from PyQt5.QtGui import QPixmap, QColor, QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QStyle,
                             QWizard, QWizardPage, QVBoxLayout, QPlainTextEdit,
                             QLabel, QLineEdit, QMainWindow, QFileDialog, QMessageBox)

from qt_material import apply_stylesheet
from step_1 import Ui_Form_Step1
from step_2 import Ui_Form_Step2
from step_3 import Ui_Form_None
from step_3_RT import Ui_Form_RT
from step_3_RI import Ui_Form_RI
import images_rc
import pandas as pd

class WizardPage1(QWizardPage, Ui_Form_Step1):
    def __init__(self, parent=None):
        super(WizardPage1, self).__init__(parent)
        self.setupUi(self)
        ui = Ui_Form_Step1()


        # self.registerField("smoothvalue*", self.spinBox)
        # self.registerField("peakfiltervalue", self.doubleSpinBox_2)
        # self.registerField("peakgroupvalue", self.doubleSpinBox_2)
    def slot1(self):
        QMessageBox.about(
            None,
            'Help',
            'A higher factor leading to a more pronounced smoothing effect, albeit potentially causing the loss of low-intensity peaks. Default: 5     ')

    def slot2(self):
        QMessageBox.about(
            None,
            'Help',
            'A high peak filter factor can filter out low-abundance peaks. Default: 10        ')

    def slot3(self):
        QMessageBox.about(
            None,
            'Help',
            'Set a smaller bin number when using a smaller data points per second in acquisition method development. e. g., Set bin number to 0.5 when data points per second is two     ')


class WizardPage2(QWizardPage, Ui_Form_Step2):
    def __init__(self, parent=None):
        super(WizardPage2, self).__init__(parent)
        self.setupUi(self)
        ui = Ui_Form_Step1()
        self.choose = "None"
        self.msp = ""
        self.RTRIinfo = ""
        self.demo = ""
        self.lineEdit = QLineEdit()
        self.pushButton.clicked.connect(self.openmsp)
        #self.pushButton_2.clicked.connect(self.opendemo)
        self.pushButton_2.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.clicked.connect(self.openRTRIinfo)
        self.comboBox.setCurrentIndex(0)
        self.comboBox.activated[str].connect(self.chooseRTRIinfo)


    def demo(self):
        rt_demo_example = pd.DataFrame(
            {'Name': ['Formaldehyde', 'Propene', 'Methyl Alcohol', 'Methyl formate', 'Methanethiol'],
             'RT': [0.984836066, 1.065983607, 1.305737705, 1.372131148, 1.479098361]})

        ri_demo_example = pd.DataFrame(
            {'RI': [400, 500, 600, 700, 800],
             'RT (min)': [1.575, 1.584, 2.036, 3.329, 5.45]})

        try:
            rt_demo_example.to_csv('Dataanalysis_RT_demo.csv', index=False)
            ri_demo_example.to_csv('Dataanalysis_RI_demo.csv', index=False)
            QMessageBox.about(
                None,
                'Help',
                'RT and RI sample files are stored in the same directory as the software')
        except:
            pass


    def tooltip1(self):
        QMessageBox.about(
            None,
            'Help',
            'Selecting type of retention information to be used in data analysis      ')


    def validatePage(self):

        if self.choose == "None":
            if self.msp != "":
                return True
            else:
                QMessageBox.critical(
                    None,
                    'Error',
                    'Please input the MSP file！')
                return False

        elif self.choose == "RT" or self.choose == "RI":
            #print(self.msp)
            #print(self.RTRIinfo)
            if self.msp != "" and self.RTRIinfo != "":
                return True
            elif self.msp == "" and self.RTRIinfo != "":
                QMessageBox.critical(
                    None,
                    'Error',
                    'Please input the MSP file！')
                return False
            elif self.msp != "" and self.RTRIinfo == "":
                QMessageBox.critical(
                    None,
                    'Error',
                    'Please input a retention information file！')
                return False
            else:
                QMessageBox.critical(
                    None,
                    'Error',
                    'Please input MPS file and retention information file！')
                return False

    def openmsp(self):
        self.msp, _ = QFileDialog.getOpenFileName(self, 'Open MSP File', './', 'MSP files (*.msp)')

    def opendemo(self):
        self.demo, _ =  QFileDialog.getOpenFileName(self, 'open file', './', 'All files (*.*)')

    def openRTRIinfo(self):
        self.RTRIinfo, _ = QFileDialog.getOpenFileName(self, 'Open RTRI File', './', 'CSV files (*.csv)')


    def chooseRTRIinfo(self, text):
        self.choose = text

        if self.choose == "None":
            self.pushButton_2.setEnabled(False)
            self.pushButton_4.setEnabled(False)
        elif self.choose == "RT":
            self.pushButton_2.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.label_4.setText("Import RT list")
            self.pushButton_4.setText("RT")

        elif self.choose == "RI":
            self.pushButton_2.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.label_4.setText("Import RI calibration data")
            self.pushButton_4.setText("RI")




class WizardPage3None(QWizardPage, Ui_Form_None):
    def __init__(self, parent=None):
        super(WizardPage3None, self).__init__(parent)

        self.setupUi(self)
        ui = Ui_Form_None()

        #隐藏Peak group search score weight和Direct search score weight
        self.label_8.setHidden(True)
        self.label_6.setHidden(True)
        self.doubleSpinBox_5.setHidden(True)
        self.doubleSpinBox_6.setHidden(True)
        self.pushButton_11.setHidden(True)
        self.pushButton_12.setHidden(True)

    def slot1(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.7       ')

    def slot2(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.3       ')
    def slot3(self):
        QMessageBox.about(
            None,
            'Help',
            'Peak group with ion number below this threshold will not be subjected to qualitative analysis      ')
    def slot4(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.2       ')
    def slot5(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.8       ')
    def slot6(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.4       ')



class WizardPage3RT(QWizardPage, Ui_Form_RT):
    def __init__(self, parent=None):
        super(WizardPage3RT, self).__init__(parent)
        self.setupUi(self)
        ui = Ui_Form_RT()
        self.radioButton.setChecked(True)
        self.doubleSpinBox_12.setEnabled(True)
        self.doubleSpinBox_7.setEnabled(True)
        self.doubleSpinBox_8.setEnabled(True)
        self.doubleSpinBox_9.setEnabled(True)
        self.radioButton.clicked.connect(self.choose1)


        self.label_16.setHidden(True)
        self.label_17.setHidden(True)
        self.doubleSpinBox_6.setHidden(True)
        self.doubleSpinBox_10.setHidden(True)
        self.pushButton_14.setHidden(True)
        self.pushButton_15.setHidden(True)

    def choose1(self, bool):

        if bool:
            self.doubleSpinBox_12.setEnabled(True)
            self.doubleSpinBox_7.setEnabled(True)
            self.doubleSpinBox_8.setEnabled(True)
            self.doubleSpinBox_9.setEnabled(True)
        else:
            self.doubleSpinBox_12.setEnabled(False)
            self.doubleSpinBox_7.setEnabled(False)
            self.doubleSpinBox_8.setEnabled(False)
            self.doubleSpinBox_9.setEnabled(False)



    def slot2(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.7       ')

    def slot3(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.3       ')

    def slot4(self):
        QMessageBox.about(
            None,
            'Help',
            'Component with ion number below this threshold will not be subjected to qualitative analysis      ')

    def slot5(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.2       ')

    def slot6(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.8       ')

    def slot7(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.4       ')

    def slot8(self):
        QMessageBox.about(
            None,
            'Help',
            'RT penalty will be applied only when RT difference exceeds this threshold      ')

    def slot9(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.05      ')

    def slot10(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.1       ')

    def slot11(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.05      ')




class WizardPage3RI(QWizardPage, Ui_Form_RI):
    def __init__(self, parent=None):
        super(WizardPage3RI, self).__init__(parent)
        self.setupUi(self)
        ui = Ui_Form_RI()
        self.radioButton.setChecked(True)
        self.doubleSpinBox_5.setEnabled(True)
        self.doubleSpinBox_99.setEnabled(True)
        self.doubleSpinBox_7.setEnabled(True)
        self.doubleSpinBox_8.setEnabled(True)
        self.doubleSpinBox_9.setEnabled(True)
        self.doubleSpinBox_13.setEnabled(True)
        self.spinBox_12.setEnabled(True)
        self.radioButton.clicked.connect(self.choose)


        self.label_16.setHidden(True)
        self.label_17.setHidden(True)
        self.doubleSpinBox_6.setHidden(True)
        self.doubleSpinBox_10.setHidden(True)
        self.pushButton_18.setHidden(True)
        self.pushButton_19.setHidden(True)

    def choose(self, bool):

        if bool:
            self.doubleSpinBox_5.setEnabled(True)
            self.doubleSpinBox_99.setEnabled(True)
            self.doubleSpinBox_7.setEnabled(True)
            self.doubleSpinBox_8.setEnabled(True)
            self.doubleSpinBox_9.setEnabled(True)
            self.doubleSpinBox_13.setEnabled(True)
            self.spinBox_12.setEnabled(True)
        else:
            self.doubleSpinBox_5.setEnabled(False)
            self.doubleSpinBox_99.setEnabled(False)
            self.doubleSpinBox_7.setEnabled(False)
            self.doubleSpinBox_8.setEnabled(False)
            self.doubleSpinBox_9.setEnabled(False)
            self.doubleSpinBox_13.setEnabled(False)
            self.spinBox_12.setEnabled(False)



    def slot2(self):
        QMessageBox.about(
            None,
            'Help',
            'Enter the allowed maximum RI       ')

    def slot3(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.7       ')

    def slot4(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.3       ')

    def slot5(self):
        QMessageBox.about(
            None,
            'Help',
            'Component with ion number below this threshold will not be subjected to qualitative analysis      ')

    def slot6(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.2       ')

    def slot7(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.8       ')

    def slot8(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.4       ')

    def slot9(self):
        QMessageBox.about(
            None,
            'Help',
            'RT penalty will be applied only when RT difference exceeds this threshold      ')

    def slot10(self):
        QMessageBox.about(
            None,
            'Help',
            'RI penalty window will be linearly scaled by this factor, setting it to 0 disables this feature. default: 2      ')

    def slot11(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.05      ')

    def slot12(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.2       ')

    def slot13(self):
        QMessageBox.about(
            None,
            'Help',
            'Default: 0.15      ')

    def slot14(self):
        QMessageBox.about(
            None,
            'Help',
            'RI below this threshold will use an alternative penalty factor     ')






class GoWizard(QWizard):
    _signal = pyqtSignal(dict)
    def __init__(self, *is_identification, parent=None):
        super(GoWizard, self).__init__(parent)
        if is_identification != ():
            self.is_identification = is_identification[0]
        else:
            self.is_identification = is_identification


        self.page1 = WizardPage1()
        self.page2 = WizardPage2()
        self.page3none = WizardPage3None()
        self.page3RT = WizardPage3RT()
        self.page3RI = WizardPage3RI()

        if self.is_identification != 1:
            self.addPage(self.page1)
            self.addPage(self.page2)
            self.addPage(self.page3none)
            self.addPage(self.page3RT)
            self.addPage(self.page3RI)
        else:
            self.addPage(self.page2)
            self.addPage(self.page3none)
            self.addPage(self.page3RT)
            self.addPage(self.page3RI)

        self.setStartId(0)

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.setWizardStyle(QWizard.ModernStyle)
        self.setWindowTitle('Choose Params')

        self.setOption(QWizard.NoBackButtonOnStartPage)
        self.setOption(QWizard.NoCancelButton)

        pix = QPixmap(640, 64)
        pix.fill(QColor(52, 104, 192))
        self.setPixmap(QWizard.BannerPixmap, pix)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)


        self.setTitleFormat(Qt.RichText)
        self.setSubTitleFormat(Qt.RichText)

        self.setButtonText(QWizard.NextButton, 'Next')
        self.setButtonText(QWizard.BackButton, 'Back')
        self.setButtonText(QWizard.FinishButton, 'Run')

        self.setWindowTitle('DataAnalyzer')

        self.resize(1000, 800)

        self.button(QWizard.FinishButton).clicked.connect(self.finalClicked)

    def nextId(self):
        if self.is_identification != 1:
            if self.currentId() == 1:
                combobox_index = self.page(1).comboBox.currentIndex()

                if combobox_index == 0:
                    return 2
                elif combobox_index == 1:
                    return 3
                elif combobox_index == 2:
                    return 4
            elif self.currentId() == 0:
                return 1
            else:
                return -1
        else:
            if self.currentId() == 0:
                combobox_index = self.page(0).comboBox.currentIndex()

                if combobox_index == 0:
                    return 1
                elif combobox_index == 1:
                    return 2
                elif combobox_index == 2:
                    return 3
            elif self.currentId() == 0:
                return 1
            else:
                return -1

    def finalClicked(self):
        # smoothvalue = self.field("smoothvalue")
        # peakfiltervalue = self.field("peakfiltervalue")
        # peakgroupvalue = self.field("peakgroupvalue")
        # print(f"smoothvalue: {smoothvalue}, peakfiltervalue: {peakfiltervalue}, peakgroupvalue:{peakgroupvalue}")


        all_parameter = {}
        #page1
        all_parameter["smooth_value"] = self.page1.spinBox.value()
        all_parameter["peak_filt_value"] = self.page1.doubleSpinBox.value()
        all_parameter["group_peak_factor"] = self.page1.doubleSpinBox_2.value()

        #page2
        all_parameter["msp"] = self.page2.msp
        all_parameter["chooseinfo"] = self.page2.choose
        all_parameter["RTRIinfo"] = self.page2.RTRIinfo
        #all_parameter["demo"] = self.page2.demo


        #page3-none
        all_parameter["page3none_match_weight"] = self.page3none.doubleSpinBox_3.value()
        all_parameter["page3none_r_match_weight"] = self.page3none.doubleSpinBox_4.value()
        all_parameter["page3none_group_weight"] = self.page3none.doubleSpinBox_6.value()
        all_parameter["page3none_direct_weight"] = self.page3none.doubleSpinBox_5.value()
        all_parameter["page3none_group_minimum_number_of_ions"] = self.page3none.spinBox_2.value()
        all_parameter["page3none_sim_threshold"] = self.page3none.doubleSpinBox_7.value()

        #page3-RT
        all_parameter["page3RT_search_wid"] = self.page3RT.doubleSpinBox_5.value()
        all_parameter["page3RT_match_weight"] = self.page3RT.doubleSpinBox_3.value()
        all_parameter["page3RT_r_match_weight"] = self.page3RT.doubleSpinBox_4.value()
        all_parameter["page3RT_group_weight"] = self.page3RT.doubleSpinBox_6.value()
        all_parameter["page3RT_direct_weight"] = self.page3RT.doubleSpinBox_10.value()
        all_parameter["page3RT_group_minimum_number_of_ions"] = self.page3RT.spinBox_2.value()
        all_parameter["page3RT_ri_participate"] = self.page3RT.radioButton.isChecked()
        all_parameter["page3RT_sim_threshold"] = self.page3RT.doubleSpinBox_11.value()
        all_parameter["page3RT_window"] = self.page3RT.doubleSpinBox_12.value()
        all_parameter["page3RT_level_factor"] = self.page3RT.doubleSpinBox_7.value()
        all_parameter["page3RT_max_penalty"] = self.page3RT.doubleSpinBox_8.value()
        all_parameter["page3RT_no_info_penalty"] = self.page3RT.doubleSpinBox_9.value()


        #page3-RI
        all_parameter["page3RI_search_wid"] = self.page3RI.spinBox_2.value()
        all_parameter["page3RI_match_weight"] = self.page3RI.doubleSpinBox_3.value()
        all_parameter["page3RI_r_match_weight"] = self.page3RI.doubleSpinBox_4.value()
        all_parameter["page3RI_group_weight"] = self.page3RI.doubleSpinBox_6.value()
        all_parameter["page3RI_direct_weight"] = self.page3RI.doubleSpinBox_10.value()
        all_parameter["page3RI_group_minimum_number_of_ions"] = self.page3RI.spinBox_3.value()
        all_parameter["page3RI_RI_max"] = self.page3RI.spinBox_4.value()
        all_parameter["page3RI_ri_participate"] = self.page3RI.radioButton.isChecked()
        all_parameter["page3RI_sim_threshold"] = self.page3RI.doubleSpinBox_11.value()

        all_parameter["page3RI_window"] = self.page3RI.doubleSpinBox_5.value()
        all_parameter["page3RI_window_scale"] = self.page3RI.doubleSpinBox_9.value()
        all_parameter["page3RI_level_factor"] = self.page3RI.doubleSpinBox_7.value()
        all_parameter["page3RI_max_penalty"] = self.page3RI.doubleSpinBox_8.value()
        all_parameter["page3RI_no_info_penalty"] = self.page3RI.doubleSpinBox_99.value()
        all_parameter["page3RI_inaccurate_ri_threshold"] = self.page3RI.spinBox_12.value()
        all_parameter["page3RI_inaccurate_ri_level_factor"] = self.page3RI.doubleSpinBox_13.value()
        #print(all_parameter)
        self._signal.emit(all_parameter)
        self.accept()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GoWizard()
    apply_stylesheet(app, theme='light_cyan_500.xml', invert_secondary=True)

    window.show()
    sys.exit(app.exec())


