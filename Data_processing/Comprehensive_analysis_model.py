"""This file incorporates a range of common synthetic analysis models"""
import numpy as np
import pandas as pd
from IPython.display import display
import warnings
import tkinter
from tkinter import filedialog
from Data_processing.data_standardization import positive_indicator_processing, negative_indicator_processing

warnings.filterwarnings("ignore")  # 忽略警告
def Ewm(data: pd.DataFrame, positive_columns: list, negative_columns: list):
    """
    States:The function is also named as entropy-weighted,used to get the weights of indicator

    Input: data:pd.DataFrame,positive_columns:list,negative_columns:list.

    Output: None

    Notice:You need do some choices to use the function.
    """
    # process the data
    standardized_data = positive_indicator_processing(data, positive_columns)
    standardized_data = negative_indicator_processing(standardized_data, negative_columns)
    row, column = standardized_data.shape
    entropy = np.zeros(column)  # 信息熵
    weight = np.zeros(column)  # 权重
    d = np.zeros(column)  # 信息信用值
    # calculate the entropy
    for j in range(column):
        p = standardized_data.iloc[:, j] / np.sum(standardized_data.iloc[:, j])
        entropy[j] = -np.sum(p * np.log(p))
        d[j] = 1 - entropy[j]
    # calculate the weight
    for j in range(column):
        weight[j] = (1 - entropy[j]) / np.sum(1 - entropy)
    # 创建Tkinter根窗口
    root = tkinter.Tk()
    root.attributes('-topmost', 1)  # 设置窗口显示在顶层
    root.withdraw()  # 隐藏根窗口
    print("-------------熵权法计算结果-----------")
    calculate_result = pd.DataFrame({"信息熵": entropy, "信息信用值": d, "权重(%)": weight * 100}
                                    , index=standardized_data.columns.values)
    calculate_result.reset_index(drop=True)
    # 输出计算的权重排名结果
    display(calculate_result)  # 输出计算的权重结果
    choice=input("是否导出熵权法权重计算结果? 是（Yes/Y/y）/否（No/N/n）")
    if choice in ["是","Yes","Y","y"]:
        choice_flag = False
        while not choice_flag:
            filetypes = [('Excel文件', '*.xlsx')]
            filepath = filedialog.asksaveasfilename(title="选择保存路径和文件名", filetypes=filetypes, defaultextension='.xlsx')
            if filepath:
                calculate_result.to_excel(filepath)
                print("结果已保存到：", filepath)
                print("导出成功!")
                choice_flag=True
            else:
                print("未选择保存路径,是否继续保存？ 是（Yes/Y/y）/否（No/N/n）")
                choice=input("是否继续保存? 是（Yes/Y/y）/否（No/N/n）")
                if choice not in ["是","Yes","Y","y"]:
                    break
    print("\n-------------熵权法计算排名情况-----------")
    calculate_result_sort = calculate_result.sort_values(by="权重(%)", ascending=False)
    calculate_result_sort['排名'] = ["第" + str(i) + "名" for i in range(1, len(calculate_result_sort) + 1)]
    calculate_result_sort.reset_index(drop=True)
    # 输出计算的权重排名结果
    display(calculate_result_sort)  # 输出计算的权重排名结果
    choice=input("是否导出熵权法计算排名情况? 是（Yes/Y/y）/否（No/N/n）")
    if choice in ["是","Yes","Y","y"]:
        choice_flag = False
        while not choice_flag:
            filetypes = [('Excel文件', '*.xlsx')]
            filepath = filedialog.asksaveasfilename(title="选择保存路径和文件名", filetypes=filetypes, defaultextension='.xlsx')
            if filepath:
                calculate_result.to_excel(filepath)
                print("结果已保存到：", filepath)
                print("导出成功!")
                choice_flag=True
            else:
                print("未选择保存路径,是否继续保存？ 是（Yes/Y/y）/否（No/N/n）")
                choice=input("是否继续保存? 是（Yes/Y/y）/否（No/N/n）")
                if choice not in ["是","Yes","Y","y"]:
                    break
    print("\n-------------熵权法计算结束-----------")