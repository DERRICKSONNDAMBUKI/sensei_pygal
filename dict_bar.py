# Making a bar graph from a dictionary
# Since each bar needs a label and a value, a dictionary is a great
# way to store the data for a bar graph. The keys are used as the
# labels along the x-axis, and the values are used to determine the
# height of each bar.
import pygal
results = {
    1: 18, 2: 16, 3: 18,
    4: 17, 5: 18, 6: 13,
}
chart = pygal.Bar()
chart.force_uri_protocol = 'http'
chart.x_labels = results.keys()
chart.add('D6', results.values())
chart.render_to_file('rolling_dice_dict.svg')
