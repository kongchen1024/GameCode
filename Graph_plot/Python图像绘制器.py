import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
from typing import Dict
import pandas as pd
from tkinter import filedialog, colorchooser, ttk
from PIL import ImageTk, Image
import tkinter.font as tkFont
from matplotlib import pyplot as plt
from ttkthemes import ThemedStyle

global_data = pd.DataFrame()  # 创建全局变量 data
global_sheet_names = []  # 创建全局变量 data_excel
file_path = ""  # 导入文件地址
columns_choice = []  # 选择研究指标列
data_shape = []  # 定义data数据形状
bar_dict = {}  # 定义柱状图字典
pie_dict = {}  # 定义饼状图字典
temp = 0

class WinGUI(Tk):
    widget_dic: Dict[str, Widget] = {}

    """"
             初始化模块
    """

    def __init__(self):
        super().__init__()
        self.__win()
        self.widget_dic["tk_frame_left"] = self.__tk_frame_left(self)
        self.widget_dic["tk_tabs_left"] = self.__tk_tabs_left(self.widget_dic["tk_frame_left"])
        self.widget_dic["tk_table_data"] = self.__tk_table_data(self.widget_dic["tk_tabs_left_0"])
        self.widget_dic["tk_label_image"] = self.__tk_label_image(self.widget_dic["tk_tabs_left_1"])
        self.widget_dic["tk_button_import"] = self.__tk_button_import(self)
        self.widget_dic["tk_text_receive_console"] = self.__tk_text_receive_console(self)
        self.widget_dic["tk_input_input"] = self.__tk_input_input(self)
        self.widget_dic["tk_label_send"] = self.__tk_label_send(self)
        self.widget_dic["tk_button_console_send"] = self.__tk_button_console_send(self)
        self.widget_dic["tk_button_console_clear"] = self.__tk_button_console_clear(self)
        self.widget_dic["tk_label_receive"] = self.__tk_label_receive(self)
        self.widget_dic["tk_select_box_choice_indicator"] = self.__tk_select_box_choice_indicator(self)
        self.widget_dic["tk_button_indicator_add"] = self.__tk_button_indicator_add(self)
        self.widget_dic["tk_button_indicator_delete"] = self.__tk_button_indicator_delete(self)
        self.widget_dic["tk_select_box_excel"] = self.__tk_select_box_excel(self)
        self.widget_dic["tk_radio_button_data_transposition"] = self.__tk_radio_button_data_transposition(self)
        self.widget_dic["tk_tabs_right"] = self.__tk_tabs_right(self)
        self.widget_dic["tk_frame_draw_image"] = self.__tk_frame_draw_image(self.widget_dic["tk_tabs_right_1"])
        self.widget_dic["tk_tabs_draw_image"] = self.__tk_tabs_draw_image(self.widget_dic["tk_frame_draw_image"])
        self.widget_dic["tk_label_bar_x_label"] = self.__tk_label_bar_x_label(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_label_bar_y_label"] = self.__tk_label_bar_y_label(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_label_bar_notice"] = self.__tk_label_bar_notice(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_label_bar_title"] = self.__tk_label_bar_title(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_scale_bar_x_fontsize"] = self.__tk_scale_bar_x_fontsize(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_input_bar_title"] = self.__tk_input_bar_title(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_input_bar_x_label"] = self.__tk_input_bar_x_label(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_select_box_bar_title_weight"] = self.__tk_select_box_bar_title_weight(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_select_box_bar_title_fontstyle"] = self.__tk_select_box_bar_title_fontstyle(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_select_box_bar_title_fontname"] = self.__tk_select_box_bar_title_fontname(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_button_bar_title_color"] = self.__tk_button_bar_title_color(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_input_bar_y_label"] = self.__tk_input_bar_y_label(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_scale_bar_y_fontsize"] = self.__tk_scale_bar_y_fontsize(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_select_box_bar_label_fontweight"] = self.__tk_select_box_bar_label_weight(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_select_box_bar_label_fontstyle"] = self.__tk_select_box_bar_label_fontstyle(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_select_box_bar_label_fontname"] = self.__tk_select_box_bar_label_fontname(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_button_bar_label_color"] = self.__tk_button_bar_label_color(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_label_bar_x"] = self.__tk_label_bar_x(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_input_bar_x"] = self.__tk_input_bar_x(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_label_bar_height"] = self.__tk_label_bar_height(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_input_bar_height"] = self.__tk_input_bar_height(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_label_bar_bottom"] = self.__tk_label_bar_bottom(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_input_bar_bottom"] = self.__tk_input_bar_bottom(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_select_box_align"] = self.__tk_select_box_align(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_button_bar_color"] = self.__tk_button_bar_color(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_button_bar_edgecolor"] = self.__tk_button_bar_edgecolor(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_scale_bar_arfa"] = self.__tk_scale_bar_arfa(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_label_bar_label"] = self.__tk_label_bar_label(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_input_bar_label"] = self.__tk_input_bar_label(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_button_out_image"] = self.__tk_button_out_image(self.widget_dic["tk_tabs_draw_image_bar"],
                                                                            'bar')
        self.widget_dic["tk_label_bar_width"] = self.__tk_label_bar_width(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_input_bar_width"] = self.__tk_input_bar_width(self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_scale_bar_title_size"] = self.__tk_scale_bar_title_size(
            self.widget_dic["tk_tabs_draw_image_bar"])
        self.widget_dic["tk_label_pie_title"] = self.__tk_label_pie_title(self.widget_dic["tk_tabs_draw_image_pie"])
        self.widget_dic["tk_input_pie_title"] = self.__tk_input_pie_title(self.widget_dic["tk_tabs_draw_image_pie"])
        self.widget_dic["tk_scale_pie_title_size"] = self.__tk_scale_pie_title_size(
            self.widget_dic["tk_tabs_draw_image_pie"])
        self.widget_dic["tk_select_box_pie_title_weight"] = self.__tk_select_box_pie_title_weight(
            self.widget_dic["tk_tabs_draw_image_pie"])
        self.widget_dic["tk_select_box_pie_title_fontstyle"] = self.__tk_select_box_pie_title_fontstyle(
            self.widget_dic["tk_tabs_draw_image_pie"])
        self.widget_dic["tk_select_box_pie_title_fontname"] = self.__tk_select_box_pie_title_fontname(
            self.widget_dic["tk_tabs_draw_image_pie"])
        self.widget_dic["tk_button_pie_title_color"] = self.__tk_button_pie_title_color(
            self.widget_dic["tk_tabs_draw_image_pie"])
        self.widget_dic["tk_button_out_image"] = self.__tk_button_out_image(self.widget_dic["tk_tabs_draw_image_pie"],
                                                                            'pie')
        self.__event_bind()

    "----------------------------------------------------------------------"
    """
             窗口
    """

    def __win(self):
        self.title("Python 数据分析工具箱")
        # 设置窗口大小、居中
        width = 1200
        height = 800
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        # 自动隐藏滚动条

    def scrollbar_autohide(self, bar, widget):
        self.__scrollbar_hide(bar, widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar, widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar, widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar, widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar, widget))

    def __scrollbar_show(self, bar, widget):
        bar.lift(widget)

    def __scrollbar_hide(self, bar, widget):
        bar.lower(widget)

    def vbar(self, ele, x, y, w, h, parent):
        sw = 20  # Scrollbar 宽度
        x = x + w - sw
        vbar = Scrollbar(parent, orient="vertical")
        ele.configure(yscrollcommand=vbar.set)
        vbar.config(command=ele.yview)
        vbar.place(x=x, y=y, width=sw, height=h)
        self.scrollbar_autohide(vbar, ele)

    def hbar(self, ele, x, y, w, h, parent):
        sh = 15  # Scrollbar 宽度
        y = y + h - sh
        hbar = Scrollbar(parent, orient="horizontal")
        ele.configure(xscrollcommand=hbar.set)
        hbar.config(command=ele.xview)
        hbar.place(x=x, y=y, width=w, height=sh)
        self.scrollbar_autohide(hbar, ele)

    "----------------------------------------------------------------------"
    """
             左侧菜单
    """

    """
             左侧容器    
    """

    def __tk_frame_left(self, parent):
        frame = Frame(parent, )
        frame.place(x=10, y=10, width=732, height=782)
        return frame

    """
             左侧选项卡
    """

    def __tk_tabs_left(self, parent):
        frame = Notebook(parent)
        self.widget_dic["tk_tabs_left_0"] = self.__tk_frame_left_0(frame)
        frame.add(self.widget_dic["tk_tabs_left_0"], text="数据")
        self.widget_dic["tk_tabs_left_1"] = self.__tk_frame_left_1(frame)
        frame.add(self.widget_dic["tk_tabs_left_1"], text="图像")
        frame.place(x=10, y=10, width=713, height=636)
        return frame

    def __tk_frame_left_0(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=713, height=636)
        return frame

    def __tk_frame_left_1(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=713, height=636)
        return frame

    """
             左侧数据表格
    """

    def __tk_table_data(self, parent):
        # 设置一个主题
        style = ThemedStyle(parent) #倾向于clearlooks,itft1,plastik,ubuntu
        # "adapta","aquativo","arc","black","blue","breeze","clearlooks",
        # "elegance","equilux","itft1","keramik","kroc","plastik","radiance",
        # "scidblue","scidgreen","scidgrey","scidmint","scidpink","scidpurple",
        # "scidsand","smog","ubuntu","winxpblue","yaru",
        style.set_theme("plastik")
        # 表头字段 表头宽度
        if len(columns_choice) >= 5:
            columns = {column: 142 for column in columns_choice}
        else:
            columns = {column: 710 // len(columns_choice) for column in columns_choice}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns))
        for text, width in columns.items():
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)
        tk_table.place(x=0, y=0, width=711, height=608)
        self.vbar(tk_table, 0, 0, 711, 608, parent)
        self.hbar(tk_table, 0, 0, 711, 608, parent)
        return tk_table

    """
             左侧图像
    """

    def __tk_label_image(self, parent):
        label = Label(parent, text="", anchor="center", )
        label.place(x=10, y=20, width=696, height=582)
        return label

    """
             左侧控制台模块
    """

    def __tk_text_receive_console(self, parent):
        text = Text(parent)
        text.place(x=120, y=660, width=539, height=95)
        self.vbar(text, 120, 660, 539, 95, parent)
        self.hbar(text, 120, 660, 539, 95, parent)
        return text

    def __tk_input_input(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=120, y=760, width=538, height=32)
        return ipt

    def __tk_label_send(self, parent):
        label = Label(parent, text="输入指令至控制台：", anchor="center", )
        label.place(x=10, y=760, width=107, height=30)
        return label

    def __tk_button_console_send(self, parent):
        btn = Button(parent, text="发送", takefocus=False, )
        btn.place(x=680, y=760, width=62, height=30)
        return btn

    def __tk_button_console_clear(self, parent):
        btn = Button(parent, text="清空", takefocus=False, )
        btn.place(x=680, y=720, width=62, height=30)
        return btn

    def __tk_label_receive(self, parent):
        label = Label(parent, text="控制台信息：", anchor="center", )
        label.place(x=10, y=690, width=111, height=30)
        return label

    "----------------------------------------------------------------------"
    """
             右侧数据导入模块
    """

    def __tk_button_import(self, parent):
        btn = Button(parent, text="导入数据", takefocus=False, )
        btn.place(x=760, y=10, width=86, height=35)
        return btn

    def __tk_select_box_excel(self, parent):
        cb = Combobox(parent, state="readonly", )
        if global_sheet_names:
            cb['values'] = list(sheet_name for sheet_name in global_sheet_names)
            cb.current(0)
            cb.bind('<<ComboboxSelected>>', self.select_excel)
        else:
            cb['values'] = ("选择子表")
            cb.set(cb['values'][0])
        cb.place(x=870, y=10, width=155, height=38)
        self.widget_dic["tk_button_indicator_add"].bind('<Button-1>', self.indicator_add)
        self.widget_dic["tk_button_indicator_delete"].bind('<Button-1>', self.indicator_delete)
        return cb

    def __tk_radio_button_data_transposition(self, parent):
        rb = Radiobutton(parent, text="转置", )
        rb.place(x=1050, y=10, width=118, height=37)
        return rb

    def __tk_select_box_choice_indicator(self, parent):
        cb = Combobox(parent, state="readonly", )
        if len(cb['values']) != 0:
            cb.set(cb['values'][0])  # 默认显示第一个
        if global_data.size != 0:
            cb['values'] = list(column for column in global_data.columns.values)
            cb.current(0)
        cb.place(x=870, y=70, width=151, height=30)
        return cb

    def __tk_button_indicator_add(self, parent):
        btn = Button(parent, text="添加指标", takefocus=False, )
        btn.place(x=760, y=70, width=86, height=30)
        return btn

    def __tk_button_indicator_delete(self, parent):
        btn = Button(parent, text="删除", takefocus=False, )
        btn.place(x=1050, y=70, width=118, height=27)
        return btn

    "----------------------------------------------------------------------"
    """
             右侧选项卡
    """

    def __tk_tabs_right(self, parent):
        frame = Notebook(parent)
        self.widget_dic["tk_tabs_right_0"] = self.__tk_frame_right_0(frame)
        frame.add(self.widget_dic["tk_tabs_right_0"], text="数据处理")
        self.widget_dic["tk_tabs_right_1"] = self.__tk_frame_right_1(frame)
        frame.add(self.widget_dic["tk_tabs_right_1"], text="图像绘制")
        self.widget_dic["tk_tabs_right_2"] = self.__tk_frame_right_2(frame)
        frame.add(self.widget_dic["tk_tabs_right_2"], text="分类模型")
        self.widget_dic["tk_tabs_right_3"] = self.__tk_frame_right_3(frame)
        frame.add(self.widget_dic["tk_tabs_right_3"], text="预测模型")
        frame.place(x=760, y=130, width=430, height=646)
        frame.select(1)  # 默认进行图像绘制
        return frame

    def __tk_frame_right_0(self, parent):
        frame = Frame(parent)
        frame.place(x=760, y=130, width=430, height=646)
        return frame

    def __tk_frame_right_1(self, parent):
        frame = Frame(parent)
        frame.place(x=760, y=130, width=430, height=646)
        return frame

    def __tk_frame_right_2(self, parent):
        frame = Frame(parent)
        frame.place(x=760, y=130, width=430, height=646)
        return frame

    def __tk_frame_right_3(self, parent):
        frame = Frame(parent)
        frame.place(x=760, y=130, width=430, height=646)
        return frame

    "----------------------------------------------------------------------"
    """
             图像绘制模块
    """

    def __tk_frame_draw_image(self, parent):
        frame = Frame(parent, )
        frame.place(x=10, y=10, width=410, height=605)
        return frame

    def __tk_tabs_draw_image(self, parent):
        frame = Notebook(parent)
        self.widget_dic["tk_tabs_draw_image_bar"] = self.__tk_frame_draw_image_bar(frame)
        frame.add(self.widget_dic["tk_tabs_draw_image_bar"], text="柱状图")
        self.widget_dic["tk_tabs_draw_image_pie"] = self.__tk_frame_draw_image_pie(frame)
        frame.add(self.widget_dic["tk_tabs_draw_image_pie"], text="饼状图")
        self.widget_dic["tk_tabs_draw_image_2"] = self.__tk_frame_draw_image_2(frame)
        frame.add(self.widget_dic["tk_tabs_draw_image_2"], text="热力图")
        self.widget_dic["tk_tabs_draw_image_3"] = self.__tk_frame_draw_image_3(frame)
        frame.add(self.widget_dic["tk_tabs_draw_image_3"], text="频数图")
        self.widget_dic["tk_tabs_draw_image_4"] = self.__tk_frame_draw_image_4(frame)
        frame.add(self.widget_dic["tk_tabs_draw_image_4"], text="箱线图")
        self.widget_dic["tk_tabs_draw_image_5"] = self.__tk_frame_draw_image_5(frame)
        frame.add(self.widget_dic["tk_tabs_draw_image_5"], text="散点图")
        frame.place(x=10, y=10, width=391, height=577)
        frame.select(1)  # 默认绘制饼状图
        return frame

    def __tk_frame_draw_image_bar(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=391, height=577)
        return frame

    def __tk_frame_draw_image_pie(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=391, height=577)
        return frame

    def __tk_frame_draw_image_2(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=391, height=577)
        return frame

    def __tk_frame_draw_image_3(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=391, height=577)
        return frame

    def __tk_frame_draw_image_4(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=391, height=577)
        return frame

    def __tk_frame_draw_image_5(self, parent):
        frame = Frame(parent)
        frame.place(x=10, y=10, width=391, height=577)
        return frame

    """
             柱状图
    """

    def __tk_label_bar_x_label(self, parent):
        label = Label(parent, text="X轴标签：", anchor="center", )
        label.place(x=0, y=100, width=64, height=30)
        return label

    def __tk_label_bar_y_label(self, parent):
        label = Label(parent, text="Y轴标签：", anchor="center", )
        label.place(x=0, y=140, width=64, height=30)
        return label

    def __tk_label_bar_notice(self, parent):
        label = Label(parent, text="柱形参数：不输入采取默认选择", anchor="center", )
        label.place(x=0, y=240, width=184, height=30)
        return label

    def __tk_label_bar_title(self, parent):
        label = Label(parent, text="标题：", anchor="center", )
        label.place(x=0, y=10, width=50, height=30)
        return label

    def __tk_scale_bar_x_fontsize(self, parent):
        scale = Scale(parent, orient=HORIZONTAL,from_=8, to=18)
        scale.set(12)
        scale.place(x=250, y=100, width=101, height=30)
        scale.bind("<ButtonRelease-1>", lambda event: self.on_slider_release(scale, ['x_label', 'size'],'bar'))
        return scale

    def on_entry_click(self, entry, default_text):
        if entry.get() == default_text:
            entry.delete(0, tk.END)
            entry.configure(foreground='black')

    def check_input(self, entry, path, default_text,image_type=''):
        global bar_dict,pie_dict
        # 监测柱状图输入情况
        input_text = entry.get()
        if input_text != "":
            length = len(path)
            if image_type == 'bar':
                cur = bar_dict
            elif image_type == 'pie':
                cur = pie_dict
            while length > 1:
                cur = cur[path[-length]]
                length -= 1
            cur[path[-1]] = input_text  # 更新柱状图参数字典
            if image_type == 'bar':
                self.draw_bar(self)  # 绘制柱状图
            elif image_type == 'pie':
                self.draw_pie(self)  # 绘制饼状图
        else:
            entry.insert(0, default_text)
            entry.configure(foreground='grey')

    def __tk_input_bar_title(self, parent):
        entry = Entry(parent)
        default_text = "柱状图"
        entry.insert(0, default_text)
        entry.bind('<FocusIn>', lambda e: self.on_entry_click(entry, default_text))
        entry.bind('<FocusOut>', lambda e: self.check_input(entry, path=['title', 'input'], default_text=default_text,image_type='bar'))
        entry.place(x=50, y=10, width=195, height=30)
        return entry

    def __tk_input_bar_x_label(self, parent):
        entry = Entry(parent)
        default_text = "X轴标签"
        global global_data, columns_choice
        if not global_data.empty:
            if global_data[columns_choice].shape[1] != 2:
                tkinter.messagebox.showerror("绘制柱状图的列数应为2")
                return
            else:
                default_text = global_data[columns_choice].columns[0]
        entry.insert(0, default_text)
        entry.bind('<FocusIn>', lambda e: self.on_entry_click(entry, default_text))
        entry.bind('<FocusOut>',
                   lambda e: self.check_input(entry, path=['x_label', 'input'], default_text=default_text,image_type='bar'))
        entry.place(x=60, y=100, width=186, height=30)
        return entry

    def on_select_box_click(self, cb, default_selection):
        if cb.get() == default_selection:
            cb.delete(0, tk.END)
            cb.configure(foreground='black')

    def check_selection(self, cb, path,image_type=''):
        global bar_dict,pie_dict
        selection = cb.get()
        weight_dir = {"正常": "normal", "粗体": "bold", "细体": "light"}
        style_dir={"正常":"normal","斜体":"italic","倾斜":'italic'}
        name_dir={'Arial':'Arial','仿宋':'Fangsong'}
        length = len(path)
        if image_type == 'bar':
            cur = bar_dict
        elif image_type == 'pie':
            cur = pie_dict
        while length > 1:
            cur = cur[path[-length]]
            length -= 1
        if "weight" in path or 'fontweight' in path:
            cur[path[-1]] = weight_dir[selection]  # 更新柱状图参数字典
        elif 'fontstyle' in path:
            cur[path[-1]] = style_dir[selection]
        else:
            cur[path[-1]] = name_dir[selection]
        if image_type == 'bar':
            self.draw_bar(self)  # 绘制柱状图
        elif image_type == 'pie':
            self.draw_pie(self)  # 绘制饼状图

    def __tk_select_box_bar_title_weight(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("正常", "粗体", "细体")
        default_selection = '正常'
        cb.set('粗细')
        cb.bind('<<ComboboxSelected>>', lambda e: self.on_select_box_click(cb, default_selection))
        cb.bind('<FocusIn>', lambda e: self.check_selection(cb, ['title', 'weight'],'bar'))
        cb.place(x=0, y=60, width=68, height=30)
        return cb

    def __tk_select_box_bar_title_fontstyle(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("正常", "斜体", "倾斜")
        default_selection = '正常'
        cb.set('样式')
        cb.bind('<<ComboboxSelected>>', lambda e: self.on_select_box_click(cb, default_selection))
        cb.bind('<FocusIn>', lambda e: self.check_selection(cb, ['title', 'fontstyle'],'bar'))
        cb.place(x=90, y=60, width=68, height=30)
        return cb

    def __tk_select_box_bar_title_fontname(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("Arial", "仿宋")
        default_selection = '仿宋'
        cb.set('字体')
        cb.bind('<<ComboboxSelected>>', lambda e: self.on_select_box_click(cb, default_selection))
        cb.bind('<FocusIn>', lambda e: self.check_selection(cb, ['title', 'fontname'],'bar'))
        cb.place(x=170, y=60, width=68, height=30)
        return cb

    def select_color(self,path,image_type=''):
        color = colorchooser.askcolor()
        global bar_dict,pie_dict
        if color[1]:
            length = len(path)
            if image_type == 'bar':
                cur = bar_dict
            else:
                cur = pie_dict
            while length > 1:
                cur = cur[path[-length]]
                length -= 1
            cur[path[-1]]=color[1]
        if image_type =='bar':
            self.draw_bar(self)
        else:
            self.draw_pie(self)

    def __tk_button_bar_title_color(self, parent):
        btn = Button(parent, text="颜色", takefocus=False, )
        btn.bind('<Button-1>',lambda e:self.select_color(['title','color'],'bar'))
        btn.place(x=260, y=60, width=86, height=30)
        return btn

    def __tk_input_bar_y_label(self, parent):
        entry = Entry(parent)
        default_text = "Y轴标签"
        entry.insert(0, default_text)
        entry.bind('<FocusIn>', lambda e: self.on_entry_click(entry, default_text))
        entry.bind('<FocusOut>',
                   lambda e: self.check_input(entry, path=['y_label', 'input'], default_text=default_text,image_type='bar'))
        entry.place(x=60, y=140, width=186, height=30)
        return entry

    def __tk_scale_bar_y_fontsize(self, parent):
        scale = Scale(parent, orient=HORIZONTAL,from_=8, to=18)
        scale.set(12)
        scale.place(x=250, y=140, width=101, height=30)
        scale.bind("<ButtonRelease-1>", lambda event: self.on_slider_release(scale, ['y_label', 'size'],'bar'))
        return scale

    def __tk_select_box_bar_label_weight(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("正常", "粗体", "细体")
        default_selection = '正常'
        cb.set('粗细')
        cb.bind('<<ComboboxSelected>>', lambda e: self.on_select_box_click(cb, default_selection))
        cb.bind('<FocusIn>', lambda e: self.check_selection(cb, ['label', 'frontweight'],'bar'))
        cb.place(x=0, y=190, width=68, height=30)
        return cb

    def __tk_select_box_bar_label_fontstyle(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("正常", "斜体", "倾斜")
        default_selection = '正常'
        cb.set('样式')
        cb.bind('<<ComboboxSelected>>', lambda e: self.on_select_box_click(cb, default_selection))
        cb.bind('<FocusIn>', lambda e: self.check_selection(cb, ['label', 'fontstyle'],'bar'))
        cb.place(x=90, y=190, width=68, height=30)
        return cb

    def __tk_select_box_bar_label_fontname(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("Arial", "仿宋")
        default_selection = '仿宋'
        cb.set('字体')
        cb.bind('<<ComboboxSelected>>', lambda e: self.on_select_box_click(cb, default_selection))
        cb.bind('<FocusIn>', lambda e: self.check_selection(cb, ['label', 'fontname'],'bar'))
        cb.place(x=170, y=190, width=68, height=30)
        return cb

    def __tk_button_bar_label_color(self, parent):
        btn = Button(parent, text="颜色", takefocus=False, )
        btn.bind('<Button-1>', lambda e: self.select_color(['label', 'color'],'bar'))
        btn.place(x=260, y=190, width=86, height=30)
        return btn

    def __tk_label_bar_x(self, parent):
        label = Label(parent, text="位置：", anchor="center", )
        label.place(x=0, y=290, width=50, height=30)
        return label

    def __tk_input_bar_x(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=50, y=290, width=299, height=30)
        return ipt

    def __tk_label_bar_height(self, parent):
        label = Label(parent, text="高度：", anchor="center", )
        label.place(x=0, y=340, width=50, height=30)
        return label

    def __tk_input_bar_height(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=50, y=340, width=299, height=30)
        return ipt

    def __tk_label_bar_bottom(self, parent):
        label = Label(parent, text="底高：", anchor="center", )
        label.place(x=0, y=420, width=50, height=30)
        return label

    def __tk_input_bar_bottom(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=50, y=420, width=299, height=30)
        return ipt

    def __tk_select_box_align(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("对齐", "Python", "Tkinter Helper")
        cb.place(x=0, y=470, width=68, height=30)
        return cb

    def __tk_button_bar_color(self, parent):
        btn = Button(parent, text="颜色", takefocus=False, )
        btn.bind('<Button-1>', lambda e: self.select_color(['bar', 'color'],'bar'))
        btn.place(x=80, y=470, width=86, height=30)
        return btn

    def __tk_button_bar_edgecolor(self, parent):
        btn = Button(parent, text="边框颜色", takefocus=False, )
        btn.bind('<Button-1>', lambda e: self.select_color(['edge', 'color'],'bar'))
        btn.place(x=180, y=470, width=86, height=30)
        return btn

    def __tk_scale_bar_arfa(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=280, y=470, width=101, height=30)
        return scale

    def __tk_label_bar_label(self, parent):
        label = Label(parent, text="柱标签：", anchor="center", )
        label.place(x=0, y=520, width=64, height=30)
        return label

    def __tk_input_bar_label(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=60, y=520, width=186, height=30)
        return ipt

    def __tk_button_out_image(self, parent,image_type=''):
        btn = Button(parent, text="导出图片", takefocus=False, )
        btn.place(x=280, y=520, width=92, height=30)
        if image_type == 'bar':
            btn.bind("<Button-1>", self.draw_bar)
        else:
            btn.bind('<Button-1>', self.draw_pie)
        return btn

    def __tk_label_bar_width(self, parent):
        label = Label(parent, text="宽度：", anchor="center", )
        label.place(x=0, y=380, width=50, height=30)
        return label

    def __tk_input_bar_width(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=50, y=380, width=299, height=30)
        return ipt

    def on_slider_release(self,scale,path,image_type=''):
        global bar_dict,pie_dict
        length = len(path)
        if image_type == 'bar':
            cur = bar_dict
        else:
            cur = pie_dict
        while length > 1:
            cur = cur[path[-length]]
            length -= 1
        cur[path[-1]] = scale.get()  # 更新柱状图参数字典
        if image_type == 'bar':
            self.draw_bar(self)  # 绘制柱状图
        else:
            self.draw_pie(self)  # 绘制饼图

    def __tk_scale_bar_title_size(self, parent):
        scale = Scale(parent, orient=HORIZONTAL,from_=10, to=20)
        scale.set(14)
        scale.place(x=250, y=10, width=101, height=30)
        scale.bind("<ButtonRelease-1>", lambda event: self.on_slider_release(scale, ['title', 'size'],'bar'))
        return scale

    def __tk_label_pie_title(self, parent):
        label = Label(parent, text="标题：", anchor="center", )
        label.place(x=0, y=10, width=50, height=30)
        return label

    def __tk_scale_pie_title_size(self, parent):
        scale = Scale(parent, orient=HORIZONTAL,from_=10, to=20)
        scale.set(14)
        scale.place(x=250, y=10, width=101, height=30)
        scale.bind("<ButtonRelease-1>", lambda event: self.on_slider_release(scale, ['title', 'size'],'pie'))
        return scale

    def __tk_input_pie_title(self, parent):
        entry = Entry(parent)
        default_text = "饼状图"
        entry.insert(0, default_text)
        entry.bind('<FocusIn>', lambda e: self.on_entry_click(entry, default_text))
        entry.bind('<FocusOut>', lambda e: self.check_input(entry, path=['title', 'input'], default_text=default_text,image_type='pie'))
        entry.place(x=50, y=10, width=195, height=30)
        return entry

    def __tk_select_box_pie_title_weight(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("正常", "粗体", "细体")
        default_selection = '正常'
        cb.set('粗细')
        cb.bind('<<ComboboxSelected>>', lambda e: self.on_select_box_click(cb, default_selection))
        cb.bind('<FocusIn>', lambda e: self.check_selection(cb, ['title', 'weight'],'pie'))
        cb.place(x=0, y=60, width=68, height=30)
        return cb

    def __tk_select_box_pie_title_fontstyle(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("正常", "斜体", "倾斜")
        default_selection = '正常'
        cb.set('样式')
        cb.bind('<<ComboboxSelected>>', lambda e: self.on_select_box_click(cb, default_selection))
        cb.bind('<FocusIn>', lambda e: self.check_selection(cb, ['title', 'fontstyle'],'pie'))
        cb.place(x=90, y=60, width=68, height=30)
        return cb

    def __tk_select_box_pie_title_fontname(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("Arial", "仿宋")
        default_selection = '仿宋'
        cb.set('字体')
        cb.bind('<<ComboboxSelected>>', lambda e: self.on_select_box_click(cb, default_selection))
        cb.bind('<FocusIn>', lambda e: self.check_selection(cb, ['title', 'fontname'],'pie'))
        cb.place(x=170, y=60, width=68, height=30)
        return cb

    def __tk_button_pie_title_color(self, parent):
        btn = Button(parent, text="颜色", takefocus=False, )
        btn.bind('<Button-1>',lambda e:self.select_color(['title','color'],'pie'))
        btn.place(x=260, y=60, width=86, height=30)
        return btn

    "----------------------------------------------------------------------"
    """
             事件绑定
    """

    def __event_bind(self):
        self.widget_dic["tk_button_import"].bind('<Button-1>', self.import_data)
        self.widget_dic["tk_radio_button_data_transposition"].bind("<Button-1>", self.data_transposition)
        pass

    "----------------------------------------------------------------------"
    """
             处理事件
    """
    """
             导入数据
    """

    def import_data(self, evt):
        # 弹出文件选择对话框
        global file_path
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
        if file_path:
            global global_sheet_names
            global_sheet_names = pd.ExcelFile(file_path).sheet_names
            # 更新子表下拉列表
            self.widget_dic["tk_select_box_excel"] = self.__tk_select_box_excel(self)
        pass

    def insert_data(self):
        global global_data, columns_choice
        # Create a font
        fnt = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=fnt)
        # Configuring tags for row colors
        self.widget_dic["tk_table_data"].tag_configure('oddrow', background='white')
        self.widget_dic["tk_table_data"].tag_configure('evenrow', background='#C0C0C0')
        # 插入新的数据
        for index, row in global_data[columns_choice].iterrows():
            temp=index
            if index % 2 == 0:
                self.widget_dic["tk_table_data"].insert('', 'end', values=list(global_data[columns_choice].iloc[index,:].values),
                                                        tags=('evenrow',))
            else:
                self.widget_dic["tk_table_data"].insert('', 'end', values=list(global_data[columns_choice].iloc[index,:].values),
                                                        tags=('oddrow',))

    def select_excel(self, evt):
        # 选择 excel
        if file_path:
            try:
                global global_data, columns_choice, data_shape
                sheet_name = self.widget_dic["tk_select_box_excel"].get()
                global_data = pd.read_excel(file_path, sheet_name=sheet_name)
                if global_data.memory_usage().sum() > 1024 * 1024:
                    tkinter.messagebox.showwarning("警告", "导入数据的内存超过1MB,可能导致运行卡顿")
                # 更新选中的指标，默认是全选
                columns_choice = list(global_data.columns)  # 转 list
                #  更新data形状
                data_shape = global_data.shape
                # 更新表格设置
                self.widget_dic["tk_table_data"] = self.__tk_table_data(self.widget_dic["tk_tabs_left_0"])
                # 清空表格数据
                self.widget_dic["tk_table_data"].delete(*self.widget_dic["tk_table_data"].get_children())
                # 插入数据
                self.insert_data()
                # 更新选取指标的下拉列表
                self.widget_dic["tk_select_box_choice_indicator"] = self.__tk_select_box_choice_indicator(self)
                print("数据导入成功！")
                # 更新柱状图初始化字典
                self.__init__bardir()
                # 更新饼状图初始化字典
                self.__init_piedir()
            except Exception as e:
                print("数据导入失败:", str(e))
        else:
            print("未选择文件！")

    def __init__bardir(self):
        global global_data, columns_choice
        data = global_data[columns_choice]
        global bar_dict  # 初始化柱状图参数的字典
        bar_dict['title'] = {'input': '柱状图', 'size': 14, 'weight': 'normal', 'fontstyle': 'italic',
                             'fontname': 'FangSong', 'color': 'black'}
        bar_dict['x_label'] = {'input': 'X轴标签', 'size': 12}
        bar_dict['y_label'] = {'input': 'Y轴标签', 'size': 12}
        bar_dict['label'] = {'fontweight': 'bold', 'fontstyle': 'italic', 'fontname': 'Fangsong', 'color': 'black'}
        if data.shape[1] >= 2:
            bar_dict['bar'] = {'bar_x': list(data.iloc[:, 0]), 'bar_height': list(data.iloc[:, 1]), 'bar_width': 0.5,
                               'bar_bottom': [0] * len(data.iloc[:, 0]), 'bar_align': 'center', 'bar_color': 'blue',
                               'bar_label': '柱标签', 'bar_arfa': 1.0, 'bar_edgecolor': 'black'}

    def __init_piedir(self):
        global global_data, columns_choice
        data = global_data[columns_choice]
        global pie_dict  # 初始化柱状图参数的字典
        pie_dict['title'] = {'input': '饼状图', 'size': 14, 'weight': 'normal', 'fontstyle': 'italic',
                             'fontname': 'FangSong', 'color': 'black'}
        if data.shape[1] ==2:
            pie_dict['pie']={'sizes': list(data.iloc[:, 1]), 'labels': list(data.iloc[:, 0]),'color': None,
                             'autopct': '%1.1f%%', 'startangle': 90}

    def data_transposition(self, evt):
        global global_data, columns_choice, data_shape
        # 对数据进行转置
        global_data = global_data.T
        if 'index' not in global_data.columns:
            global_data.insert(0, 'index', global_data.index)
        if list(global_data.columns) == list(global_data.head(1)):
            global_data.drop(global_data.index[0])
        columns_choice = list(global_data.columns)
        self.widget_dic["tk_table_data"] = self.__tk_table_data(self.widget_dic["tk_tabs_left_0"])
        self.widget_dic["tk_table_data"].delete(*self.widget_dic["tk_table_data"].get_children())
        for index, row in global_data.iterrows():
            self.widget_dic["tk_table_data"].insert("", "end", values=list(row))
        self.widget_dic["tk_select_box_choice_indicator"] = self.__tk_select_box_choice_indicator(self)

    """
             指标选择
    """

    def indicator_add(self, evt):
        # 选择研究指标
        global columns_choice, global_data
        # 如果表格指标选取满了，直接清空
        if len(columns_choice) == len(global_data.columns):
            self.widget_dic["tk_table_data"].delete(*self.widget_dic["tk_table_data"].get_children())
            columns_choice = []
        column = self.widget_dic["tk_select_box_choice_indicator"].get()
        if column != "":
            if column in columns_choice:
                print("选取的指标已在表格中！")
            else:
                # 维护原表格的columns的顺序
                columns_choice.append(column)
                new_columns_choice = [item for item in columns_choice]
                columns_choice = []
                for column_cur in list(global_data.columns):
                    if column_cur in new_columns_choice:
                        columns_choice.append(column_cur)
                # 更新表格设置
                self.widget_dic["tk_table_data"] = self.__tk_table_data(self.widget_dic["tk_tabs_left_0"])
                # 清空表格数据
                self.widget_dic["tk_table_data"].delete(*self.widget_dic["tk_table_data"].get_children())
                # 插入新的数据
                self.insert_data()

    def indicator_delete(self, evt):
        global columns_choice, global_data
        # 如果表格指标选取满了，直接清空
        column = self.widget_dic["tk_select_box_choice_indicator"].get()
        if column != "":
            if column not in columns_choice:
                print("要删除的指标不在表格中!")
            else:
                columns_choice.remove(column)
                # 更新表格设置
                self.widget_dic["tk_table_data"] = self.__tk_table_data(self.widget_dic["tk_tabs_left_0"])
                # 清空表格数据
                self.widget_dic["tk_table_data"].delete(*self.widget_dic["tk_table_data"].get_children())
                # 插入新的数据
                self.insert_data()

    """
             绘制图像
    """

    def draw_bar(self, evt):
        global global_data, bar_dict,columns_choice
        if global_data[columns_choice].shape[1] > 2:
            print("暂不支持绘制图像!")
            return
        # 创建一个新的图形
        plt.rcParams['font.family'] = 'Fangsong'
        plt.figure(figsize=(5, 4))
        plt.title(bar_dict['title']['input'], fontsize=bar_dict['title']['size'],
                  fontweight=bar_dict['title']['weight'], fontstyle=bar_dict['title']['fontstyle'],
                  fontname=bar_dict['title']['fontname'], color=bar_dict['title']['color'])
        plt.bar(global_data.iloc[:, 0].values, global_data.iloc[:, 1].values, width=bar_dict['bar']['bar_width'],
                bottom=bar_dict['bar']['bar_bottom'], align=bar_dict['bar']['bar_align'],
                color=bar_dict['bar']['bar_color'], label=bar_dict['bar']['bar_label'],
                alpha=bar_dict['bar']['bar_arfa'], edgecolor=bar_dict['bar']['bar_edgecolor'])
        plt.xlabel(bar_dict['x_label']['input'], fontsize=bar_dict['x_label']['size'],
                   fontweight=bar_dict['label']['fontweight'], fontstyle=bar_dict['label']['fontstyle'],
                   fontname=bar_dict['label']['fontname'], color=bar_dict['label']['color'])
        plt.ylabel(bar_dict['y_label']['input'], fontsize=bar_dict['y_label']['size'],
                   fontweight=bar_dict['label']['fontweight'], fontstyle=bar_dict['label']['fontstyle'],
                   fontname=bar_dict['label']['fontname'], color=bar_dict['label']['color'])
        # 保存图形到临时文件
        temp_file = "bar.png"
        plt.savefig(temp_file)
        # 根据比例缩放图像
        image = Image.open(temp_file)
        # 加载临时文件的图像
        image = ImageTk.PhotoImage(image)
        self.widget_dic["tk_label_image"].configure(image=image)
        self.widget_dic["tk_label_image"].image = image
        self.widget_dic["tk_tabs_left"].select(1)

    def draw_pie(self, evt):
        global global_data, pie_dict,columns_choice
        if global_data[columns_choice].shape[1] > 2:
            tkinter.messagebox.showerror("错误", "饼图只支持绘制2维数据")
        # 创建一个新的图形
        plt.rcParams['font.family'] = 'Fangsong'
        plt.figure(figsize=(5, 4))
        plt.title(pie_dict['title']['input'], fontsize=pie_dict['title']['size'],
                  fontweight=pie_dict['title']['weight'], fontstyle=pie_dict['title']['fontstyle'],
                  fontname=pie_dict['title']['fontname'], color=pie_dict['title']['color'])
        plt.pie(x=global_data.iloc[:, 1].values, labels=global_data.iloc[:, 0].values, autopct=pie_dict['pie']['autopct'],
                colors=pie_dict['pie']['color'],startangle=pie_dict['pie']['startangle'],)
        # 保存图形到临时文件
        temp_file = "pie.png"
        plt.savefig(temp_file)
        # 根据比例缩放图像
        image = Image.open(temp_file)
        # 加载临时文件的图像
        image = ImageTk.PhotoImage(image)
        self.widget_dic["tk_label_image"].configure(image=image)
        self.widget_dic["tk_label_image"].image = image
        self.widget_dic["tk_tabs_left"].select(1)


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
