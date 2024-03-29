import io
import os
import images_rc
from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
import pickle
import numpy as np
import pandas as pd
import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidget, QHBoxLayout, \
    QTableWidgetItem, QVBoxLayout, QMessageBox, QPushButton, QComboBox
from dataanalysis import Ui_MainWindow
import sys
from qt_material import apply_stylesheet
from pyecharts.charts import Bar, Line, Grid
from pyecharts import options as opts
from Wizard import GoWizard
from Data_Analyzer import DataAnalysis



class WorkerThread(QThread):
    finished = pyqtSignal(int)
    all_df_signal = pyqtSignal(object)

    def __init__(self, total_result_pkl, peak_group_pkl, filename, smooth_value, peak_filt_value, group_peak_factor,
                 msp, chooseinfo,
                 RTRIinfo,
                 page3none_match_weight, page3none_r_match_weight, page3none_group_weight, page3none_direct_weight,
                 page3none_group_minimum_number_of_ions, page3none_sim_threshold, page3RT_search_wid,
                 page3RT_match_weight, page3RT_r_match_weight, page3RT_group_weight, page3RT_direct_weight,
                 page3RT_group_minimum_number_of_ions, page3RT_ri_participate, page3RT_sim_threshold, page3RT_window,
                 page3RT_level_factor, page3RT_max_penalty, page3RT_no_info_penalty,
                 page3RI_search_wid, page3RI_match_weight,
                 page3RI_r_match_weight, page3RI_group_weight, page3RI_direct_weight,
                 page3RI_group_minimum_number_of_ions,
                 page3RI_RI_max, page3RI_ri_participate, page3RI_sim_threshold, page3RI_window,
                 page3RI_window_scale, page3RI_level_factor, page3RI_max_penalty, page3RI_no_info_penalty,
                 page3RI_inaccurate_ri_threshold, page3RI_inaccurate_ri_level_factor):
        super().__init__()

        self.total_result_pkl = total_result_pkl
        self.peak_group_pkl = peak_group_pkl
        self.filename = filename
        self.smooth_value = smooth_value
        self.peak_filt_value = peak_filt_value
        self.group_peak_factor = group_peak_factor
        self.msp = msp
        self.chooseinfo = chooseinfo
        self.RTRIinfo = RTRIinfo
        self.page3none_match_weight = page3none_match_weight
        self.page3none_r_match_weight = page3none_r_match_weight
        self.page3none_group_weight = page3none_group_weight
        self.page3none_direct_weight = page3none_direct_weight
        self.page3none_group_minimum_number_of_ions = page3none_group_minimum_number_of_ions
        self.page3none_sim_threshold = page3none_sim_threshold
        self.page3RT_search_wid = page3RT_search_wid
        self.page3RT_match_weight = page3RT_match_weight
        self.page3RT_r_match_weight = page3RT_r_match_weight
        self.page3RT_group_weight = page3RT_group_weight
        self.page3RT_direct_weight = page3RT_direct_weight
        self.page3RT_group_minimum_number_of_ions = page3RT_group_minimum_number_of_ions
        self.page3RT_ri_participate = page3RT_ri_participate
        self.page3RT_sim_threshold = page3RT_sim_threshold
        self.page3RT_window = page3RT_window
        self.page3RT_level_factor = page3RT_level_factor
        self.page3RT_max_penalty = page3RT_max_penalty
        self.page3RT_no_info_penalty = page3RT_no_info_penalty
        self.page3RI_search_wid = page3RI_search_wid
        self.page3RI_match_weight = page3RI_match_weight
        self.page3RI_r_match_weight = page3RI_r_match_weight
        self.page3RI_group_weight = page3RI_group_weight
        self.page3RI_direct_weight = page3RI_direct_weight
        self.page3RI_group_minimum_number_of_ions = page3RI_group_minimum_number_of_ions
        self.page3RI_RI_max = page3RI_RI_max
        self.page3RI_ri_participate = page3RI_ri_participate
        self.page3RI_sim_threshold = page3RI_sim_threshold
        self.page3RI_window = page3RI_window
        self.page3RI_window_scale = page3RI_window_scale
        self.page3RI_level_factor = page3RI_level_factor
        self.page3RI_max_penalty = page3RI_max_penalty
        self.page3RI_no_info_penalty = page3RI_no_info_penalty
        self.page3RI_inaccurate_ri_threshold = page3RI_inaccurate_ri_threshold
        self.page3RI_inaccurate_ri_level_factor = page3RI_inaccurate_ri_level_factor

    def run(self):
        self.mymainwindow = MyMainWindow()

        all_pkl = self.mymainwindow.Main(self.total_result_pkl, self.peak_group_pkl, self.filename, self.smooth_value,
                                         self.peak_filt_value, self.group_peak_factor, self.msp, self.chooseinfo,
                                         self.RTRIinfo,
                                         self.page3none_match_weight, self.page3none_r_match_weight,
                                         self.page3none_group_weight, self.page3none_direct_weight,
                                         self.page3none_group_minimum_number_of_ions, self.page3none_sim_threshold,
                                         self.page3RT_search_wid,
                                         self.page3RT_match_weight, self.page3RT_r_match_weight,
                                         self.page3RT_group_weight, self.page3RT_direct_weight,
                                         self.page3RT_group_minimum_number_of_ions, self.page3RT_ri_participate,
                                         self.page3RT_sim_threshold, self.page3RT_window,
                                         self.page3RT_level_factor, self.page3RT_max_penalty,
                                         self.page3RT_no_info_penalty,
                                         self.page3RI_search_wid, self.page3RI_match_weight,
                                         self.page3RI_r_match_weight, self.page3RI_group_weight,
                                         self.page3RI_direct_weight, self.page3RI_group_minimum_number_of_ions,
                                         self.page3RI_RI_max, self.page3RI_ri_participate, self.page3RI_sim_threshold,
                                         self.page3RI_window,
                                         self.page3RI_window_scale, self.page3RI_level_factor, self.page3RI_max_penalty,
                                         self.page3RI_no_info_penalty,
                                         self.page3RI_inaccurate_ri_threshold, self.page3RI_inaccurate_ri_level_factor)

        self.all_df_signal.emit(all_pkl)
        self.finished.emit(0)
        # except:
        #     self.finished.emit(1)

