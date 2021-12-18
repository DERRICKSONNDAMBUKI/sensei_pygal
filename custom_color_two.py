import pygal
from pygal.style import LightGreenStyle

x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

chart_style = Style() # ricky has bugs
chart_style.colors = [
    '#CCCCCC', '#AAAAAA', '#888888'
]
chart_style.plot_background = '#EEEEEE'
chart = pygal.Line(style=chart_style)

chart.force_url_protocol = 'http'
chart.title = 'Squares and Cubes'
chart.x_labels = x_values

chart.add('Squares', squares)
chart.add('Cubes', cubes)
chart.render_to_file('squares_cubes.svg')
