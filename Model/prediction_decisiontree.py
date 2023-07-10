"""This file is used for decision tree classification"""
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier as DecisionTree
import sklearn.tree as tree
import pandas as pd
from sklearn.model_selection import train_test_split


def DecisionTreeClassifier(data: pd.DataFrame,path=None,random_state_tree: int = 0,test_size:int = 0.2,
                           random_state_split:int = 0) -> DecisionTree:
    """
    :param data: 完整的数据集:第一列是标签，剩余列是特征
    :param path: 保存路径
    :param random_state_tree: 决策树随机种子
    :param test_size: 测试集比例
    :param random_state_split: 切割集随机种子
    :return:DecisionTreeClassifier 分类器
    """
    if path is None:
        path = []
    X=data.drop(columns=data.columns[0])
    y=data[data.columns[0]]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state_split)
    tree = DecisionTree(random_state=random_state_tree)
    tree.fit(X_train, y_train)
    y_pred=tree.predict(X_test)
    accuracy=accuracy_score(y_test,y_pred)
    print(accuracy)
    # TODO: 优化模型

    # TODO: 输出模型效果

    return tree