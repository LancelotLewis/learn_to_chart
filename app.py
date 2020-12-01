import pandas as pd
import numpy as np
from time import sleep
import matplotlib.pyplot as plt
from pyecharts.charts import Line
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

plt.switch_backend('agg')
# cmap = plt.get_cmap('viridis')
cmap = plt.get_cmap('Spectral')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/matplotlib')
def matplotlib_html():
    return render_template('matplotlib.html')

@app.route('/matplotlib/data', methods=['POST'])
def matplotlib_data():
    cols = request.form.getlist('cols')
    cols = list(cols)

    df = pd.read_csv('data/test.csv', index_col=0)
    df = pd.DataFrame(df, columns=cols)

    colors = cmap(np.linspace(0, 1, len(cols)))

    for index, col in enumerate(cols):
        plt.plot(list(df.index), df[col], c=colors[index], label=col)

    plt.legend()
    plt.savefig('static/matplotlib/result.png')
    sleep(1)
    plt.close('all')
    return jsonify({"url": '/static/matplotlib/result.png'})



@app.route('/pyecharts')
def pyecharts_html():
    return render_template('pyecharts.html')

@app.route('/pyecharts/data', methods=['POST'])
def pyecharts_data():
    cols = request.form.getlist('cols')
    cols = list(cols)

    df = pd.read_csv('data/test.csv', index_col=0)
    file = request.files.get('file')
    df = pd.read_csv(file, index_col=0)
    df = pd.DataFrame(df, columns=cols)


    line = Line()
    line.add_xaxis(list(df.index))
    for col in cols:
        print(col, df[col].to_list())
        line.add_yaxis(col, df[col].to_list())

    line.render('static/pyecharts/result.html')
    return jsonify({ 'url': '/static/pyecharts/result.html' })



@app.route('/echarts')
def echarts_html():
    return render_template('echarts.html')

@app.route('/echarts/data', methods=['POST'])
def echarts_data():
    cols = request.form.getlist('cols')
    cols = list(cols)

    # 通过form表单传递文件
    file = request.files.get('file')
    df = pd.read_csv(file, index_col=0)
    df = pd.DataFrame(df, columns=cols)
    return df.to_json(orient='split')
