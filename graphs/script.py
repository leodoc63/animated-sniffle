#import Vertex below....
from vertex import Vertex

#import Graph below...
from graph import Graph

#Make the Graph instance here
railway = Graph()

#Make the Vertex instance here
station_one = Vertex("Ballahoo")
station_two = Vertex("Penn")

#Call .add_vertex() here
railway.add_vertex(station_one)
railway.add_vertex(station_two)

#Call .add_edge() here
railway.add_edge(station_one, station_two)
print("Edges for {0}: {1}".format(station_one.value, station_one.get_edges()))
print("Edges for {0}: {1}".format(station_two.value, station_two.get_edges()))
