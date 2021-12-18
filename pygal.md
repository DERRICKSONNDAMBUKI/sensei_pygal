What is Pygal
Data visualization involves exploring data through
visual representations. Pygal helps you make visually
appealing representations of the data you’re working
with. Pygal is particularly well suited for visualizations
that will be presented online, because it supports
interactive elements.
squares = [
(0, 0), (1, 1), (2, 4), (3, 9),
(4, 16), (5, 25),
]
chart = pygal.XY(stroke=False)
chart.force_uri_protocol = 'http'
chart.add('x^2', squares)
chart.render_to_file('squares.svg')
Using a list comprehension for a scatter plot

Install Pygal
Pygal can be installed using pip.
Pygal on Linux and OS X
$ pip install --user pygal
Pygal on Windows
> python –m pip install --user pygal