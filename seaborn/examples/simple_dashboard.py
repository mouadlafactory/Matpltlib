import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import seaborn as sns

# Load sample data
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')

# Initialize Dash app
app = dash.Dash(__name__)

# Custom CSS with Tailwind-like classes
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Create visualizations
def create_sales_chart():
    """Create sales trend chart"""
    # Generate sample sales data
    dates = pd.date_range('2023-01-01', periods=30, freq='D')
    sales = np.random.normal(1000, 200, 30).cumsum()
    
    fig = px.line(
        x=dates, y=sales,
        title="📈 Sales Trend (Last 30 Days)",
        labels={'x': 'Date', 'y': 'Sales ($)'}
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12),
        title_font_size=16,
        height=400
    )
    return fig

def create_tips_scatter():
    """Create tips scatter plot"""
    fig = px.scatter(
        tips, x='total_bill', y='tip', color='sex',
        title="💰 Tips vs Total Bill",
        labels={'total_bill': 'Total Bill ($)', 'tip': 'Tip ($)'}
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12),
        title_font_size=16,
        height=400
    )
    return fig

def create_iris_heatmap():
    """Create iris correlation heatmap"""
    numeric_cols = iris.select_dtypes(include=[np.number]).columns
    corr_matrix = iris[numeric_cols].corr()
    
    fig = px.imshow(
        corr_matrix,
        title="🌺 Iris Dataset Correlation Heatmap",
        color_continuous_scale='RdBu'
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12),
        title_font_size=16,
        height=400
    )
    return fig

def create_tips_boxplot():
    """Create tips boxplot by day"""
    fig = px.box(
        tips, x='day', y='tip', color='sex',
        title="📊 Tips Distribution by Day and Gender"
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12),
        title_font_size=16,
        height=400
    )
    return fig

# App layout
app.layout = html.Div([
    # Header
    html.Div([
        html.H1("📊 Interactive Data Dashboard", 
               className="text-4xl font-bold text-white text-center mb-4"),
        html.P("Beautiful visualizations with Dash, Plotly & Tailwind CSS", 
              className="text-xl text-blue-100 text-center")
    ], className="bg-gradient-to-r from-blue-600 to-purple-600 p-8 rounded-lg mb-8 shadow-lg"),
    
    # KPI Cards
    html.Div([
        html.Div([
            html.Div([
                html.I(className="fas fa-chart-line text-4xl text-green-500 mb-3"),
                html.H3("Total Sales", className="text-xl font-bold text-gray-800 mb-2"),
                html.P("$45,230", className="text-3xl font-bold text-green-600")
            ], className="text-center p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-all duration-300")
        ], className="w-full md:w-1/3 p-3"),
        
        html.Div([
            html.Div([
                html.I(className="fas fa-users text-4xl text-blue-500 mb-3"),
                html.H3("Customers", className="text-xl font-bold text-gray-800 mb-2"),
                html.P("1,234", className="text-3xl font-bold text-blue-600")
            ], className="text-center p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-all duration-300")
        ], className="w-full md:w-1/3 p-3"),
        
        html.Div([
            html.Div([
                html.I(className="fas fa-star text-4xl text-yellow-500 mb-3"),
                html.H3("Satisfaction", className="text-xl font-bold text-gray-800 mb-2"),
                html.P("4.8/5", className="text-3xl font-bold text-yellow-600")
            ], className="text-center p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-all duration-300")
        ], className="w-full md:w-1/3 p-3")
    ], className="flex flex-wrap mb-8"),
    
    # Charts Row 1
    html.Div([
        html.Div([
            dcc.Graph(figure=create_sales_chart())
        ], className="w-full lg:w-1/2 p-4 bg-white rounded-lg shadow-md mb-4"),
        
        html.Div([
            dcc.Graph(figure=create_tips_scatter())
        ], className="w-full lg:w-1/2 p-4 bg-white rounded-lg shadow-md mb-4")
    ], className="flex flex-wrap"),
    
    # Charts Row 2
    html.Div([
        html.Div([
            dcc.Graph(figure=create_iris_heatmap())
        ], className="w-full lg:w-1/2 p-4 bg-white rounded-lg shadow-md mb-4"),
        
        html.Div([
            dcc.Graph(figure=create_tips_boxplot())
        ], className="w-full lg:w-1/2 p-4 bg-white rounded-lg shadow-md mb-4")
    ], className="flex flex-wrap"),
    
    # Interactive Section
    html.Div([
        html.H3("🎛️ Interactive Controls", className="text-2xl font-bold text-gray-800 mb-6 text-center"),
        html.Div([
            html.Div([
                html.Label("Select Day:", className="block text-sm font-medium text-gray-700 mb-2"),
                dcc.Dropdown(
                    id='day-dropdown',
                    options=[{'label': day, 'value': day} for day in tips['day'].unique()],
                    value=tips['day'].unique()[0],
                    className="mb-4"
                )
            ], className="w-full md:w-1/2 p-4"),
            
            html.Div([
                html.Label("Select Gender:", className="block text-sm font-medium text-gray-700 mb-2"),
                dcc.Dropdown(
                    id='gender-dropdown',
                    options=[{'label': gender, 'value': gender} for gender in tips['sex'].unique()],
                    value=tips['sex'].unique()[0],
                    className="mb-4"
                )
            ], className="w-full md:w-1/2 p-4")
        ], className="flex flex-wrap")
    ], className="bg-white rounded-lg shadow-md p-6 mb-8"),
    
    # Dynamic Chart
    html.Div([
        html.H3("📊 Dynamic Visualization", className="text-2xl font-bold text-gray-800 mb-4 text-center"),
        dcc.Graph(id='dynamic-chart')
    ], className="bg-white rounded-lg shadow-md p-6 mb-8"),
    
    # Footer
    html.Div([
        html.P("🚀 Built with Dash, Plotly, and Tailwind CSS", 
               className="text-center text-gray-600 py-4 text-lg")
    ], className="bg-gray-100 rounded-lg")
    
], className="min-h-screen bg-gray-100 p-4")

# Callback for dynamic chart
@app.callback(
    Output('dynamic-chart', 'figure'),
    [Input('day-dropdown', 'value'),
     Input('gender-dropdown', 'value')]
)
def update_dynamic_chart(selected_day, selected_gender):
    filtered_tips = tips[(tips['day'] == selected_day) & (tips['sex'] == selected_gender)]
    
    fig = px.histogram(
        filtered_tips, x='total_bill', nbins=20,
        title=f"💳 Bill Distribution - {selected_day} ({selected_gender})",
        labels={'total_bill': 'Total Bill ($)', 'count': 'Frequency'}
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12),
        title_font_size=16,
        height=400
    )
    
    return fig

if __name__ == '__main__':
    print("🚀 Starting Dashboard...")
    print("📊 Open your browser to: http://localhost:8050")
    app.run_server(debug=True, host='0.0.0.0', port=8050)
