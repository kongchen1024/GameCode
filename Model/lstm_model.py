import torch
import torch.nn as nn

# 定义神经网络模型
class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# 定义模型参数
input_size = 784  # 输入特征维度
hidden_size = 128  # 隐藏层维度
num_classes = 10  # 输出类别数

# 创建模型实例
model = NeuralNetwork(input_size, hidden_size, num_classes)

# 定义输入数据
input_data = torch.randn(10, 784)  # 示例输入数据，批量大小为10

# 运行前向传播
output = model(input_data)

# 打印输出结果
print(output)
