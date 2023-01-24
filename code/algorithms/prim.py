from code.algorithms import nearest, randomise

def prim(batteries, houses):
    nearest.assign(batteries, houses)
    for battery in batteries:
        results = []
        n = len(battery.houses) + 1
        points = [battery] + battery.houses
        visited = [0] * n
        visited[0] = True
        for _ in range(n - 1):
            min_edge = [None, None, float('inf')]
            for i in range(n):
                if visited[i]:
                    for j in range(n):
                        if not visited[j]:
                            distance = abs(points[i].pos_x - points[j].pos_x) + abs(points[i].pos_y - points[j].pos_y)
                            if distance < min_edge[2]:
                                min_edge = [i, j, distance]
            results.append(min_edge)
            visited[min_edge[1]] = True
        for result in results:
            try:
                if len(points[result[0]].cables) == 0:
                    points[result[0]].lay_cable(points[result[1]].pos_x, points[result[1]].pos_y)
                else:
                    points[result[1]].lay_cable(points[result[0]].pos_x, points[result[0]].pos_y)

            except:
                points[result[1]].lay_cable(points[result[0]].pos_x, points[result[0]].pos_y)
