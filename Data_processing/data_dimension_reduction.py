"""This file is used to Reduce the dimensionality of the data"""
import copy

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA as PCA_sklearn


def PCA(data: pd.DataFrame, total_variance_interpretation_rate: 80):
    """
    States:The function reduce the dimensionality of the data by PCA
    Input: data:pd.DataFrame
    total_variance_interpretation_rate:int,default:80%
    Output: reduced_data:pd.DataFrame
    """
    reduced_data = copy.deepcopy(data)
    # 探索合适的维数
    explained_data = pd.DataFrame(columns=['n_components', 'explained_variance_ratio'])  # 储存累计贡献率数据
    for n_components in range(1, min(reduced_data.shape[0],len(reduced_data.columns))):
        pca = PCA_sklearn(n_components=n_components)
        pca.fit(reduced_data)
        if np.sum(pca.explained_variance_ratio_) < total_variance_interpretation_rate: continue  # 默认 <80% 不采纳
        explained_data.loc[n_components] = [n_components, np.sum(pca.explained_variance_ratio_)]
    # 绘制累计贡献率曲线
    plt.rcParams['font.sans-serif'] = ['FangSong']
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(explained_data['n_components'], explained_data['explained_variance_ratio'], color='red', linewidth=2.0,
            linestyle='--', label='累计贡献率')
    ax.set_title('PCA累计贡献率', fontsize=16, fontweight='bold')
    ax.set_xlabel('维数大小', fontsize=14)
    ax.set_ylabel('累计贡献率', fontsize=14)
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.legend(fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.5)
    fig.tight_layout()
    plt.show()
    print(explained_data)
    # 选择降维维数
    n_components = input('请输入降维维数:')
    pca = PCA_sklearn(n_components= int(n_components))
    reduced_data = pca.fit_transform(reduced_data)
    return pd.DataFrame(reduced_data, columns=[f"Feature {i + 1}" for i in range(reduced_data.shape[1])]),pca.components_.T


if __name__ == '__main__':
    # 创建一个更大的具有明显主成分关系的DataFrame数据集
    data=pd.read_excel(r'D:\Pycharm\PyCharm 2022.1.2\统计建模大赛\数据表\原始数据表\湖南省水资源承载力数据.xlsx',sheet_name=2)
    data.set_index(data['市'],inplace=True)
    data.drop('市',axis=1,inplace=True)
    # 打印数据集的前几行
    print(data.head())
    reduced_data,A= PCA(data, total_variance_interpretation_rate=0.8)
    print(reduced_data.head())
    print(A)