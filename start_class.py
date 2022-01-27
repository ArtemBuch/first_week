class PostMan():
    def __init__(self):
        self.all_route = []
        self.path = []
        self.minPath = 999999
        self.minCounter = 0
        self.counter = 0


    def start(self):
        self.input_data()
        self.pre_processing()
        self.processing()
        self.print()


    def input_data(self):
        method = input("Для использования координат из задачи введите 1. Для ввода координат вручную введите 2: ")
        if method == '1':
            self.all_points = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
        elif method == '2':
            self.all_points = []
            tmp = input('Введите сразу все координаты(5 пар) в формате "(0, 1);(1, 4);(4, 1);(5, 5);(7, 2)": ').replace("(", "").replace(")", "").replace(" ", "").split(';')
            for i in tmp:
                self.all_points.append(tuple(map(int, i.split(','))))
        else:
            print('Не понял')


    def pre_processing(self):
        for point_i in range(len(self.all_points)):
            self.all_route.append(list())
            for point_j in range(len(self.all_points)):
                self.all_route[point_i].append(0)
                if point_i != point_j:
                    self.all_route[point_i][point_j] = ((self.all_points[point_j][0] - self.all_points[point_i][0]) ** 2 + (self.all_points[point_j][1] - self.all_points[point_i][1]) ** 2) ** 0.5


    def processing(self):
        i1 = 0
        for i2 in range(len(self.all_points)):
            for i3 in range(len(self.all_points)):
                for i4 in range(len(self.all_points)):
                    for i5 in range(len(self.all_points)):
                        if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i1 != i5) and (i2 != i3) and (i2 != i4) and (i2 != i5) and (i3 != i4) and (i3 != i5) and (i4 != i5):
                            self.path.append(f'{i1+1}{i2 + 1}{i3 + 1}{i4 + 1}{i5 + 1}{i1+1}')
                            if (self.all_route[i1][i2] + self.all_route[i2][i3] + self.all_route[i3][i4] + self.all_route[i4][i5] + self.all_route[i5][i1]) < self.minPath:
                                    self.minPath = self.all_route[i1][i2] + self.all_route[i2][i3] + self.all_route[i3][i4] + self.all_route[i4][i5] + self.all_route[i5][i1]
                                    self.minCounter = self.counter
                            self.counter += 1


    def print(self):
        point__1 = self.all_points[int(self.path[self.minCounter][0]) - 1]
        point__2 = self.all_points[int(self.path[self.minCounter][1]) - 1]
        point__3 = self.all_points[int(self.path[self.minCounter][2]) - 1]
        point__4 = self.all_points[int(self.path[self.minCounter][3]) - 1]
        point__5 = self.all_points[int(self.path[self.minCounter][4]) - 1]

        route_12 = self.all_route[int(self.path[self.minCounter][0]) - 1][int(self.path[self.minCounter][1]) - 1]
        route_23 = self.all_route[int(self.path[self.minCounter][1]) - 1][int(self.path[self.minCounter][2]) - 1] + route_12
        route_34 = self.all_route[int(self.path[self.minCounter][2]) - 1][int(self.path[self.minCounter][3]) - 1] + route_23
        route_45 = self.all_route[int(self.path[self.minCounter][3]) - 1][int(self.path[self.minCounter][4]) - 1] + route_34
        route_51 = self.all_route[int(self.path[self.minCounter][4]) - 1][int(self.path[self.minCounter][5]) - 1] + route_45

        print(f'{point__1} -> {point__2}[{route_12}] -> {point__3}[{route_23}] -> {point__4}[{route_34}] -> {point__5}[{route_45}] -> {point__1}[{route_51}] = {self.minPath}')


if __name__ == "__main__":
    postman = PostMan()
    postman.start()
