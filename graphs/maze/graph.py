from vertex import Vertex

class Graph:
  def __init__(self):
    self.graph_dict = {}

  def add_vertex(self, node):
    self.graph_dict[node.value] = node

  def add_edge(self, from_node, to_node, weight = 0):
    self.graph_dict[from_node.value].add_edge(to_node.value, weight)
    self.graph_dict[to_node.value].add_edge(from_node.value, weight)

  def explore(self):
    print("Exploring the graph....\n")
    #FILL IN EXPLORE METHOD BELOW
    
  
  def print_map(self):
    print("\nMAZE LAYOUT\n")
    for node_key in self.graph_dict:
      print("{0} connected to...".format(node_key))
      node = self.graph_dict[node_key]
      for adjacent_node, weight in node.edges.items():
        print("=> {0}: cost is {1}".format(adjacent_node, weight))
      print("")
    print("")

def build_graph():
  graph = Graph()
  
  # MAKE ROOMS INTO VERTICES BELOW...
  entrance = Vertex("entrance")
  ante_chamber = Vertex("ante-chamber")
  kings_room = Vertex("King's Room")
  

  # ADD ROOMS TO GRAPH BELOW...
  graph.add_vertex(entrance)
  graph.add_vertex(ante_chamber)
  graph.add_vertex(kings_room)
  

  # ADD EDGES BETWEEN ROOMS BELOW...
  graph.add_edge(entrance, ante_chamber, 7)
  graph.add_edge(entrance, kings_room, 3)
  graph.add_edge(ante_chamber, kings_room, 1)
  

  # DON'T CHANGE THIS CODE
  graph.print_map()
  return graph

    



