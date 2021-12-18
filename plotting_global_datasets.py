# Plotting global datasets

# Pygal can generate world maps, and you can add any data
# you want to these maps. Data is indicated by coloring, by
# labels, and by tooltips that show data when users hover
# over each country on the map.
# Installing the world map module
# The world map module is not included by default in Pygal 2.0. It
# can be installed with pip:
# $ pip install --user pygal_maps_world

# Making a world map
# The following code makes a simple world map showing the
# countries of North America.

from pygal.maps.world import World
wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'North America'
wm.add('North America', [
    'ca', 'mx', 'us'
])
wm.render_to_file('north_america.svg')
# ricky has bugs - solve - $ pip install --user pygal_maps_world
