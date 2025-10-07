import geopandas as gpd
import matplotlib.pyplot as plt

# ---------- BFS Coloring ----------
def get_neighbors(region):
    return borders.get(region, [])

def heuristic_fun(used_colors):
    return len(colors) - len(used_colors)

def greedy_map_coloring_unique(map_graph, colors):
    frontier = []
    start = list(map_graph.keys())[0]

    for color in colors:
        assignment = {start: color}
        used_colors = {color}
        h = heuristic_fun(used_colors)
        frontier.append((h, assignment, used_colors))

    while frontier:
        # Sort by heuristic value and pop the last item (lowest h value)
        frontier.sort(key=lambda x: x[0], reverse=True) 
        h, assignment, used_colors = frontier.pop()

        if len(assignment) == len(map_graph):
            return assignment

        unassigned = [r for r in map_graph if r not in assignment]
        if not unassigned:
            continue
        next_region = unassigned[0]

        for color in colors:
            if color not in used_colors:
                new_assignment = assignment.copy()
                new_assignment[next_region] = color
                new_used_colors = used_colors.copy()
                new_used_colors.add(color)
                new_h = heuristic_fun(new_used_colors)
                frontier.append((new_h, new_assignment, new_used_colors))

    return None

# ---------- تحميل الخريطة ----------
world = gpd.read_file(r"D:\anton\College\2nd Semester\Artificial Intelligence\Tasks\Project\data\ne_110m_admin_0_countries.shp")
africa = world[world['CONTINENT'] == 'Africa']

# ---------- اختيار 10 دول فقط (عينة صغيرة وسريعة)
sample_names = [
    'Egypt', 'Libya', 'Sudan', 'Chad', 'Niger',
    'Algeria', 'Mali', 'Tunisia', 'Eritrea', 'Nigeria'
]
sample_africa = africa[africa['NAME'].isin(sample_names)]

# ---------- بناء الجيران
borders = {}
for idx1, country1 in sample_africa.iterrows():
    neighbors = []
    for idx2, country2 in sample_africa.iterrows():
        if country1['NAME'] != country2['NAME'] and country1['geometry'].touches(country2['geometry']):
            neighbors.append(country2['NAME'])
    borders[country1['NAME']] = neighbors

# ---------- قائمة ألوان بدون تكرار
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'cyan', 'pink', 'brown', 'lime']

# ---------- تنفيذ التلوين
coloring = greedy_map_coloring_unique(borders, colors)

# ---------- عرض الخريطة
fig, ax = plt.subplots(figsize=(10, 10))
for idx, country in sample_africa.iterrows():
    name = country['NAME']
    color = coloring.get(name, 'lightgray')
    gpd.GeoSeries([country['geometry']]).plot(ax=ax, color=color, edgecolor='black')
    ax.annotate(name, xy=(country['geometry'].centroid.x, country['geometry'].centroid.y),
                ha='center', fontsize=7)

plt.title("Map Coloring - Sample 10 African Countries (No Color Repeats)")
plt.axis('off')
plt.show()
    