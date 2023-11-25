from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from joblib import dump, load
import plotly.express as px
import plotly.graph_objects as go
import uuid



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def wakeup():
    request_type_str = request.method
    if request_type_str == 'GET':
     return render_template('index.html', href='static/baseline.svg')
    else:
        text = request.form['text']
        random_string = uuid.uuid4().hex
        path = "static/predictions_graph" + random_string + ".svg"
        model = load('iris.joblib')
        widths_array = format_input(text)
        plot_model('iris/iris.data.csv', model, widths_array, path)
        return render_template('index.html', href=path)


def plot_model(training_data_file_name, model, petal_width_input, model_output_graph):
    data = pd.read_csv("./iris/iris.data.csv")
    petal_length = data["p_len"]
    petal_width = data["p_wid"]
    p_len_np = petal_length.to_numpy()
    p_wid_np = petal_width.to_numpy()
    p_wid_np_reshape = p_wid_np.reshape(len(petal_width),1)
    p_wid_np_reshape        
    preds = model.predict(p_wid_np_reshape)
    fig = px.scatter(x=petal_width,y=petal_length,title="length versus height of petals",labels={'x': 'petal width', 'y': 'petal length'})
    fig.add_trace(go.Scatter(x=p_wid_np, y=preds, mode='lines', name='Model'))
    new_preds = model.predict(petal_width_input)
    fig.add_trace(go.Scatter(x=petal_width_input.reshape(len(petal_width_input)), y=new_preds, name='New Outputs', mode='markers', marker=dict(color='purple', size=20, line=dict(color='purple', width=2))))
    fig.write_image(model_output_graph, width=800)
    fig.show()

def format_input(input_lst):
    def is_float(s):
        try:
            float(s)
            return True
        except:
            return False
    input_list = np.array([float(x) for x in input_lst.split(',') if is_float(x)])
    return input_list.reshape(len(input_list),1)