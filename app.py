from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

from data_transformation import DataTransformer

transformer = DataTransformer()
data = transformer.ingest_clean('data.csv')
dfs = transformer.transform(data)

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

graphs = []

graph = px.pie(dfs[0],names='What type of internship are you interested in?', title='Distribution of internships')
graphs.append(graph)

graph = px.bar(dfs[1], x='How much are you willing to spend for going abroad?', color='Gender', title='Global Talent')
graphs.append(graph)

graph = px.bar(dfs[2], x='How much are you willing to spend for going abroad?', color='Gender', title='Global Teacher')
graphs.append(graph)

graph = px.bar(dfs[3], x='How much are you willing to spend for going abroad?', color='Gender', title='Global Volunteer')
graphs.append(graph)



graph = px.pie(dfs[1],names='Where do you study?', title='Global Talent')
graphs.append(graph)

graph = px.pie(dfs[2],names='Where do you study?', title='Global Teacher')
graphs.append(graph)

graph = px.pie(dfs[3],names='Where do you study?', title='Global Volunteer')
graphs.append(graph)


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([dcc.Graph(figure=graphs[0])], width=6)
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(figure=graphs[1])]),
        dbc.Col([dcc.Graph(figure=graphs[2])])
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(figure=graphs[3])])
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(figure=graphs[4])])
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(figure=graphs[5])])
    ]),
    dbc.Row([
        dbc.Col([dcc.Graph(figure=graphs[6])])
    ])
])



if __name__ == "__main__":
    app.run_server(debug=True)