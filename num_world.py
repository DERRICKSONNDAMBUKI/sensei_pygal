# Plotting numerical data on a world map
# To plot numerical data on a map, pass a dictionary to add()
# instead of a list.
from pygal.maps.world import World

populations = {
    'ca': 34126000,
    'us': 309349000,
    'mx': 113423000,
}

wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'Population of North America'
wm.add('North America', populations)
wm.render_to_file('na_populations.svg')

# $ pip install --user pygal_maps_world