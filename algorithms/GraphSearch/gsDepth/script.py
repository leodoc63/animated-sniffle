# Build your depth first function below
def dfs(graph, current_vertex, target_value, visited = None):
    if visited == None:
        visited = []
    visited.append(current_vertex)
    return visited

    if current_vertex == target_value:
        return visited
