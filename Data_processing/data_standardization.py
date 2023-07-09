"""This file is used to standardize data"""
import copy
import pandas as pd
from sklearn.preprocessing import StandardScaler


def min_max_standardization(data: pd.DataFrame) -> pd.DataFrame:
    """
        States:min_max_standardization-->>Convert to a range of 0 to 1 a range of 0 to 1

        Equation:(data-data.min())/(data.max()-data.min())

        Input: Each column of the data is a research indicate

        Output:data that has been minimized,the type is also pd.DataFrame

        Notice:this function has no effect on original data,but require more space.
    """
    standardized_data = copy.deepcopy(data)
    standardized_data = (standardized_data - standardized_data.min()) / \
                        (standardized_data.max() - standardized_data.min())
    return standardized_data


def normalization(data: pd.DataFrame) -> pd.DataFrame:
    """
        States:normalization-->>Convert to a range of 0 to 1 a range of 0 to 1

        Equation:data/data.sum(axis=0)

        Input: Each column of the data is research indicate

        Output:data that has been normalization,the type is also pd.DataFrame

        Notice:this function has no effect on original data,but require more space.
    """
    standardized_data = copy.deepcopy(data)
    return standardized_data.div(standardized_data.sum(axis=0))


def z_score_standardization(data: pd.DataFrame) -> pd.DataFrame:
    """
        States:normalization-->>Convert to mean=0,sigma=1

        Equation:(data-data.mean())/(data.max()-data.min())

        Input: Each column of the data is a research indicate

        Output:data that has been standardized,the type is also pd.DataFrame

        Notice:this function has no effect on original data,but require more space.
    """
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(copy.deepcopy(data))
    standardized_df = pd.DataFrame(standardized_data, columns=data.columns)
    return standardized_df


def center_standardization(data: pd.DataFrame) -> pd.DataFrame:
    """
        States:normalization-->>Convert to mean=0,sigma=1

        Equation:data-data.mean(axis=0)

        Input: Each column of the data is a research indicate

        Output:data that has been standardized,the type is also pd.DataFrame

        Notice:this function has no effect on original data,but require more space.
    """
    standardized_data = copy.deepcopy(data)
    return standardized_data - standardized_data.mean()


def positive_indicator_processing(data: pd.DataFrame, columns_to_convert: list) -> pd.DataFrame:
    """
        States:forward index processing-->>Convert positive index to a range of 0 to 1

        Equation:(X-min)/(max-min)

        Input: data:pd.DataFrame,columns_to_convert:list

        Output: standardized_data:pd.DataFrame

        Notice:this function has no effect on original data,but require more space.
    """
    standardized_data = copy.deepcopy(data)
    for column in columns_to_convert:
        cur = standardized_data[column]
        cur = (cur.max() - cur) / (cur.max() - cur.min())
        standardized_data[column] = cur
    return standardized_data


def negative_indicator_processing(data: pd.DataFrame, columns_to_convert:list) -> pd.DataFrame:
    """
        States:negative index processing-->>Convert forward index to a range of 0 to 1

        Equation:(X-min)/(max-min)

        Input: data:pd.DataFrame,columns_to_convert:list

        Output: standardized_data:pd.DataFrame

        Notice:this function has no effect on original data,but require more space.
    """
    standardized_data = copy.deepcopy(data)
    for column in columns_to_convert:
        cur = standardized_data[column]
        cur = (cur - cur.min()) / (cur.max() - cur.min())
        standardized_data[column]=cur
    return standardized_data
