import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('./CO2 Data/annualMeanCo2.csv')

fig = go.Figure(go.Scatter(x = df['year'],
                           y = df['mean'],
                           name= "<b>CO2 (ppm)</b>"))

fig.update_layout(title='<b>Average Atmospheric CO2 (ppm)</b>',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

fig.update_xaxes(title_text = "<b>Year</b>")
fig.update_yaxes(title_text = "<b>CO2 (ppm)</b>")

fig.update_layout(height = 600, width = 1200, title_text = "<b>Average Atmospheric CO2 (ppm)</b>")
fig.show()