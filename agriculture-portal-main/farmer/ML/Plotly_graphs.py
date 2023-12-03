from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd


class MakingGraphs():
    def __init__(self,filepath):
        self.filepath = filepath
        self.data = pd.read_csv(filepath)
    def makepie(self,labels,values,title_text):
        fig = go.Figure()
        fig.add_trace(go.Pie(
                labels=self.data[labels],
                values=self.data[values],
                titlefont=dict(size=20),
                titleposition='top right',
            ))
        fig.update_layout(
            title=title_text,
            paper_bgcolor="#222222",
            font_color="white",
            # line=dict(color='#000000', width=2),
        )
        fig.update_traces(marker=dict(line=dict(color='#000000', width=1)))
        return fig
    def makebar(self,x_val,y_val,title,x_title_text,y_title_text):
        fig = go.Figure()
        fig.add_trace(go.Bar(
                 x=self.data[x_val],
                 y=self.data[y_val],
                 base='group',
            marker=dict(
                color =  'darkolivegreen',
            )

             ),
        )
        fig.update_layout(
            xaxis_title= x_title_text,
            yaxis_title= y_title_text,
            title=title,
            paper_bgcolor="#222222",
            font_color="white",
        )
        return fig
    def make_rainfall_bar(self,markdown_value,title,x_title_text,y_title_text):
        fig = go.Figure()
        data1 = self.data[self.data['SUBDIVISION'] == markdown_value]
        reshaped_data = data1.loc[:, 'JAN':'DEC'].stack().reset_index(level=1)
        reshaped_data.columns = ['Month', 'Rainfall']
        if(markdown_value not in ['ANDAMAN & NICOBAR ISLANDS', 'ARUNACHAL PRADESH', 'ASSAM & MEGHALAYA', 'NAGA MANI MIZO TRIPURA', 'SUB HIMALAYAN WEST BENGAL & SIKKIM', 'GANGETIC WEST BENGAL', 'ORISSA', 'JHARKHAND', 'BIHAR', 'EAST UTTAR PRADESH', 'WEST UTTAR PRADESH', 'UTTARAKHAND', 'HARYANA DELHI & CHANDIGARH', 'PUNJAB', 'HIMACHAL PRADESH', 'JAMMU & KASHMIR', 'WEST RAJASTHAN', 'EAST RAJASTHAN', 'WEST MADHYA PRADESH', 'EAST MADHYA PRADESH', 'GUJARAT REGION', 'SAURASHTRA & KUTCH', 'KONKAN & GOA', 'MADHYA MAHARASHTRA', 'MATATHWADA', 'VIDARBHA', 'CHHATTISGARH', 'COASTAL ANDHRA PRADESH', 'TELANGANA', 'RAYALSEEMA', 'TAMIL NADU', 'COASTAL KARNATAKA', 'NORTH INTERIOR KARNATAKA', 'SOUTH INTERIOR KARNATAKA', 'KERALA', 'LAKSHADWEEP']):
            markdown_value = "Not Selected"
        fig.add_trace(go.Bar(
            x=reshaped_data['Month'],
            y=reshaped_data['Rainfall'],
            base='group',
            marker=dict(
                color =  'coral',
            )

             ),
        )
        fig.update_layout(
            xaxis_title= markdown_value,
            yaxis_title= y_title_text,
            title=title + markdown_value.title(),
            paper_bgcolor="#202422",
            font_color="white",
        )
        return fig
    def makeScatter(self,x_val,y_val,z_val,title,x_title_text,y_title_text):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
                 x=self.data[x_val],
                 y=self.data[y_val],
                 mode = "markers",
                    
             ),
        )
        fig.update_layout(
            title=title,
            paper_bgcolor="#222222",
            font_color="white",
        )
        return fig

rainfall = MakingGraphs('C:/xampp/htdocs/agriculture-portal-main/farmer/ML/rainfall_prediction/rainfall_in_india_1901-2017.csv')
yield_boi = MakingGraphs('C:/xampp/htdocs/agriculture-portal-main/farmer/ML/yield_prediction/crop_production_karnataka.csv')

app = Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(
    [
        html.H3("Select a dataset to visualize".title()),
        html.Div(children=[
            html.H4("Crop Predition Dataset:"),
            dcc.RadioItems(
                id="selection_crop_pred",
                options=[
                    {"label": "Crop Predition 1", "value": "No Of Users per stop"},
                    {"label": "Crop Predition 2", "value": "No Of Users throughtout the day"},
                    {'label':'Crop Predition 3','value':'Scheduled time vs Real Time'},
                ],
            ),],style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw'}),
        html.Div(children=[
            html.H4("\nCrop Recommendation Dataset:"),
            dcc.RadioItems(
                id="selection_crop_recommend",
                options=[
                    {"label": "Crop Recommendation 1", "value": "No Of Users per stop"},
                    {"label": "Crop Recommendation 2", "value": "No Of Users throughtout the day"},
                    {'label':'Crop Recommendation 3','value':'Scheduled time vs Real Time'},
                ],
            ),], style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw'}),
        html.Div(children=[
            html.H4("Rainfall In India Dataset:"),
            dcc.RadioItems(
                id="selection_rain",
                options=[
                    {"label": 'States Represented In Analysis', "value": 'Average Rainfall in Pie Chart'},
                    {"label": 'States Represented In Bar Graph', "value": 'Average Rainfall in Bar Graph'},
                    {'label':'Rainfall Throughtout The Year In','value':'Rainfall Per Month In Each State'},
                ],
            ),
            dcc.Dropdown(
            options = {'ANDAMAN & NICOBAR ISLANDS': 'ANDAMAN & NICOBAR ISLANDS', 'ARUNACHAL PRADESH': 'ARUNACHAL PRADESH', 'ASSAM & MEGHALAYA': 'ASSAM & MEGHALAYA', 'NAGA MANI MIZO TRIPURA': 'NAGA MANI MIZO TRIPURA', 'SUB HIMALAYAN WEST BENGAL & SIKKIM': 'SUB HIMALAYAN WEST BENGAL & SIKKIM', 'GANGETIC WEST BENGAL': 'GANGETIC WEST BENGAL', 'ORISSA': 'ORISSA', 'JHARKHAND': 'JHARKHAND', 'BIHAR': 'BIHAR', 'EAST UTTAR PRADESH': 'EAST UTTAR PRADESH', 'WEST UTTAR PRADESH': 'WEST UTTAR PRADESH', 'UTTARAKHAND': 'UTTARAKHAND', 'HARYANA DELHI & CHANDIGARH': 'HARYANA DELHI & CHANDIGARH', 'PUNJAB': 'PUNJAB', 'HIMACHAL PRADESH': 'HIMACHAL PRADESH', 'JAMMU & KASHMIR': 'JAMMU & KASHMIR', 'WEST RAJASTHAN': 'WEST RAJASTHAN', 'EAST RAJASTHAN': 'EAST RAJASTHAN', 'WEST MADHYA PRADESH': 'WEST MADHYA PRADESH', 'EAST MADHYA PRADESH': 'EAST MADHYA PRADESH', 'GUJARAT REGION': 'GUJARAT REGION', 'SAURASHTRA & KUTCH': 'SAURASHTRA & KUTCH', 'KONKAN & GOA': 'KONKAN & GOA', 'MADHYA MAHARASHTRA': 'MADHYA MAHARASHTRA', 'MATATHWADA': 'MATATHWADA', 'VIDARBHA': 'VIDARBHA', 'CHHATTISGARH': 'CHHATTISGARH', 'COASTAL ANDHRA PRADESH': 'COASTAL ANDHRA PRADESH', 'TELANGANA': 'TELANGANA', 'RAYALSEEMA': 'RAYALSEEMA', 'TAMIL NADU': 'TAMIL NADU', 'COASTAL KARNATAKA': 'COASTAL KARNATAKA', 'NORTH INTERIOR KARNATAKA': 'NORTH INTERIOR KARNATAKA', 'SOUTH INTERIOR KARNATAKA': 'SOUTH INTERIOR KARNATAKA', 'KERALA': 'KERALA', 'LAKSHADWEEP': 'LAKSHADWEEP'}, 
            value = 'LAKSHADWEEP', 
            placeholder="Select Your Location",
            style={'color': 'tomato', 'font-size': 16},
            id='state_dropdown'),
            ],style={'display':'inline-block','vertical-align':'top','margin-top':'3vw','margin-left':'3vw'}, className='row'),
        html.Div(children=[
            html.Div(children=[
                html.H4("\nYield Prediction Dataset:"),
                dcc.RadioItems(
                    id="selection_yield",
                    options=[
                        {"label": "District Names", "value": "District_Names"},
                    ],
                    ),
                ], style={'margin-left': '3vw', 'margin-top': '3vw'}),],className="row"),
        dcc.Loading([
            dcc.Graph(id="graph1",style={"background-color": "#f83212"})],
            type="cube",id="loading-graph1"),
        dcc.Loading([
            dcc.Graph(id="graph2",style={"background-color": "#f83212"})],
            type="cube", id="loading-graph2"),
    ],style={"backgroundColor": "#222222"} )

@app.callback(
    Output("graph1", "figure"), 
    Input("selection_rain", "value"),
    Input("state_dropdown","value"),
)
def display_graph_rainfall(value,markdown_val_rainfall):
    print(value)
    animations = {
        'Average Rainfall in Pie Chart': rainfall.makepie('SUBDIVISION','ANNUAL',"All The State Values in the graph"),
        'Average Rainfall in Bar Graph': rainfall.makebar('SUBDIVISION','ANNUAL','States represented in Bar Graph','State','Annual Rainfall(in mm)'),
        'Rainfall Per Month In Each State': rainfall.make_rainfall_bar(markdown_val_rainfall,'Rainfall In ','ANDAMAN & NICOBAR ISLANDS','Annual Rainfall'),
        }
    return animations[value]
@app.callback(
    Output("graph2", "figure"), 
    Input("selection_yield", "value"),
)
def display_graph_yield(value):
    print(value)
    animations = {
        'District_Names': yield_boi.makepie("District_Name","Production","Production Per District"),
    }
    return animations[value]


if __name__ == "__main__":
    app.run_server(port=1121)