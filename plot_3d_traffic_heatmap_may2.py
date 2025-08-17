import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取数据
file_path = r'f:\Math_model\CUMCM2024Problems\E\问题4支撑材料\5月2日车流量统计.csv'
df = pd.read_csv(file_path, encoding='gbk')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 获取唯一的交叉口名称和方向
intersections = df['交叉口'].unique()
directions = sorted(df['方向'].unique())

# 创建Z值矩阵（车流量）
Z = np.zeros((len(intersections), len(directions)), dtype=float)
for i, intersection in enumerate(intersections):
    for j, direction in enumerate(directions):
        value = df[(df['交叉口'] == intersection) & (df['方向'] == direction)]['方向计数'].values
        if len(value) > 0:
            Z[i, j] = value[0]

# 创建热力图
fig, ax = plt.subplots(figsize=(12, 10))

# 绘制热力图
im = ax.imshow(Z, cmap='viridis', aspect='auto')

# 设置坐标轴标签
ax.set_xlabel('方向')
ax.set_ylabel('交叉口')

# 设置坐标轴刻度
ax.set_xticks(np.arange(len(directions)))
ax.set_xticklabels(directions)
ax.set_yticks(np.arange(len(intersections)))
ax.set_yticklabels(intersections)

# 旋转x轴标签以提高可读性
plt.setp(ax.get_xticklabels(), rotation=0, ha='center', va='center')
plt.setp(ax.get_yticklabels(), rotation=0, ha='right', va='center')

# 添加颜色条
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('车流量')

# 在每个格子中添加数值
for i in range(len(intersections)):
    for j in range(len(directions)):
        text = ax.text(j, i, f'{int(Z[i, j])}',
                       ha='center', va='center', color='w', fontsize=8)

# 设置标题
ax.set_title('5月2日车流量热力图')

# 调整布局
plt.tight_layout()

# 保存图像
plt.savefig(r'f:\Math_model\CUMCM2024Problems\E\问题4支撑材料\5月2日车流量热力图.png', dpi=300, bbox_inches='tight')
plt.show()