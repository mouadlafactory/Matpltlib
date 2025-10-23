import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Initialize Dash app
app = dash.Dash(__name__)

# Sample data generation
def generate_sample_data():
    """Generate comprehensive sample data for the dashboard"""
    np.random.seed(42)
    
    # Sales data
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    sales_data = []
    
    for date in dates:
        base_sales = 1000 + np.random.normal(0, 200)
        seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * date.dayofyear / 365)
        sales_data.append({
            'date': date,
            'sales': max(0, base_sales * seasonal_factor),
            'region': np.random.choice(['North', 'South', 'East', 'West']),
            'product': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home']),
            'customer_type': np.random.choice(['Premium', 'Standard', 'Basic'])
        })
    
    df = pd.DataFrame(sales_data)
    
    # Customer demographics
    customer_data = []
    for i in range(1000):
        customer_data.append({
            'age': np.random.normal(35, 12),
            'income': np.random.normal(50000, 20000),
            'satisfaction': np.random.uniform(1, 5),
            'region': np.random.choice(['North', 'South', 'East', 'West']),
            'gender': np.random.choice(['Male', 'Female'])
        })
    
    customer_df = pd.DataFrame(customer_data)
    
    return df, customer_df

# Generate data
sales_df, customer_df = generate_sample_data()

