import pandas as pd
import plotly.graph_objects as go
import dash_table

from plotlydash.views.helpers import *


def create_df():

    df_node = pd.DataFrame()
    df_node['index'] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    df_node['label'] = [
        'Data Source #2', 'Filter Data', 'Data Source #1', 'Duplicate Data', 
        'Clean #1', 'Clean #2', 'Final Data', 'Merge', 'Data Source #3'
    ]
    df_node['x'] = [0.1, 0.9, 0.1, 0.9, 0.45, 0.62, 0.9, 0.27, 0.1]
    df_node['y'] = [0.45, 0.6, 0.1, 0.12, 0.4, 0.7, 0.39, 0.4, 0.9]
    df_node['color'] = ['#e63946', '#a8dadc', '#e63946', '#a8dadc', '#1d3557', '#1d3557', '#457b9d', '#1d3557', '#e63946']

    df_link = pd.DataFrame()
    df_link['source'] = [5, 5, 2, 4, 0, 4, 7, 8]
    df_link['target'] = [1, 6, 7, 3, 7, 5, 4, 7]
    df_link['value'] = [2.0, 4.6, 2.0, 3.4, 3.4, 6.6, 10.0, 4.6]

    return df_node, df_link

def create_sankey_chart(df_node, df_link):
    
    fig = go.Figure(go.Sankey(
        arrangement = "snap",
        node = {
            "label": df_node.label,
            "x": df_node.x,
            "y": df_node.y,
            "color": df_node.color,
            "pad":1  # 10 Pixels,
        },
        link = {
            "source": df_link.source,
            "target": df_link.target,
            "value": df_link.value
        },
    ))

    fig.update_layout(
        hovermode = 'x',
        font=dict(size = 16, family="arial", color="black"),
        margin=dict(l=0, r=0, t=30, b=60),
        paper_bgcolor='#f9f9f9'
    )

    return fig

def create_dash_datatable(df_node, df_link):

    df = pd.merge(df_link, df_node, left_on='source', right_on='index', how='left')
    df = pd.merge(df, df_node, left_on='target', right_on='index', how='left', suffixes=('_source', '_target'))

    df = df.sort_values(by='source')

    styles = []
    # print('for loop')
    for i in range(df.shape[0]):
        # print(i)
        # print(df['label_target'][i], ' : ', df['color_target'][i])
        # print(df['label_source'][i], ' : ', df['color_source'][i])
        styles.append(
            {
                'if': {
                    'row_index': i, 
                    'column_id': 'Target'
                }, 
                'background-color': df['color_target'][i], 
                'color': determine_font_color(df['color_target'][i])
            }
        )
        styles.append(
            {
                'if': {
                    'row_index': i, 
                    'column_id': 'Source'
                }, 
                'background-color': df['color_source'][i], 
                'color': determine_font_color(df['color_source'][i])

            }
        )

    df = df[['label_source', 'label_target', 'value']]
    # df = df[['label_source', 'label_target', 'value', 'x_source', 'y_source', 'x_target', 'y_target']]
    df.rename(columns={'label_source': 'Source', 'label_target': 'Target', 'value': 'Value'}, inplace=True)

    table = dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
                style_cell={'textAlign': 'center'},
                style_data_conditional=styles
            )

    return table