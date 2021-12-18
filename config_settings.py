
import pygal
from pygal.style import LightGreenStyle

x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

# Configuration settings
# Some settings are controlled by a Config object.
my_config = pygal.Config()
my_config.show_y_guides = False
my_config.width = 1000
my_config.dots_size = 5
chart = pygal.Line(config=my_config)

chart.force_url_protocol = 'http'
chart.title = 'Squares and Cubes'
chart.x_labels = x_values

# Styling series
# You can give each series on a chart different style settings.
chart.add('Squares', squares, dots_size=2)
chart.add('Cubes', cubes, dots_size=3)

# chart.add('Squares', squares)
# chart.add('Cubes', cubes)
chart.render_to_file('config_style.svg')
