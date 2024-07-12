import folium
from folium.plugins import MarkerCluster, Search

# Create a map centered on the continental U.S.
m = folium.Map(location=[37.1, -95.7], zoom_start=4, control_scale=True)

# Add the Stamen Terrain tile layer with attribution
folium.TileLayer(
    tiles='Stamen Terrain',
    attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.',
    name='Stamen Terrain',
    overlay=True,
    control=True
).add_to(m)

# Add an additional tile layer (e.g., OpenStreetMap)
folium.TileLayer(
    tiles='OpenStreetMap',
    attr='Map tiles by OpenStreetMap contributors',
    name='OpenStreetMap',
    overlay=True,
    control=True
).add_to(m)

# List of locations (latitude, longitude, name, image URL)
locations = [
    (40.7128, -74.0060, 'New York City, NY', 'https://example.com/nyc.jpg'),
    (34.0522, -118.2437, 'Los Angeles, CA', 'https://example.com/la.jpg'),
    (41.8781, -87.6298, 'Chicago, IL', 'https://example.com/chicago.jpg'),
    (29.7604, -95.3698, 'Houston, TX', 'https://example.com/houston.jpg'),
    (33.4484, -112.0740, 'Phoenix, AZ', 'https://example.com/phoenix.jpg'),
    (37.7749, -122.4194, 'San Francisco, CA', 'https://example.com/sf.jpg'),
    (47.6062, -122.3321, 'Seattle, WA', 'https://example.com/seattle.jpg'),
    (38.9072, -77.0369, 'Washington, D.C.', 'https://example.com/wdc.jpg'),
    (25.7617, -80.1918, 'Miami, FL', 'https://example.com/miami.jpg'),
    (37.3318, -122.0312, 'San Jose, CA', 'https://example.com/sanjose.jpg'),
    (38.4405, -82.4456, 'Charleston, WV', 'https://example.com/charleston.jpg'),
    (39.7392, -104.9903, 'Denver, CO', 'https://example.com/denver.jpg'),
    (30.2672, -97.7431, 'Austin, TX', 'https://example.com/austin.jpg'),
    (38.2527, -85.7585, 'Louisville, KY', 'https://example.com/louisville.jpg'),
    (44.9778, -93.2650, 'Minneapolis, MN', 'https://example.com/minneapolis.jpg'),
    (39.9612, -82.9988, 'Columbus, OH', 'https://example.com/columbus.jpg'),
    (36.1699, -115.1398, 'Las Vegas, NV', 'https://example.com/vegas.jpg'),
    (42.3601, -71.0589, 'Boston, MA', 'https://example.com/boston.jpg'),
    (39.7684, -86.1581, 'Indianapolis, IN', 'https://example.com/indianapolis.jpg'),
    (47.4419, -122.3151, 'Tacoma, WA', 'https://example.com/tacoma.jpg'),
    (32.7157, -117.1611, 'San Diego, CA', 'https://example.com/sandiego.jpg'),
    (24.5854, -81.3496, 'Key West, FL', 'https://example.com/keywest.jpg'),
    (41.5868, -93.6250, 'Des Moines, IA', 'https://example.com/desmoines.jpg'),
]
# New York City Boroughs
boroughs = [
    (40.6501, -73.9496, 'Brooklyn', 'https://example.com/brooklyn.jpg', 'Known for its cultural diversity and landmarks.'),
    (40.7033, -73.9797, 'Queens', 'https://example.com/queens.jpg', 'Famous for its ethnic communities and cuisine.'),
    (40.7831, -73.9712, 'Manhattan', 'https://example.com/manhattan.jpg', 'The heart of NYC with iconic skyline and Central Park.'),
    (40.5795, -74.1519, 'Staten Island', 'https://example.com/statenisland.jpg', 'Known for its ferry and suburban atmosphere.'),
    (40.8448, -73.8654, 'The Bronx', 'https://example.com/bronx.jpg', 'Birthplace of hip hop and home to the Bronx Zoo.')
]
# Create a MarkerCluster
marker_cluster = MarkerCluster().add_to(m)

# Add markers for each location with custom icons and more detailed popups
for lat, lon, name, img_url in locations:
    popup_content = f"<b>{name}</b><br><img src='{img_url}' width='200'><br><p>Explore this vibrant city!</p>"
    folium.Marker(
        location=[lat, lon],
        popup=popup_content,
        tooltip='Click for info',
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(marker_cluster)

# Add search functionality
search = Search(
    layer=marker_cluster,
    search_label='name',
    placeholder='Search for a city...',
    collapsed=False
).add_to(m)

# Add a polyline between two cities (e.g., New York City to Los Angeles)
folium.PolyLine(locations=[(40.7128, -74.0060), (34.0522, -118.2437)], color='red', weight=2.5, opacity=1, dash_array='5, 5').add_to(m)

# Add a marker for a notable landmark (e.g., Statue of Liberty)
folium.Marker(
    location=[40.6892, -74.0445],
    popup='<b>Statue of Liberty</b><br><img src="https://example.com/statue.jpg" width="200">',
    icon=folium.Icon(color='green', icon='tree')
).add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

# Save the map to an HTML file
m.save('enhanced_us_cities_map.html')

print("Map has been saved as 'enhanced_us_cities_map.html'")
