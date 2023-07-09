"""This file is used to fill in missing data values"""
import copy

import pandas as pd


def fill_missing_with_median(data: pd.DataFrame, columns_to_fill: list) -> pd.DataFrame:
    """
        States:The function fills the specified column of data using the median

        Input: data:pd.DataFrame,columns_to_fill:list

        Output: filled_data:pd.DataFrame

        Notice:The function has no effect on original data,but require more space.
    """
    filled_data = copy.deepcopy(data)
    for column in columns_to_fill:
        median_value = filled_data[column].median()
        filled_data[column].fillna(median_value, inplace=True)
    return filled_data


def fill_missing_with_mean(data: pd.DataFrame, columns_to_fill: list) -> pd.DataFrame:
    """
        States:The function fills the specified column of data using the mean

        Input: data:pd.DataFrame,columns_to_fill:list

        Output: filled_data:pd.DataFrame

        Notice:The function has no effect on original data,but require more space.
    """
    filled_data = copy.deepcopy(data)
    for column in columns_to_fill:
        mean_value = filled_data[column].mean()
        filled_data[column].fillna(mean_value, inplace=True)
    return filled_data


def fill_missing_with_mode(data: pd.DataFrame, columns_to_fill: list) -> pd.DataFrame:
    """
        States:The function fills the specified column of data using the mode

        Input: data:pd.DataFrame,columns_to_fill:list

        Output: filled_data:pd.DataFrame

        Notice:The function has no effect on original data,but require more space.
    """
    filled_data = copy.deepcopy(data)
    for column in columns_to_fill:
        mode_value = filled_data[column].mode()
        filled_data[column].fillna(mode_value, inplace=True)
    return filled_data


def fill_missing_with_positive_three_std_deviation(data: pd.DataFrame, columns_to_fill: list) -> pd.DataFrame:
    """
        States:The function fills the specified column of data using the positive three standard deviation

        Input: data:pd.DataFrame,columns_to_fill:list

        Output: filled_data:pd.DataFrame

        Notice:The function has no effect on original data,but require more space.
    """
    filled_data = copy.deepcopy(data)
    for column in columns_to_fill:
        std_value = filled_data[column].mean() + 3 * filled_data[column].std()
        filled_data[column].fillna(std_value, inplace=True)
    return filled_data


def fill_missing_with_negative_three_std_deviation(data: pd.DataFrame, columns_to_fill: list) -> pd.DataFrame:
    """
        States:The function fills the specified column of data using the negative three standard deviation

        Input: data:pd.DataFrame,columns_to_fill:list

        Output: filled_data:pd.DataFrame

        Notice:The function has no effect on original data,but require more space.
    """
    filled_data = copy.deepcopy(data)
    for column in columns_to_fill:
        std_value = filled_data[column].mean() - 3 * filled_data[column].std()
        filled_data[column].fillna(std_value, inplace=True)
    return filled_data


def fill_missing_with_specified_rule(data: pd.DataFrame, columns_to_fill: list, choice=1, num=0) -> pd.DataFrame:
    """
        States:The function fills the specified column of data using the specified rule

        Rule:
                1.  (default)The function fills the specified column of data using specified number
                2.  The function fills the specified column of data using the value above of the missing value
                3.  The function fills the specified column of data using the value below of the missing value
                4.  The function fills the specified column of data by delete the row which is completely empty

        Input: data:pd.DataFrame,columns_to_fill:list

        Output: filled_data:pd.DataFrame

        Notice:The function has no effect on original data,but require more space.
    """
    filled_data = copy.deepcopy(data)
    if choice == 4:
        return filled_data[~filled_data.isnull().all(axis=1)]
    for column in columns_to_fill:
        if choice == 1:
            filled_data[column].fillna(num, inplace=True)
        elif choice == 2:
            filled_data.fillna(method='ffill', axis=0, inplace=True)
        elif choice == 3:
            filled_data.fillna(method='bfill', axis=0, inplace=True)
    return filled_data
