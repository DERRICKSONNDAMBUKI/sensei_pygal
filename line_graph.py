import pygal
# To make a plot with Pygal, you specify the kind of plot and
# then add the data.
# Making a line graph
# To view the output, open the file squares.svg in a browser.

x_values = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4, 9, 16, 25]

chart = pygal.Line()
chart.force_url_protocol = 'http'
chart.title = 'squares'
chart.x_labels = x_values
chart.x_title = 'Value'
chart.y_title = 'Square of Value'
chart.add('x^2', squares)
chart.render_to_file('squares_line.svg')