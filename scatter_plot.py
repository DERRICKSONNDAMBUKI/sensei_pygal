import pygal
squares = [
    (0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)
]
chart = pygal.XY(stroke=False)
chart.force_uri_protocol = 'http'
chart.add('x^2', squares)
chart.render_to_file('squares_scatter.svg')