import glob,os

import pandas as pd

from bokeh.io import output_notebook
from bokeh.plotting import figure, show, ColumnDataSource
from bokeh.models import HoverTool, Range1d

from ipywidgets import interact


def prediction_triangle_file_list(prediction_folder):
    def plot(filepath):
        df = pd.read_csv(filepath)
        prediction_triangle(df)
    return interact(plot, filepath=glob.glob('%s/*csv'%prediction_folder))

def prediction_triangle(df):
    
    df['true_label_color'] = df['true_label'].apply(label2color)
    df['true_label_text'] = df['true_label'].apply(label2text)
    
    source = ColumnDataSource(df)
    
    hover = HoverTool(
        tooltips="""
        <div>
            <div>
                <span style="font-size: 17px; font-weight: bold;">True Label: @true_label_text</span>
            </div>
            <div>
                <img
                    src="@img_filepath" height="300" alt="@img_filepath" width="300"
                    style="float: left; margin: 0px 15px 15px 0px;"
                    border="2"
                ></img>
            </div>
            
        </div>
        """
    )
    
    p = figure(plot_width=600, plot_height=600, 
               toolbar_location = 'right',
               tools='pan,box_zoom,wheel_zoom,reset')
    p.add_tools(hover)
    circles = p.circle('prob1', 'prob2', size=10, source=source)
    circles.glyph.fill_color = 'true_label_color'
    
    p.x_range = Range1d(0.0, 1.0)
    p.y_range = Range1d(0.0, 1.0)

    output_notebook()
    show(p)
    
def label2color(x):
    colors = ['red','green','blue','black']
    return colors[x-1]

def label2text(x):
    if x==4:
        return 'unknown'
    else:
        return x