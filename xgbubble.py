import plotly.graph_objs as go

''' Data up to date as of 1/18/21'''

fig = go.Figure(data=[go.Scatter(
    x=[1.18, 1.13, 1.25, 1.44,
       1.00, 1.46, 1.31, 1.64,
       1.93, 1.21, 1.20, 0.77,
       1.29, 1.52, 1.57, 1.25,
       1.16, 2.12, 1.27, 1.38],
    y=[1.29, 1.96, 1.42, 0.82,
       1.77, 1.00, 1.40, 1.14,
       1.62, 1.57, 1.91, 1.95,
       1.71, 0.98, 1.05, 1.00,
       1.59, 0.67, 1.37, 1.05],
    text=['Arsenal:<br>24 points', 'Aston Villa:<br>26 points', 'Brighton:<br>17 points', 'Burnley:<br>16 points',
          'Chelsea:<br>29 points', 'Crystal Palace:<br>23 points', 'Everton:<br>32 points', 'Fulham:<br>12 points',
          'Leeds:<br>23 points', 'Leicester:<br>35 points', 'Liverpool:<br>34 points', 'Manchester City:<br>35 points',
          'Manchester United:<br>37 points', 'Newcastle:<br>19 points', 'Sheffield:<br>5 points', 'Southampton:<br>29 points',
          'Spurs:<br>33 points', 'West Brom:<br>11 points', 'West Ham:<br>29 points', 'Wolves:<br>22 points',
          ],
    mode='markers',
    marker=dict(
        color=['#EF0107', '#670E36', '#0057B8', '#99D6EA',
               '#034694', '#A7A5A6', '#003399', '#000000',
               '#FFCD00', '#FDBE11', '#C8102E', '#6CABDD',
               '#DA291C', '#241F20', '#0D171A', '#D71920',
               '#132257', '#755031', '#7A263A', '#FDB913'],
        size=[24, 26, 17, 16,
              29, 23, 32, 12,
              23, 35, 34, 35,
              37, 19, 5,  29,
              33, 11, 29, 22],
    )
)])

fig.update_layout(
    title='xG and xGA vs. Actual Performance',
    xaxis=dict(
        title='xGA per game',
        gridcolor='white',
        gridwidth=2,
    ),
    yaxis=dict(
        title='xG per game',
        gridcolor='white',
        gridwidth=2,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
)

fig.show()