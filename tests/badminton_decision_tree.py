# Demo of creating the badminton decision tree in the `tests/static` directory. 

from treeplotter.tree import Node, Tree
from treeplotter.plotter import create_tree_diagram

weather_node = Node(name="Weather")
option_sunny = Node(name="Sunny")
option_cloudy = Node(name="Cloudy")
option_rainy = Node(name="Rainy")

weather_node.add_children([option_sunny, option_rainy, option_cloudy])

cloud_play = Node(name="Yes")
option_cloudy.add_child(cloud_play)

# #### Sunny path
humidity_node = Node(name="Humidity")
wind_node = Node(name="Wind")

option_sunny.add_child(humidity_node)
option_rainy.add_child(wind_node)

humidity_high = Node(name="High")
humidity_normal = Node(name="Normal")
humidity_node.add_children([humidity_high, humidity_normal])

humidity_no = Node(name="No")
humidity_yes = Node(name="Yes")
humidity_high.add_child(humidity_no)
humidity_normal.add_child(humidity_yes)

# #### Rainy path
wind_strong = Node("Strong")
wind_weak = Node("Weak")
wind_node.add_children([wind_strong, wind_weak])

strong_no = Node("No")
weak_yes = Node("Yes")
wind_strong.add_child(strong_no)
wind_weak.add_child(weak_yes)

BADMINTON_DECISION_TREE = Tree(root=weather_node)
create_tree_diagram(
    BADMINTON_DECISION_TREE,
    "/Users/lukepoeppel/treeplotter/tests/badminton",
    verbose=True
)
