# learn_to_chart 使用指南

## 启动项目

### 初始化项目

```
git clone https://github.com/LancelotLewis/learn_to_chart.git
```

### 虚拟环境

```
python -m venv .venv

source .venv/Scripts/activate
```

### 安装依赖

```
pip install -r requirements.txt
```

> 示例使用的是 python 3.7.8 ，如果安装的是其他版本的 python，请手动安装 flask、pandas、pyecharts、matplotlib、python-dotenv 即可

### 启动项目

```
flask run
```

## 开发项目

项目中 demo 分为三个部分

### 1. 使用 js 库 echarts 绘制图表（纯 js 库，不熟可能难度稍大，但 js 其实挺好学的）

/echarts

### 2. 使用 python 库 pyecharts 绘制图表（本质上还是用的 echarts，所以尽量还是用 echarts 比较方便）

/pyecharts

### 3. 使用 python 库 matplotlib 绘制图表（绘制的结果是 jpg 或 png，效果不如 echarts）

/matplotlib
