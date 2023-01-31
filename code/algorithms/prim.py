from code.algorithms import nearest, randomise
import random

def prim(batteries, houses):
    nearest.assign(batteries, houses)
    for battery in batteries:
        results = []
        points = battery.houses
        points = [battery] + points
        visited = [0] * len(points)
        visited[0] = True

        # run until there are n-1 edges
        for _ in range(len(points) - 1):
            min_edge = [None, None, float('inf')]

            # check distance between current point and every other point
            for i in range(len(points)):
                if visited[i]:

                    # checks if distance between points is smallest
                    for j in range(len(points)):
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
