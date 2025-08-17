import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取数据
file_path = r'f:\Math_model\CUMCM2024Problems\E\问题4支撑材料\5月5日车流量统计.csv'
df = pd.read_csv(file_path, encoding='gbk')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 获取唯一的交叉口名称和方向
intersections = df['交叉口'].unique()
directions = sorted(df['方向'].unique())

# 创建网格数据
X, Y = np.meshgrid(directions, range(len(intersections)))

# 创建Z值（车流量）
Z = np.zeros_like(X, dtype=float)
for i, intersection in enumerate(intersections):
    for j, direction in enumerate(directions):
        value = df[(df['交叉口'] == intersection) & (df['方向'] == direction)]['方向计数'].values
        if len(value) > 0:
            Z[i, j] = value[0]

# 创建等高线图
fig, ax = plt.subplots(figsize=(12, 8))

# 绘制填充等高线图
contour_filled = ax.contourf(X, Y, Z, levels=15, cmap='viridis')

# 绘制等高线
contour_lines = ax.contour(X, Y, Z, levels=15, colors='black', linewidths=0.5, alpha=0.7)

# 添加颜色条
cbar = plt.colorbar(contour_filled)
cbar.set_label('车流量')

# 添加等高线标签
ax.clabel(contour_lines, inline=True, fontsize=8, fmt='%1.0f')

# 设置坐标轴标签
ax.set_xlabel('方向')
ax.set_ylabel('交叉口')

# 设置y轴刻度标签为交叉口名称
ax.set_yticks(range(len(intersections)))
ax.set_yticklabels(intersections)

# 设置x轴刻度为方向值
ax.set_xticks(directions)

# 设置标题
ax.set_title('5月5日车流量等高线图')

# 保存图像
plt.savefig(r'f:\Math_model\CUMCM2024Problems\E\问题4支撑材料\5月5日车流量等高线图.png', dpi=300, bbox_inches='tight')
plt.show()