# Custom CSS with Tailwind-like styling
external_stylesheets = [
    'https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Define the layout
app.layout = html.Div([
    # Header
    html.Div([
        html.Div([
            html.H1("📊 Advanced Analytics Dashboard", 
                   className="text-4xl font-bold text-white mb-2"),
            html.P("Real-time business intelligence and data visualization", 
                  className="text-xl text-blue-100")
        ], className="text-center")
    ], className="bg-gradient-to-r from-blue-600 to-purple-600 p-8 rounded-lg mb-8 shadow-lg"),
    
    # KPI Cards
    html.Div([
        html.Div([
            html.Div([
                html.I(className="fas fa-chart-line text-3xl text-green-500 mb-2"),
                html.H3("Total Sales", className="text-2xl font-bold text-gray-800"),
                html.P(f"${sales_df['sales'].sum():,.0f}", className="text-3xl font-bold text-green-600")
            ], className="text-center p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow")
        ], className="w-full md:w-1/4 p-2"),
        
        html.Div([
            html.Div([
                html.I(className="fas fa-users text-3xl text-blue-500 mb-2"),
                html.H3("Total Customers", className="text-2xl font-bold text-gray-800"),
                html.P(f"{len(customer_df):,}", className="text-3xl font-bold text-blue-600")
            ], className="text-center p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow")
        ], className="w-full md:w-1/4 p-2"),
        
        html.Div([
            html.Div([
                html.I(className="fas fa-star text-3xl text-yellow-500 mb-2"),
                html.H3("Avg Satisfaction", className="text-2xl font-bold text-gray-800"),
                html.P(f"{customer_df['satisfaction'].mean():.1f}/5", className="text-3xl font-bold text-yellow-600")
            ], className="text-center p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow")
        ], className="w-full md:w-1/4 p-2"),
        
        html.Div([
            html.Div([
                html.I(className="fas fa-calendar text-3xl text-purple-500 mb-2"),
                html.H3("Days Tracked", className="text-2xl font-bold text-gray-800"),
                html.P(f"{len(sales_df)}", className="text-3xl font-bold text-purple-600")
            ], className="text-center p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow")
        ], className="w-full md:w-1/4 p-2")
    ], className="flex flex-wrap mb-8"),
    
    # Charts Row 1
    html.Div([
        # Sales Trend Chart
        html.Div([
            html.H3("📈 Sales Trend Over Time", className="text-2xl font-bold text-gray-800 mb-4"),
            dcc.Graph(
                id='sales-trend-chart',
                figure=px.line(
                    sales_df.groupby('date')['sales'].sum().reset_index(),
                    x='date', y='sales',
                    title="Daily Sales Trend",
                    color_discrete_sequence=['#3B82F6']
                ).update_layout(
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    font=dict(size=12),
                    title_font_size=16
                )
            )
        ], className="w-full lg:w-1/2 p-4 bg-white rounded-lg shadow-md"),
        
        # Regional Sales
        html.Div([
            html.H3("🗺️ Sales by Region", className="text-2xl font-bold text-gray-800 mb-4"),
            dcc.Graph(
                id='regional-sales-chart',
                figure=px.pie(
                    sales_df.groupby('region')['sales'].sum().reset_index(),
                    values='sales', names='region',
                    title="Sales Distribution by Region",
                    color_discrete_sequence=['#10B981', '#F59E0B', '#EF4444', '#8B5CF6']
                ).update_layout(
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    font=dict(size=12),
                    title_font_size=16
                )
            )
        ], className="w-full lg:w-1/2 p-4 bg-white rounded-lg shadow-md")
    ], className="flex flex-wrap mb-8"),
    
    # Charts Row 2
    html.Div([
        # Customer Demographics
        html.Div([
            html.H3("👥 Customer Demographics", className="text-2xl font-bold text-gray-800 mb-4"),
            dcc.Graph(
                id='customer-scatter',
                figure=px.scatter(
                    customer_df, x='age', y='income', color='satisfaction',
                    size='satisfaction', hover_data=['region', 'gender'],
                    title="Customer Age vs Income (colored by satisfaction)",
                    color_continuous_scale='Viridis'
                ).update_layout(
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    font=dict(size=12),
                    title_font_size=16
                )
            )
        ], className="w-full lg:w-1/2 p-4 bg-white rounded-lg shadow-md"),
        
        # Product Performance
        html.Div([
            html.H3("📦 Product Performance", className="text-2xl font-bold text-gray-800 mb-4"),
            dcc.Graph(
                id='product-bar',
                figure=px.bar(
                    sales_df.groupby('product')['sales'].sum().reset_index(),
                    x='product', y='sales',
                    title="Sales by Product Category",
                    color='sales',
                    color_continuous_scale='Blues'
                ).update_layout(
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    font=dict(size=12),
                    title_font_size=16,
                    xaxis_tickangle=-45
                )
            )
        ], className="w-full lg:w-1/2 p-4 bg-white rounded-lg shadow-md")
    ], className="flex flex-wrap mb-8"),
    
    # Charts Row 3
    html.Div([
        # Heatmap
        html.Div([
            html.H3("🔥 Customer Satisfaction Heatmap", className="text-2xl font-bold text-gray-800 mb-4"),
            dcc.Graph(
                id='satisfaction-heatmap',
                figure=px.density_heatmap(
                    customer_df, x='age', y='income',
                    title="Customer Density by Age and Income",
                    color_continuous_scale='Reds'
                ).update_layout(
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    font=dict(size=12),
                    title_font_size=16
                )
            )
        ], className="w-full lg:w-1/2 p-4 bg-white rounded-lg shadow-md"),
        
        # 3D Scatter
        html.Div([
            html.H3("🌐 3D Customer Analysis", className="text-2xl font-bold text-gray-800 mb-4"),
            dcc.Graph(
                id='3d-scatter',
                figure=px.scatter_3d(
                    customer_df, x='age', y='income', z='satisfaction',
                    color='region', size='satisfaction',
                    title="3D Customer Analysis",
                    color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
                ).update_layout(
                    plot_bgcolor='white',
                    paper_bgcolor='white',
                    font=dict(size=12),
                    title_font_size=16
                )
            )
        ], className="w-full lg:w-1/2 p-4 bg-white rounded-lg shadow-md")
    ], className="flex flex-wrap mb-8"),
    
    # Interactive Controls
    html.Div([
        html.Div([
            html.H3("🎛️ Interactive Controls", className="text-2xl font-bold text-gray-800 mb-4"),
            html.Div([
                html.Label("Select Region:", className="block text-sm font-medium text-gray-700 mb-2"),
                dcc.Dropdown(
                    id='region-dropdown',
                    options=[{'label': region, 'value': region} for region in sales_df['region'].unique()],
                    value=sales_df['region'].unique()[0],
                    className="mb-4"
                ),
                html.Label("Select Product:", className="block text-sm font-medium text-gray-700 mb-2"),
                dcc.Dropdown(
                    id='product-dropdown',
                    options=[{'label': product, 'value': product} for product in sales_df['product'].unique()],
                    value=sales_df['product'].unique()[0],
                    className="mb-4"
                ),
                html.Button("🔄 Refresh Data", id="refresh-button", 
                           className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition-colors")
            ], className="p-6 bg-gray-50 rounded-lg")
        ], className="w-full p-4 bg-white rounded-lg shadow-md")
    ], className="mb-8"),
    
    # Footer
    html.Div([
        html.P("📊 Built with Dash, Plotly, and Tailwind CSS", 
               className="text-center text-gray-600 py-4")
    ], className="bg-gray-100 rounded-lg")
    
], className="min-h-screen bg-gray-100 p-4")

# Callbacks for interactivity
@app.callback(
    Output('sales-trend-chart', 'figure'),
    [Input('region-dropdown', 'value'),
     Input('product-dropdown', 'value')]
)
def update_sales_trend(selected_region, selected_product):
    filtered_df = sales_df[
        (sales_df['region'] == selected_region) & 
        (sales_df['product'] == selected_product)
    ]
    
    fig = px.line(
        filtered_df.groupby('date')['sales'].sum().reset_index(),
        x='date', y='sales',
        title=f"Sales Trend - {selected_region} {selected_product}",
        color_discrete_sequence=['#3B82F6']
    ).update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=12),
        title_font_size=16
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
