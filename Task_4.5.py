def find_all_paths(dic_way, current, final_point, way):
    way = way + [current]
    ways = []

    if current == final_point:
        return [way]

    if not dic_way.get(current):
        return []

    for neighbor in dic_way[current]:
        new_paths = find_all_paths(dic_way, neighbor, final_point, way)
        ways.extend(new_paths)

    return ways


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
path = []

paths = find_all_paths(graph, start, end, path)
print("The number of all paths is", len(paths))
print("All possible paths from point A to point F:", *paths)
