import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px

app = dash.Dash()

data = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [10, 11, 12, 13]})
fig = px.line(data, x='x', y='y')
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
