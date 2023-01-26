# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 20:25:50 2022

@author: USER
"""

import pandas as pd     #(version 0.24.2)
import numpy as np
import dash             #(version 1.0.0)
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go    
import plotly.express as px
df = pd.read_csv(r"C:\Users\USER\OneDrive\Desktop\Data science\Higher national diploma in data science\vgsales.csv")
dff1= df.iloc[:30,:]
dff3 = df.groupby(['Year','Genre']).agg({'Global_Sales': 'sum','EU_Sales':'sum','JP_Sales':'sum','NA_Sales':'sum'}).reset_index()
dff3['Year']=dff3['Year'].astype('int')
app = dash.Dash(__name__)
app.title='Video Game Sales App'
server = app.server
fig=px.pie(data_frame=dff1, values='Rank', names='Publisher',width=600,color_discrete_sequence=px.colors.qualitative.Prism,
              title='Top 5 publishers',hole=.5,) 
fig.update_layout(legend = dict(font = dict(family = "Open Sans", size = 18, color = "white")),
                  plot_bgcolor='#1f2c56',paper_bgcolor='#1f2c56',
                  titlefont={'color': 'White','size': 30},title_x=0.45,
                  hoverlabel=dict(font_color="white",font_size=16,font_family="Rockwell"))
fig.update_traces(textfont_size=16,textfont_color='white')

app.layout = html.Div([
    html.Div([
        html.H1("The Rise of Gaming Revenue",style={"margin-left": "600px",'display':'flex','font':'Lato','text-align': 'center', 'style':'inline-block', 'color': 'white','font-size': 50}),
        html.Div([html.Img(src=app.get_asset_url('ninja.png'),
                 id='vg-image',
                 style={
                     "height": "150px",
                     "width": "auto",
                     "margin-bottom": "25px",
                     "margin-left": "25px",
                 },),])],style={'display':'flex'}),
   html.Div([
    html.Div([dcc.Graph(id='pie-graph',className='pie_graph', figure=fig, clickData=None,
                      config={'displayModeBar': 'hover',
                          'staticPlot': False,     
                          'scrollZoom': True,      
                          'doubleClick': 'reset',  
                          'showTips': False,       
                            },
                      )],className = 'create_container2 four columns'),
    html.Div([dcc.Graph(id='my-graph',className='bar_graph',config = {'displayModeBar': 'hover'}, figure={},)
            ,],className = 'create_container2 four columns'),
    html.Div([
    html.Div([dcc.Graph(id='graph1',className='scatter_chart'),]),
    html.Div([
        dcc.RadioItems(id='radioin',className='fix_label2', options=[
         {'label': 'North America', 'value': 'NA_Sales'},
         {'label': 'Europe', 'value': 'EU_Sales'},
         {'label': 'Japan', 'value': 'JP_Sales'}
     ],
        style = {"margin-left": "75px",'display':'flex','fontSize': 20,'margin-top':'25px','font-size': 20,'text-align': 'center', 'color': 'white'},
        value='px'),]),],className = 'create_container2 five columns'),],style={'display':'flex'}),
    html.Div([
    html.Div([
        html.Div([
            html.P('Select Genre', className = 'fix_label', style = {'fontSize': 20,'color': 'white', 'margin-top': '25px'}),
            dcc.Dropdown(id = 'select_genre',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'fontSize': 18,'display':'inline-block','width':'50%','color': '#333333'},
                         value = 'Action',
                         placeholder = 'Select Countries',
                         options = [{'label': c, 'value': c} for c in (df['Genre'].unique())], className = 'dcc_compon'),]),
    html.Div([
            html.P('Select Platform', className = 'fix_label', style = {'fontSize': 20,'color': 'white','margin-top': '2px'}),
            dcc.RadioItems(id = 'radio_items',
                           labelStyle = {"display": "inline-block","color":"white"},
                           options = [],
                           style = {'color': 'white'}),]),
    html.Div([dcc.Graph(id = 'scatter_chart', className='bubble_chart',
              config = {'displayModeBar': 'hover'})])],className = 'create_container2 two columns'),
    html.Div([
        html.Div([
            html.P('Select Sales', className = 'fix_label1', style = {'fontSize': 20,'color': 'white'}),
            dcc.Dropdown(id='my_dropdown',
                options=[
                         {'label':'Global Sales', 'value':'Global_Sales'},
                         {'label':'European Sales', 'value':'EU_Sales'},
                         {'label':'North America Sales', 'value':'NA_Sales'},
                         {'label':'Japan Sales', 'value':'JP_Sales'}
                ],
                optionHeight=35,                    #height/space between dropdown options
                value='Global_Sales',               #dropdown value selected automatically when page loads
                disabled=False,                     #disable dropdown value selection
                multi=False,                        #allow multiple dropdown values to be selected
                searchable=True,                    #allow user-searching of dropdown values
                search_value='',                    #remembers the value searched in dropdown
                placeholder='Please select...',     #gray, default text shown when no option is selected
                clearable=True,                     #allow user to removes the selected value
                style={'fontSize': 18,'color': 'black','width':'50%','display':'inline-block'},
                )]),
            html.Div(children=[html.P('Select Year Range', className = 'fix_label1', style = {'display':'inline-block','fontSize': 20,'color': 'white'}),
                      dcc.RangeSlider(
                          id='year-slider', # any name you'd like to give it
                          marks= { str(Year) : str(Year) for Year in df['Year'].unique()},
                          step=1,                # number of steps between values
                          min=1980,
                          max=2017,
                          value=[1980,2017],     # default value initially chosen
                          dots=True,             # True, False - insert dots1
                          allowCross=False,      # True,False - Manage handle crossover
                          disabled=False,        # True,False - disable handle
                          pushable=2,            # any number, or True with multiple handles
                          updatemode='drag',     # 'mouseup', 'drag' - update value method
                          included=True,         # True, False - highlight handle
                          vertical=False,        # True, False - vertical, horizontal slider
                          verticalHeight=900,    # hight of slider (pixels) when vertical=True
                          tooltip={'always_visible':False,  # show current slider values
                         'placement':'bottom'},),
                      ],style = {'color': 'white','width':'100%','display':'inline-block'}),
          html.Div([dcc.Graph(id='our_graph', className='line_chart',
                        config = {'displayModeBar': 'hover'}),
             
              ],style={'display':'flex'}),],className = 'create_container2 three columns'),],style={'display':'flex'},),
    html.Div([html.H6(children='Dash App created by : Shalini Balakrishnan COHNDDSFT211F-006',
            style={
                'textAlign': 'right',
                'color': 'white',
                'fontSize': 20,}
            ),]),])


@app.callback(
    Output('radio_items', 'options'),
    [Input('select_genre', 'value')])
def get_platform_options(select_genre):
    df1 = df[df['Genre'] == select_genre]
    return [{'label': k, 'value': k} for k in df1['Platform'].unique()]

@app.callback(
    Output('radio_items', 'value'),
    [Input('radio_items', 'options')])
def get_platform_value(radio_items):
    return [k['value'] for k in radio_items][0]
@app.callback(Output('scatter_chart', 'figure'),
              [Input('select_genre', 'value')],
              [Input('radio_items', 'value')])
def update_graph(select_genre, radio_items):
    df2 = df.groupby(['Platform', 'Genre', 'Publisher'])['Global_Sales'].sum().reset_index()
    df3 = df2[(df2['Genre'] == select_genre) & (df2['Platform'] == radio_items)]
    return {
        'data':[go.Scatter(
                    x=df3['Publisher'],
                    y=df3['Global_Sales'],
                    mode = 'markers',
                    marker = dict(
                        size = 20,
                        color = df3['Global_Sales'],
                        colorscale = 'HSV',
                        showscale = False,
                        line = dict(
                            color = 'MediumPurple',
                            width = 2
                        )),
                    hoverinfo='text',
                    hovertext=
                    '<b>Genre</b>: ' + df3['Genre'].astype(str) + '<br>' +
                    '<b>Platform</b>: ' + df3['Platform'] + '<br>' +
                    '<b>Publisher</b>: ' + df3['Publisher'].astype(str) + '<br>' +
                    '<b>Global Sales</b>: $' + [f'{x:,.2f}' for x in df3['Global_Sales']] + 'million <br>'
              )],
        'layout': go.Layout(
             plot_bgcolor=' #1f2c56',
             paper_bgcolor=' #1f2c56',
             height=700,
             title={
                'text': f'Global Sales of {radio_items}',

                'y': 0.96,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
             titlefont={
                        'color': 'White',
                        'size': 30},

             hovermode='x',
             margin = dict(b = 160),
             xaxis=dict(title='<b></b>',
                        color='white',
                        showline=True,
                        showgrid=False,
                        linecolor='white',
                        linewidth=1,
                ),
             yaxis=dict(title='<b>Global Sales</b>',
                        titlefont={
                                   'color': 'White',
                                   'size': 20},
                        showline=False,
                        showgrid=True,
                        linecolor='white',),
            legend = {
                'orientation': 'h',
                'bgcolor': '#010915',
                'x': 0.5,
                'y': 1.25,
                'xanchor': 'center',
                'yanchor': 'top'},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'white',
                 )
        )

    }

@app.callback(Output(component_id='our_graph', component_property='figure'),
              [Input(component_id='year-slider',component_property='value'),
              Input(component_id='my_dropdown', component_property='value')])    

def build_graph(year_range,column_chosen):
    dff4=dff3[(dff3['Year']>=year_range[0])&(dff3['Year']<=year_range[1])]
    if column_chosen == 'Global_Sales':
        fig = px.line(dff4, x='Year', y="Global_Sales",color='Genre',markers=True,
                      color_discrete_sequence=px.colors.qualitative.Dark2,height=700,
                      labels=dict(year="Year", Global_Sales="Global Sales"),
                      title=f'Global Sales Trend of Video games by {year_range}')
        fig.update_layout(legend = dict(font = dict(family = "Open Sans", size = 20, color = "white")),
                          plot_bgcolor='#1f2c56',paper_bgcolor='#1f2c56',
                          titlefont={'color': 'White','size': 24},title_x=0.5,
                          hoverlabel=dict(font_color="white",font_size=16,font_family="Rockwell"))
        fig.update_xaxes(title_font=dict(size=20, color='white'),color='white',gridcolor='#1f2c56')
        fig.update_yaxes(title_font=dict(size=20, color='white'),color='white',gridcolor='gray')
    elif column_chosen == 'EU_Sales':       
        fig = px.line(dff4, x='Year', y="EU_Sales",color='Genre',markers=True,
                      color_discrete_sequence=px.colors.qualitative.Dark2,height=700,
                      labels=dict(year="Year", EU_Sales="Europe Sales"),
                      title=f'Europe Sales Trend of Video games by {year_range}')
        fig.update_layout(legend = dict(font = dict(family = "Open Sans", size = 20, color = "white")),
                          plot_bgcolor='#1f2c56',paper_bgcolor='#1f2c56',
                          titlefont={'color': 'White','size': 24},title_x=0.5,
                          hoverlabel=dict(font_color="white",font_size=16,font_family="Rockwell"))
        fig.update_xaxes(title_font=dict(size=20, color='white'),color='white',gridcolor='#1f2c56')
        fig.update_yaxes(title_font=dict(size=20, color='white'),color='white',gridcolor='gray')
    elif column_chosen == 'NA_Sales':
        fig = px.line(dff4, x='Year', y="NA_Sales",color='Genre',markers=True,
                      color_discrete_sequence=px.colors.qualitative.Dark2,height=700,
                      labels=dict(year="Year", NA_Sales="North America Sales"),
                      title=f'North America Sales Trend of Video games by {year_range}')
        fig.update_layout(legend = dict(font = dict(family = "Open Sans", size = 20, color = "white")),
                          plot_bgcolor='#1f2c56',paper_bgcolor='#1f2c56',
                          titlefont={'color': 'White','size': 22},title_x=0.5,
                          hoverlabel=dict(font_color="white",font_size=16,font_family="Rockwell"))
        fig.update_xaxes(title_font=dict(size=20, color='white'),color='white',gridcolor='#1f2c56')
        fig.update_yaxes(title_font=dict(size=20, color='white'),color='white',gridcolor='gray')
    else:
        fig = px.line(dff4, x='Year', y="JP_Sales",color='Genre',markers=True,
                      color_discrete_sequence=px.colors.qualitative.Dark2,height=700,
                      labels=dict(year="Year", JP_Sales="Japan Sales"),
                      title=f'Japan Sales Trend of Video games by {year_range}')
        fig.update_layout(legend = dict(font = dict(family = "Open Sans", size = 20, color = "white")),
                         plot_bgcolor='#1f2c56',paper_bgcolor='#1f2c56',
                         titlefont={'color': 'White','size': 24},title_x=0.5,
                         hoverlabel=dict(font_color="white",font_size=16,font_family="Rockwell"))
        fig.update_xaxes(title_font=dict(size=20, color='white'),color='white',gridcolor='#1f2c56')
        fig.update_yaxes(title_font=dict(size=20, color='white'),color='white',gridcolor='gray')
    return fig

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='pie-graph', component_property='clickData')
)


def update_side_graph(clck_data):
    if clck_data is None:
        dff2 = dff1[dff1.Publisher == 'Nintendo']
        print(dff2)
        fig2 = px.bar(data_frame=dff2, x='Rank', y='Name',text="Rank",title='Top users picks by publishers on all years',
                           color='Platform',color_discrete_sequence=px.colors.qualitative.Prism,orientation='h')
        fig2.update_layout(legend = dict(font = dict(family = "Open Sans", size = 18, color = "white")),
                          plot_bgcolor='#1f2c56',paper_bgcolor='#1f2c56',
                          titlefont={'color': 'White','size': 30},title_x=0.5,
                          hoverlabel=dict(font_color="white",font_size=16,font_family="Rockwell"))
        fig2.update_xaxes(title_font=dict(size=16, color='white'),color='white')
        fig2.update_yaxes(title_font=dict(size=16, color='white'),color='white')
        return fig2
    else:
        print(f'click data: {clck_data}')
        publisher = clck_data['points'][0]['label']
        dff2 = dff1[dff1.Publisher == publisher]
        fig2 = px.bar(data_frame=dff2, x='Rank', y='Name',text="Rank",title=f'Top users picks for {publisher}',
                           color='Platform',color_discrete_sequence=px.colors.qualitative.Prism,orientation='h')
        fig2.update_layout(legend = dict(font = dict(family = "Open Sans", size = 18, color = "white")),
                          plot_bgcolor='#1f2c56',paper_bgcolor='#1f2c56',
                          titlefont={'color': 'White','size': 30},title_x=0.5,
                          hoverlabel=dict(font_color="white",font_size=16,font_family="Rockwell"))
        fig2.update_xaxes(title_font=dict(size=16, color='white'),color='white')
        fig2.update_yaxes(title_font=dict(size=16, color='white'),color='white')
        return fig2

@app.callback(
  Output('graph1', 'figure'),
  Input('radioin', 'value'))
def update_graph(val):
  if val == 'NA_Sales':
      fig = px.scatter(df, x="Global_Sales", y="NA_Sales",color='NA_Sales',title='Global Sales vs North America Sales',width=450,)
      fig.update_layout(legend = dict(font = dict(family = "Open Sans", size = 18, color = "white")),
                       plot_bgcolor='#1f2c56',paper_bgcolor='#1f2c56',
                       titlefont={'color': 'White','size': 24},title_x=0.5,
                       hoverlabel=dict(font_color="white",font_size=16,font_family="Rockwell"))
      fig.update_xaxes(range=[0, 50],title_text="Global Sales",
                       title_font=dict(size=16, color='white'),color='white',gridcolor='#1f2c56')
      fig.update_yaxes(title_text="North America Sales",
                       title_font=dict(size=16, color='white'),color='white',gridcolor='#1f2c56')
  elif val =='EU_Sales':
      fig = px.scatter(df, x="Global_Sales", y="EU_Sales",color='EU_Sales',title='Global Sales vs Europe Sales',width=450,)
      fig.update_layout(legend = dict(font = dict(family = "Open Sans", size = 18, color = "white")),
                       plot_bgcolor='#1f2c56',paper_bgcolor='#1f2c56',
                       titlefont={'color': 'White','size': 24},title_x=0.5,
                       hoverlabel=dict(font_color="white",font_size=16,font_family="Rockwell"))
      fig.update_xaxes(range=[0, 50],title_text="Global Sales",
                       title_font=dict(size=16, color='white'),color='white',gridcolor='#1f2c56')
      fig.update_yaxes(title_text="Europe Sales",
                       title_font=dict(size=16, color='white'),color='white',gridcolor='#1f2c56')
  else:
      fig = px.scatter(df, x="Global_Sales", y="JP_Sales",color='JP_Sales',title='Global Sales vs Japan Sales',width=450,)
      fig.update_layout(legend = dict(font = dict(family = "Open Sans", size = 18, color = "white")),
                       plot_bgcolor='#1f2c56',paper_bgcolor='#1f2c56',
                       titlefont={'color': 'White','size': 24},title_x=0.5,
                       hoverlabel=dict(font_color="white",font_size=16,font_family="Rockwell"))
      fig.update_xaxes(range=[0, 50],title_text="Global Sales",
                       title_font=dict(size=16, color='white'),color='white',gridcolor='#1f2c56')
      fig.update_yaxes(title_text="Japan Sales",
                       title_font=dict(size=16, color='white'),color='white',gridcolor='#1f2c56')
  return fig


app.run_server()
