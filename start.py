all_points = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
all_route = []
path = []
minPath = 999999
minCounter = 0
counter = 0

for point_i in range(len(all_points)):
    all_route.append(list())
    for point_j in range(len(all_points)):
        all_route[point_i].append(0)
        if point_i != point_j:
            all_route[point_i][point_j] = ((all_points[point_j][0] - all_points[point_i][0]) ** 2 + (all_points[point_j][1] - all_points[point_i][1]) ** 2) ** 0.5

i1 = 0
for i2 in range(len(all_points)):
    for i3 in range(len(all_points)):
        for i4 in range(len(all_points)):
            for i5 in range(len(all_points)):
                if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i1 != i5) and (i2 != i3) and (i2 != i4) and (i2 != i5) and (i3 != i4) and (i3 != i5) and (i4 != i5):
                    path.append(f'{i1+1}{i2 + 1}{i3 + 1}{i4 + 1}{i5 + 1}{i1+1}')
                    if (all_route[i1][i2] + all_route[i2][i3] + all_route[i3][i4] + all_route[i4][i5] + all_route[i5][i1]) < minPath:
                            minPath = all_route[i1][i2] + all_route[i2][i3] + all_route[i3][i4] + all_route[i4][i5] + all_route[i5][i1]
                            minCounter = counter
                    counter += 1

point__1 = all_points[int(path[minCounter][0]) - 1]
point__2 = all_points[int(path[minCounter][1]) - 1]
point__3 = all_points[int(path[minCounter][2]) - 1]
point__4 = all_points[int(path[minCounter][3]) - 1]
point__5 = all_points[int(path[minCounter][4]) - 1]

route_12 = all_route[int(path[minCounter][0]) - 1][int(path[minCounter][1]) - 1]
route_23 = all_route[int(path[minCounter][1]) - 1][int(path[minCounter][2]) - 1] + route_12
route_34 = all_route[int(path[minCounter][2]) - 1][int(path[minCounter][3]) - 1] + route_23
route_45 = all_route[int(path[minCounter][3]) - 1][int(path[minCounter][4]) - 1] + route_34
route_51 = all_route[int(path[minCounter][4]) - 1][int(path[minCounter][5]) - 1] + route_45

print(f'{point__1} -> {point__2}[{route_12}] -> {point__3}[{route_23}] -> {point__4}[{route_34}] -> {point__5}[{route_45}] -> {point__1}[{route_51}] = {minPath}')
