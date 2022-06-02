import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  

app = Dash(__name__)

df=pd.read_csv('clusters.csv')
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[1],
                 multi=False,
                 value=1,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='co2_emission_map', figure={})

])
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='co2_emission_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "This is just an option: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Option"] == option_slctd]

    fig = px.choropleth(
        data_frame=dff,
        locations='Code',
        color='Cluster',
        hover_data=['Country_Name', 'Cluster'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        template='plotly_dark'
    )

    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)