class MyMainWindow(QMainWindow, Ui_MainWindow, DataAnalysis):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.show_qualitative = False
        self.input_file = ''
        self.ion_num = 0
        self.choose = "s"
        self.choose_peak_group = ''
        self.total_result_pkl = ''
        self.peak_group_pkl = ''
        self.vboxlayout = QHBoxLayout(self.frame_5)
        self.browser = QWebEngineView()
        self.vboxlayout1 = QHBoxLayout(self.widget)
        self.browser1 = QWebEngineView()
        self.resize(1400, 900)

        layout = QVBoxLayout(self.frame_7)
        self.group_info = QTableWidget(self)
        layout.addWidget(self.group_info)
        self.menuRe_analysis.setEnabled(False)
        self.progressBar.setRange(0, 100)
        self.progress_value = 0
        self.progressBar.hide()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress_bar)
        self.widget_2.setHidden(True)

    def add_group_peak_table(self, peak_group_df, qualitative_and_quantitative_analysis_result, choose,
                             show_qualitative, ion_num):

        self.tableWidget.clear()


        peak_group_df_tmp = peak_group_df.copy()
        qualitative_and_quantitative_analysis_result_tmp = qualitative_and_quantitative_analysis_result.copy()

        peak_group_df_tmp = peak_group_df_tmp[peak_group_df_tmp["ion_num"] >= ion_num]
        peak_group_df_tmp = peak_group_df_tmp.reset_index(drop=True)
        # peak_group_df_tmp["rt"] = round(pd.Series(peak_group_df_tmp.rt), 2).to_list()
        peak_group_df_tmp["rt"] = np.round(peak_group_df_tmp["rt"].astype(np.float64), decimals=2).to_list()
        # print("peak_group_df_tmp", peak_group_df_tmp)
        qualitative_and_quantitative_analysis_result_tmp["rt"] = round(
            pd.Series(qualitative_and_quantitative_analysis_result_tmp.index), 2).to_list()
        # qualitative_and_quantitative_analysis_result_tmp.to_csv("C:/Users/86724/Desktop/ssss.csv")
        # peak_group_df_tmp.to_csv("C:/Users/86724/Desktop/bbbb.csv")
        qualitative_and_quantitative_analysis_result_tmp = qualitative_and_quantitative_analysis_result_tmp.iloc[:,
                                                           [0, 7]]


        if "Kovats_RI" in peak_group_df_tmp.columns:
            merge_df = pd.merge(peak_group_df_tmp.iloc[:, [0, 9]], qualitative_and_quantitative_analysis_result_tmp,
                                how="left",
                                on="rt")

            merge_df["Kovats_RI"] = merge_df["Kovats_RI"].astype(int)
            if show_qualitative:
                merge_df = merge_df[merge_df['Best_match_name'] != 'Unknown']

            self.tableWidget.setRowCount(merge_df.shape[0])
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setHorizontalHeaderLabels(
                ["RT", "RI", "Best match", "Quant Ion", "Area", "Height"])
            flag = 3
        else:

            merge_df = pd.merge(peak_group_df_tmp.iloc[:, [0]], qualitative_and_quantitative_analysis_result_tmp,
                                how="left",
                                on="rt")
            if show_qualitative:
                merge_df = merge_df[merge_df['Best_match_name'] != 'Unknown']
            self.tableWidget.setRowCount(merge_df.shape[0])
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderLabels(
                ["RT", "Best match", "Quant Ion", "Area", "Height"])
            flag = 2
        if choose == "min":
            merge_df["rt"] = np.round(merge_df["rt"].astype(np.float64) / 60, decimals=2)



        for row in range(merge_df.shape[0]):
            if choose == "min":

                son_choose_ion_df = self.choose_ion_df[
                    np.round(self.choose_ion_df["Peak_group"].astype(np.float64) / 60, decimals=2) == merge_df.iloc[
                        row, 0]]
            else:
                son_choose_ion_df = self.choose_ion_df[
                    self.choose_ion_df["Peak_group"] == merge_df.iloc[row, 0]]

            combo_box = QComboBox()

            ion_list = list(son_choose_ion_df["Ion"])
            if choose == "min":
                default_ion = peak_group_df_tmp[
                    np.round(peak_group_df_tmp["rt"].astype(np.float64) / 60, decimals=2) == merge_df.iloc[
                        row, 0]].iloc[0, 8]
            else:
                default_ion = peak_group_df_tmp[
                    np.round(peak_group_df_tmp["rt"].astype(np.float64), decimals=2) == merge_df.iloc[row, 0]].iloc[
                    0, 8]
            ion_list.remove(int(default_ion))
            ion_list.insert(0, int(default_ion))
            for i in ion_list:
                combo_box.addItem(str(i))
            combo_box.activated[str].connect(lambda item: self.change_ion(item, flag))

            self.tableWidget.setCellWidget(row, flag, combo_box)

            self.tableWidget.setItem(row, flag+1, QTableWidgetItem(
                str('{:.2e}'.format(son_choose_ion_df.loc[son_choose_ion_df["Ion"] == default_ion].iloc[0, 2]))))
            self.tableWidget.setItem(row, flag+2, QTableWidgetItem(
                str('{:.2e}'.format(son_choose_ion_df.loc[son_choose_ion_df["Ion"] == default_ion].iloc[0, 3]))))

            for col in range(merge_df.shape[1]):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(merge_df.iloc[row, col])))

        self.tableWidget.setCurrentCell(0, 0)
        self.tableWidget.clicked.connect(self.click_group_peak)
        self.tableWidget.clicked.connect(self.click_group_info_table)

        model = self.tableWidget.model()
        index = model.index(0, 0)
        self.click_group_peak(index)
        self.click_group_info_table(index)

    def change_ion(self, item, flag):
        # self.tableWidget.setItem(0, 0, QTableWidgetItem("sss"))
        row = self.tableWidget.currentRow()
        if self.choose == "min":
            line = self.choose_ion_df.loc[
                (np.round(self.choose_ion_df["Peak_group"].astype(np.float64) / 60, decimals=2) == float(
                    self.tableWidget.item(row, 0).text())) & (
                        self.choose_ion_df['Ion'] == int(item))]
        else:
            line = self.choose_ion_df.loc[
                (self.choose_ion_df['Peak_group'] == float(self.tableWidget.item(row, 0).text())) & (
                        self.choose_ion_df['Ion'] == int(item))]

        new_area = '{:.2e}'.format(float(line["Relative_Peak_Area"]))
        new_height = '{:.2e}'.format(float(line["Peak_Height"]))
        self.tableWidget.setItem(row, flag+1, QTableWidgetItem(str(new_area)))
        self.tableWidget.setItem(row, flag+2, QTableWidgetItem(str(new_height)))

    def click_group_peak(self, item):

        self.browser.setHtml('')
        # print("item", item)
        row = item.row()
        self.choose_peak_group = self.tableWidget.item(row, 0).text()
        # print("choose_peak_group", self.choose_peak_group)
        # print("type-choose_peak-group", type(self.choose_peak_group))
        # print("round(self.peak_group_df.rt, 2)", round(self.peak_group_df.rt, 2))
        # print("self.peak_group_df.rt", self.peak_group_df.rt)
        if self.choose == "min":
            tmp = self.peak_group_df.copy()
            tmp["rt"] = np.round(tmp["rt"].astype(np.float64), decimals=2).to_list()
            line = tmp[np.round(tmp.rt.astype(np.float64) / 60, decimals=2) == round(
                float(self.choose_peak_group), 2)]

            del tmp
        else:
            line = self.peak_group_df[
                np.round(self.peak_group_df.rt.astype(np.float64), decimals=2) == round(float(self.choose_peak_group),
                                                                                        2)]

        left = float(line["left"])
        right = float(line["right"])
        ions = line["ions"].iloc[0]
        # print("left", left)
        # print("right", right)
        # print("ions", ions)
        x = self.smooth_df.loc[left: right, :].index.values.tolist()
        # print("x**************", x)
        # print("ions:", ions)

        width = str(self.frame_5.frameGeometry().width() - 40) + "px"
        height = str(self.frame_5.frameGeometry().height() - 40) + "px"
        # print("height:", height)
        # print("width:", width)

        c = Line(init_opts=opts.InitOpts(theme="walden", animation_opts=opts.AnimationOpts(animation=False)))

        c.set_global_opts(
            title_opts=opts.TitleOpts(title="EIC", pos_top='0'),
            xaxis_opts=opts.AxisOpts(type_="value", is_scale=True, splitline_opts=opts.SplitLineOpts(is_show=False)),
            yaxis_opts=opts.AxisOpts(name="1e7", splitline_opts=opts.SplitLineOpts(is_show=False)),

            toolbox_opts=opts.ToolboxOpts(
                is_show=True,
                orient="horizontal",
                feature={
                    "dataZoom": {"show": True, "title": {"zoom":"Zoom", "back":"Back"}},
                    "dataView": {"show": True, "title": "Data View", "lang":["DataView", "Close", "Refresh"]},
                    "restore": {"show": True, "title": "Restore"},
                    }),
            legend_opts=opts.LegendOpts(
                type_='scroll',
                is_show=True,
                pos_top='15%',
                legend_icon="circle")
        )
        c.add_xaxis(xaxis_data=x)

        # if self.choose_peak_group == "84.51":
        #     ions = pd.DataFrame({"intensity":[29,999,16,4]}, index=['43','44','45','46'])
        # else:
        #     ions = pd.DataFrame({"intensity": [999]}, index=['60'])

        # print("ions:", ions)
        # print("type-ions", type(ions))
        for i in ions.index.values.tolist():
            # print("i", i)
            # print("type(i)", type(i))

            y = [x / 10000000 for x in (list(self.smooth_df.loc[left: right, i]))]
            # print("y", y)
            c.add_yaxis(
                series_name=str(i),
                y_axis=y,
                symbol="none",
                is_symbol_show=True,
                label_opts=opts.LabelOpts(is_show=False),

            )
        c.set_series_opts(
            linestyle_opts=opts.LineStyleOpts(width=2)
        )

        g = Grid()
        g.width = width
        g.height = height
        g.add(c, grid_opts=opts.GridOpts(pos_top='30%', pos_bottom='10%'))

        self.browser.setHtml(g.render_embed())
        self.vboxlayout.addWidget(self.browser)

        ##画初始ms比对图
        self.widget_2.setHidden(False)
        self.radioButton_2.setChecked(False)
        if self.choose == "min":
            tmp = self.qualitative_and_quantitative_analysis_result.copy()
            tmp.index = np.round(tmp.index.astype(np.float64), decimals=2).to_list()
            qua_line = tmp[
                np.around(tmp.index / 60, decimals=2) == float(
                    self.choose_peak_group)]

            del tmp


        else:
            qua_line = self.qualitative_and_quantitative_analysis_result[
                np.around(self.qualitative_and_quantitative_analysis_result.index, decimals=2) == float(
                    self.choose_peak_group)]
        # print("qua_line***************", qua_line)
        if qua_line.empty == False:
            self.browser1.setHtml('')
            best_match_name = qua_line.iloc[0, 0]
            # print("best_match_name:", best_match_name)
            all_match = qua_line["All_match"].iloc[0]
            # print("type-all_match", type(all_match))
            # print("all_match:", all_match)
            if best_match_name.split("_")[-1] == "analogue":
                self.click_match = best_match_name
                self.mz = eval(all_match.loc[best_match_name.split("_")[0], "mz"])
                self.intensity_s = eval(all_match.loc[best_match_name.split("_")[0], "intensity_s"])
                self.intensity_l = eval(all_match.loc[best_match_name.split("_")[0], "intensity_l"])
                self.mz_direct = eval(all_match.loc[best_match_name.split("_")[0], "mz_direct"])
                self.intensity_s_direct = eval(all_match.loc[best_match_name.split("_")[0], "intensity_s_direct"])
                self.intensity_l_direct = eval(all_match.loc[best_match_name.split("_")[0], "intensity_l_direct"])
                self.draw_ms_picture(self.mz, self.intensity_s, self.intensity_l, best_match_name)
            else:
                if best_match_name != "Unknown":
                    self.click_match = best_match_name
                    self.mz = eval(all_match.loc[best_match_name, "mz"])
                    self.intensity_s = eval(all_match.loc[best_match_name, "intensity_s"])
                    self.intensity_l = eval(all_match.loc[best_match_name, "intensity_l"])
                    self.mz_direct = eval(all_match.loc[best_match_name.split("_")[0], "mz_direct"])
                    self.intensity_s_direct = eval(all_match.loc[best_match_name.split("_")[0], "intensity_s_direct"])
                    self.intensity_l_direct = eval(all_match.loc[best_match_name.split("_")[0], "intensity_l_direct"])

                    self.draw_ms_picture(self.mz, self.intensity_s, self.intensity_l, best_match_name)


        else:
            self.browser1.setHtml('')

    def ischange(self, bool):
        if bool:
            self.radioButton_2.setText("Spectra of apex point")
            self.draw_ms_picture(self.mz_direct, self.intensity_s_direct, self.intensity_l_direct, self.click_match)
        else:
            self.radioButton_2.setText("Spectra of component")
            self.draw_ms_picture(self.mz, self.intensity_s, self.intensity_l, self.click_match)

    def click_ms_picture(self, item):
        self.radioButton_2.setChecked(False)
        row = item.row()
        self.click_match = self.group_info.item(row, 0).text()

        if self.click_match != "NA":
            if self.choose == "min":

                tmp = self.qualitative_and_quantitative_analysis_result.copy()
                tmp.index = np.round(tmp.index.astype(np.float64), decimals=2).to_list()
                qua_line = tmp[
                    np.around(tmp.index / 60, decimals=2) == float(
                        self.choose_peak_group)]

                del tmp
            else:
                qua_line = self.qualitative_and_quantitative_analysis_result[
                    np.around(self.qualitative_and_quantitative_analysis_result.index, decimals=2) == float(
                        self.choose_peak_group)]
            # print("qua_line***************", qua_line)
            all_match = qua_line["All_match"].iloc[0]
            self.mz = eval(all_match.loc[self.click_match, "mz"])

            self.intensity_s = eval(all_match.loc[self.click_match, "intensity_s"])
            self.intensity_l = eval(all_match.loc[self.click_match, "intensity_l"])
            self.intensity_s_direct = eval(all_match.loc[self.click_match, "intensity_s_direct"])
            self.intensity_l_direct = eval(all_match.loc[self.click_match, "intensity_l_direct"])

            self.draw_ms_picture(self.mz, self.intensity_s, self.intensity_l, self.click_match)

    def draw_ms_picture(self, mz, intensity_s, intensity_l, name):

        self.browser1.setHtml('')
        x_index = list(mz)
        y_value1 = [round(x, 1) for x in intensity_s]
        y_value2 = ['NA' if x == 0 else -x for x in intensity_l]

        bar = (
            Bar(init_opts=opts.InitOpts(theme="walden", animation_opts=opts.AnimationOpts(animation=False)))
            .add_xaxis(x_index)
            .add_yaxis("Search", y_value1, stack="stack1", bar_width=1,
                       label_opts=opts.LabelOpts(position="top", formatter="{b}"),
                       itemstyle_opts=opts.ItemStyleOpts(color='red'))
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(is_show=False, splitline_opts=opts.SplitLineOpts(is_show=False)),
                yaxis_opts=opts.AxisOpts(
                    axislabel_opts=opts.LabelOpts(is_show=False)
                ),
                title_opts=opts.TitleOpts(title="Spectrometry Comparison", pos_top='0%', subtitle=name),
                datazoom_opts=opts.DataZoomOpts(range_start=0, range_end=100, type_="inside"),
                toolbox_opts=opts.ToolboxOpts(
                    is_show=True,
                    feature={
                        "dataZoom": {"show": True, "title": {"zoom": "Zoom", "back": "Back"}},
                        "dataView": {"show": True, "title": "Data View", "lang": ["DataView", "Close", "Refresh"]},
                        "restore": {"show": True, "title": "Restore"},
                    }),
                tooltip_opts=opts.TooltipOpts(
                    is_show=True,
                    trigger="axis",
                ),
                legend_opts=opts.LegendOpts(
                    type_="plain",
                    is_show=True,
                    pos_top='15%',
                    legend_icon="circle")
            )

        )

        bar.add_yaxis(
            "Library",
            y_value2,
            itemstyle_opts=opts.ItemStyleOpts(color='blue'),
            stack="stack1", bar_width=1,
            label_opts=opts.LabelOpts(
                position="bottom",
                formatter="{b}",

            ),
        )
        width = str(self.widget.frameGeometry().width() - 30) + "px"
        height = str(self.frame_6.frameGeometry().height() - 70) + "px"

        g = Grid()
        g.width = width
        g.height = height
        g.add(bar, grid_opts=opts.GridOpts(pos_top='30%', pos_bottom='5%'))

        self.browser1.setHtml(g.render_embed())
        self.vboxlayout1.addWidget(self.browser1)

    def click_group_info_table(self, item):

        self.group_info.clear()
        row = item.row()
        choose_peak_group = self.tableWidget.item(row, 0).text()
        if self.choose == "min":

            tmp = self.qualitative_and_quantitative_analysis_result.copy()
            tmp.index = np.round(tmp.index.astype(np.float64), decimals=2).to_list()
            line = tmp[np.around(
                pd.Series(tmp.index,
                          index=tmp.index) / 60, decimals=2) == float(
                choose_peak_group)]

            del tmp
        else:
            line = self.qualitative_and_quantitative_analysis_result[np.around(
                pd.Series(self.qualitative_and_quantitative_analysis_result.index,
                          index=self.qualitative_and_quantitative_analysis_result.index), decimals=2) == float(
                choose_peak_group)]
        if line.empty == False:
            if line["All_match"].iloc[0].empty == False:
                # all_match_df = line["All_match"].iloc[0].loc[:, ["Score", "Reference_RT", "Delta_RT"]].reset_index()

                try:
                    all_match_df = line["All_match"].iloc[0].iloc[:, [0, 7, 8]].reset_index()
                    chooseinfo =all_match_df.columns[2]
                # print("all_match_df***************", all_match_df)
                except:
                    all_match_df = line["All_match"].iloc[0].iloc[:, [0]].reset_index()
                    chooseinfo = ''
                all_match_df['Score'] = all_match_df['Score'].astype('float64')
                if chooseinfo == 'Reference_RT':
                    # RT保留两位小数
                    all_match_df = all_match_df.round({'Score': 2, 'Reference_RT': 2, 'Delta_RT': 2})
                    self.group_info.setColumnCount(4)
                    self.group_info.setRowCount(all_match_df.shape[0])
                    self.group_info.setHorizontalHeaderLabels(['Name', 'Score', 'RT', 'ΔRT'])
                elif chooseinfo == 'Reference_RI':


                    all_match_df = all_match_df.round({'Score': 2})
                    all_match_df['Reference_RI'] = all_match_df['Reference_RI'].astype(int)
                    all_match_df['Delta_RI'] = all_match_df['Delta_RI'].astype(int)
                    self.group_info.setColumnCount(4)
                    self.group_info.setRowCount(all_match_df.shape[0])
                    self.group_info.setHorizontalHeaderLabels(['Name', 'Score', 'RI', 'ΔRI'])

                else:
                    all_match_df = all_match_df.round({'Score': 2, 'Reference_RI': 0, 'Delta_RI': 0})
                    self.group_info.setColumnCount(4)
                    self.group_info.setRowCount(all_match_df.shape[0])
                    self.group_info.setHorizontalHeaderLabels(['Name', 'Score', 'RT/RI', 'ΔRT/RI'])



                for row in range(all_match_df.shape[0]):
                    for col in range(all_match_df.shape[1]):
                        self.group_info.setItem(row, col, QTableWidgetItem(str(all_match_df.iloc[row, col])))

                self.group_info.clicked.connect(self.click_ms_picture)

            else:
                self.group_info.setColumnCount(4)
                self.group_info.setRowCount(1)
                self.group_info.setHorizontalHeaderLabels(['Name', 'Score', 'RT/RI', 'ΔRT/RI'])

                self.group_info.setItem(0, 0, QTableWidgetItem('NA'))
                self.group_info.setItem(0, 1, QTableWidgetItem('NA'))
                self.group_info.setItem(0, 2, QTableWidgetItem('NA'))
                self.group_info.setItem(0, 3, QTableWidgetItem('NA'))


        else:
            self.group_info.setColumnCount(4)
            self.group_info.setRowCount(1)
            self.group_info.setHorizontalHeaderLabels(['Name', 'Score', 'RT/RI', 'ΔRT/RI'])

            self.group_info.setItem(0, 0, QTableWidgetItem('NA'))
            self.group_info.setItem(0, 1, QTableWidgetItem('NA'))
            self.group_info.setItem(0, 2, QTableWidgetItem('NA'))
            self.group_info.setItem(0, 3, QTableWidgetItem('NA'))

    def open_data_mzML(self):
        _input, _ = QFileDialog.getOpenFileNames(self, 'Open mzML file', './', 'MZML files (*.mzML)')
        if _input != []:
            self.input_file = _input[0]
            self.total_result_pkl = ''
            self.peak_group_pkl = ''
            self.wizard = GoWizard()
            self.wizard._signal.connect(self.get_parm)

            self.wizard.show()
        else:
            QMessageBox.critical(
                None,
                'Error',
                'Please input a file！')

    def open_data_cdf(self):
        _input, _ = QFileDialog.getOpenFileNames(self, 'Open cdf file', './', 'CDF files (*.cdf)')
        if _input != []:
            self.input_file = _input[0]
            self.total_result_pkl = ''
            self.peak_group_pkl = ''
            self.wizard = GoWizard()
            self.wizard._signal.connect(self.get_parm)
            self.wizard.show()
        else:
            QMessageBox.critical(
                None,
                'Error',
                'Please input a file！')

    def open_project(self):
        _input, _ = QFileDialog.getOpenFileNames(self, 'Open project file(pkl)', './', 'PKL files (total_result*.pkl)')
        if _input != []:
            self.total_result_pkl = _input[0]
            self.parm_list = [self.total_result_pkl, self.peak_group_pkl] + [""] * 41
            self.run()

    def identification(self):

        self.peak_group_pkl = self.all_pkl[0]
        self.total_result_pkl = ''
        self.wizard = GoWizard(1)
        self.wizard._signal.connect(self.get_parm)
        self.wizard.show()

    def all_processing(self):
        if self.total_result_pkl == '':

            self.peak_group_pkl = ''
            self.wizard = GoWizard()
            self.wizard._signal.connect(self.get_parm)
            self.wizard.show()
        else:
            self.total_result_pkl = ''
            self.peak_group_pkl = ''
            self.input_file = self.all_pkl[0][6]
            self.wizard = GoWizard()
            self.wizard._signal.connect(self.get_parm)
            self.wizard.show()

    def get_parm(self, parm):
        # parm["group_peak_factor"] = 1
        self.parm_list = list(parm.values())

        self.parm_list.insert(0, self.input_file)
        self.parm_list = [self.total_result_pkl, self.peak_group_pkl] + self.parm_list
        # print(self.parm_list)
        # print(len(self.parm_list))
        self.run()

    def all_df_accept(self, all):
        self.all_pkl = pickle.loads(all)
        df = self.all_pkl[0][4]
        df["ion_num"] = df["ions"].apply(lambda x: len(x))
        self.peak_group_df = df
        self.qualitative_and_quantitative_analysis_result = self.all_pkl[1]
        self.smooth_df = self.all_pkl[0][0]
        self.choose_ion_df = self.all_pkl[0][5]
        self.choose_ion_df["Peak_group"] = np.round(self.choose_ion_df["Peak_group"].astype(np.float64), decimals=2)
        # print("peak_group_df:  ", self.peak_group_df)
        # print("qualitative_and_quantitative_analysis_result:  ", self.qualitative_and_quantitative_analysis_result)
        # print("smooth_df:  ", self.smooth_df)

        if isinstance(self.input_file, pd.DataFrame) == False:
            if self.input_file != '':
                dir = os.path.dirname(self.input_file)
                now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

                with open(dir + '/total_result_' + now + '.pkl', "wb") as f:
                    pickle.dump(self.all_pkl, f)

                # with open(dir + '/peak_group_' + now + '.pkl', "wb") as f:
                #     pickle.dump(self.all_pkl[0], f)
                #
                # with open(dir + '/qualitative_and_quantitative_analysis_result_' + now + '.pkl', "wb") as f:
                #     pickle.dump(self.qualitative_and_quantitative_analysis_result, f)

            else:
                dir = os.path.dirname(self.total_result_pkl)
                now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                with open(dir + '/total_result_' + now + '.pkl', "wb") as f:
                    pickle.dump(self.all_pkl, f)

    def chooseRTinfo(self, text):
        self.choose = text
        # print("*************************peak_group_df:  ", self.peak_group_df)

        try:
            self.add_group_peak_table(self.peak_group_df, self.qualitative_and_quantitative_analysis_result,
                                      self.choose,
                                      self.show_qualitative, self.ion_num)
        except:
            pass

    def check_qualitative_group(self, bool):

        self.show_qualitative = bool
        try:
            self.add_group_peak_table(self.peak_group_df, self.qualitative_and_quantitative_analysis_result,
                                      self.choose,
                                      self.show_qualitative, self.ion_num)
        except:
            pass

    def min_ion_num(self, value):

        self.ion_num = value
        try:
            self.add_group_peak_table(self.peak_group_df, self.qualitative_and_quantitative_analysis_result,
                                      self.choose,
                                      self.show_qualitative, self.ion_num)
        except:
            pass

    def run(self):
        self.progressBar.show()
        self.progress_value = 0
        self.timer.start(100)
        self.worker_thread = WorkerThread(*self.parm_list)


        self.worker_thread.all_df_signal.connect(self.all_df_accept)

        self.worker_thread.finished.connect(self.hide_progress_bar)

        self.worker_thread.start()

    def update_progress_bar(self):
        self.progress_value += 1
        if self.progress_value == 101:
            self.progress_value = 0
        else:
            self.progressBar.setValue(self.progress_value)

    def hide_progress_bar(self, run_stat):
        self.progressBar.hide()
        self.timer.stop()
        if run_stat == 0:
            self.add_group_peak_table(self.peak_group_df, self.qualitative_and_quantitative_analysis_result,
                                      self.choose,
                                      self.show_qualitative, self.ion_num)
            self.menuRe_analysis.setEnabled(True)
            QMessageBox.information(self, 'Success', 'Run successfully!')
        elif run_stat == 1:
            QMessageBox.critical(self, 'Error', 'Run Failed!')

    def export_msp(self, item):
        tmp = self.peak_group_df.copy()
        if self.choose == "min":


            tmp["rt"] = np.round(tmp["rt"].astype(np.float64), decimals=2).to_list()
            idx = tmp[np.round(tmp.rt.astype(np.float64) / 60, decimals=2) == round(
                float(self.choose_peak_group), 2)].index.item()
            del tmp
        else:
            tmp["rt"] = np.round(tmp["rt"].astype(np.float64), decimals=2).to_list()
            idx = tmp[
                np.around(tmp.rt, decimals=2) == round(float(self.choose_peak_group), 2)].index.item()

        msp_df = self.peak_group_df.ions.values[idx]

        _out1 = QFileDialog.getExistingDirectory(None, "Select Output File Path", './')
        with open(_out1 + "/Group_" + str(self.choose_peak_group) + ".msp", 'w') as file:
            file.write(f"Name: Group_{self.choose_peak_group}\n")
            file.write(f"Num peaks: {msp_df.shape[0]}\n")
            msp_df.to_csv(file, sep=' ', index=True, header=False, line_terminator='\n')



    def save(self):
        _out = QFileDialog.getExistingDirectory(None, "Select Output File Path", './')

        _out_qualitative_and_quantitative_analysis_result = self.qualitative_and_quantitative_analysis_result[
            ["Best_match_name", "All_match_list", "Quant_Ion", "Relative_Peak_Area", "Peak_Height"]]
        for index, row in _out_qualitative_and_quantitative_analysis_result.iterrows():
            _out_qualitative_and_quantitative_analysis_result.at[index, 'All_match_list'] = str(
                row['All_match_list']).strip('[[[').strip(']]]')

        _out_qualitative_and_quantitative_analysis_result.to_csv(
            _out + '/qualitative_and_quantitative_analysis_result.csv', index_label='RT')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    apply_stylesheet(app, theme='light_cyan_500.xml', invert_secondary=True)
    myWin.show()
    sys.exit(app.exec_())
