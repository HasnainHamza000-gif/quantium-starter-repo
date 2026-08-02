import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# 1. Load the processed data from Task 2
df = pd.read_csv('formatted_data.csv')

# 2. Sort data chronologically by date
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# 3. Build the line chart with clear labels
fig = px.line(
    df,
    x='date',
    y='sales',
    title='Pink Morsel Sales Over Time (Price Increase on Jan 15, 2021)',
    labels={
        'date': 'Date',
        'sales': 'Total Sales ($USD)'
    }
)

# Optional: Add a visual indicator line for the price increase date
fig.add_vline(
    x='2021-01-15',
    line_dash='dash',
    line_color='red',
    annotation_text='Price Increase (Jan 15, 2021)',
    annotation_position='top left'
)

# 4. Initialize Dash App
app = dash.Dash(__name__)

# 5. Define Layout (Header + Line Chart)
app.layout = html.Div(children=[
    html.H1(
        children='Soul Foods: Pink Morsel Sales Analysis',
        style={'textAlign': 'center', 'fontFamily': 'sans-serif'}
    ),

    html.P(
        children='Visualizing Pink Morsel sales before and after the price increase on January 15th, 2021.',
        style={'textAlign': 'center', 'fontFamily': 'sans-serif'}
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# 6. Run Server
if __name__ == '__main__':
    app.run(debug=True)