from semopy import Model
from semopy.examples import holzinger39


def structural_equation_model_fitting(desc):
    # 从 semopy 库加载 holzinger39 数据集
    data = holzinger39.get_data()
    # 使用 Model 类创建模型对象 mod
    mod = Model(desc)
    # 对模型进行拟合
    mod.fit(data)
    # 检验模型，输出每个参数的估计值、标准误等统计信息
    estimates = mod.inspect()
    # 打印参数估计结果
    return estimates

# 定义模型
desc = '''
# 定义测量模型
y1 =~ x1 + x2 + x3
y2 =~ x4 + x5 + x6
y3 =~ x7 + x8 + x9

# 定义结构模型
y1 ~ y2 + y3
y2 ~~ y3
'''
print(structural_equation_model_fitting(desc))
