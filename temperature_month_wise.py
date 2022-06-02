import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  

app = Dash(__name__)

df=pd.read_csv('temperature_month_wise.csv')
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {'label':str(x),'value':x}
                     for x in df['dt'].unique()],
                 multi=False,
                 value="2001-10-01",
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='temperature_map', figure={})

])
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='temperature_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The date chosen is: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["dt"] == option_slctd]

    fig = px.choropleth(
        data_frame=dff,
        locations='Code',
        color='AverageTemperature',
        hover_data=['Country', 'AverageTemperature'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        template='plotly_dark'
    )

    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)