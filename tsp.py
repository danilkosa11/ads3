import random
import string


def print_list():
    for row in empty_list:
        for value in row:
            print('{:3}'.format(value), '', end=' ')
        print()


def print_table(list):
    print()
    array = [[0 for j in range(number_of_cities+1)] for i in range(number_of_cities+1)]
    for value in range(number_of_cities + 1):
        if value > 0:
            array[0][value] = alphabet[value - 1]
            array[value][0] = alphabet[value - 1]

    for j in range(number_of_cities):
        for i in range(number_of_cities):
            array[j+1][i+1] = list[j][i]

    for row in array:
        for value in row:
            print('{:3}'.format(value), '', end=' ')
        print()
    print()


def euclidean_distance(x1, y1, x2, y2):
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return round(distance)


def fill_list():
    for y in range(1, number_of_cities + 1):
        for x in range(1, number_of_cities + 1):
            x1 = thisdict[alphabet[x - 1]][0]
            y1 = thisdict[alphabet[x - 1]][1]
            x2 = thisdict[alphabet[y - 1]][0]
            y2 = thisdict[alphabet[y - 1]][1]
            empty_list[y][x] = euclidean_distance(x1, y1, x2, y2)


def fill_list_letters():
    for value in range(number_of_cities + 1):
        if value > 0:
            empty_list[0][value] = alphabet[value - 1]

    for value in range(number_of_cities + 1):
        if value > 0:
            empty_list[value][0] = alphabet[value - 1]


def modify_list():
    for row in empty_list:
        for value in row:
            if type(value) == int:
                table_of_values.append(value)
    change = 0
    while (change == 0):
        index = random.randrange(len(table_of_values))
        change = table_of_values[index]
    for y in range(1, number_of_cities + 1):
        for x in range(1, number_of_cities + 1):
            if empty_list[y][x] == change:
                empty_list[y][x] = "X"
    for row in empty_list:
        for value in row:
            if type(value) == int:
                table_of_values.append(value)
    empty_list.pop(0)


def spawn_arrays():
    new = [[0 for j in range(number_of_cities)] for i in range(number_of_cities)]
    for row in range(number_of_cities):
        for value in range(number_of_cities):
            if (values[row][value] == "X"):
                new[row][value] = 123
            else:
                new[row][value] = values[row][value]
    return new
alphabet = string.ascii_uppercase
number_of_cities = 4
thisdict = {}
literki = {}

for x in range(0, number_of_cities):
    thisdict[alphabet[x]] = [random.randint(-100, 100), random.randint(-100, 100)]
    literki[alphabet[x]] = x


def print_dict():
    for key in thisdict:
        print(key, " : ", thisdict[key])
    print()


empty_list = [[0 for j in range(number_of_cities + 1)] for i in range(number_of_cities + 1)]
table_of_values = []

fill_list_letters()

print()
fill_list()
modify_list()


values = [[0 for j in range(number_of_cities)] for i in range(number_of_cities)]
for row in range(number_of_cities):
    for value in range(number_of_cities):
        values[row][value] = empty_list[row][value + 1]

#####################################
stany = []


def calculate_way(array, data):
    min_cost = 2341
    min_way = 'ABCDA'
    for droga in array:
        suma = 0
        for x in range(len(droga) - 1):
            first = droga[x]
            second = droga[x + 1]
            value_first = literki[first]
            value_second = literki[second]
            distance = data[value_first][value_second]
            suma += distance
        if suma < min_cost:
            min_cost = suma
            min_way = droga
    return min_cost, min_way


def index_2d(v):
    for i, x in enumerate(values):
        if v in x:
            return i, x.index(v)


def no_ways():
    x, y = index_2d("X")
    x = alphabet[x]
    y = alphabet[y]
    string = x + y
    string_reversed = y + x
    return string, string_reversed


def chaeck_if(all_ways):
    way1, way2 = no_ways()
    wrong_ways = []
    for stan in all_ways:
        if way1 in stan or way2 in stan:
            wrong_ways.append(stan)
    new_array = []
    for way in all_ways:
        if (way in wrong_ways):
            continue
        else:
            new_array.append(way)
    return new_array


def BFS():
    print_table(values)
    stany.append("A")
    all_cities = [[0 for j in range(number_of_cities)] for i in range(number_of_cities)]
    for city in range(number_of_cities):
        all_cities[city] = alphabet[city]
    for stan in stany:
        for city in all_cities:
            string = str(stan)
            city = str(city)
            if (city in string):
                continue
            else:
                stany.append(string + str(city))


    all_ways = []
    for x in stany:
        if len(x) == number_of_cities:
            y = str(x) + "A"
            all_ways.append(y)
        else:
            all_ways.append(x)

    final_array = chaeck_if(all_ways)
    print(final_array)
    temp_stany = []
    for x in final_array:
        if len(x) == number_of_cities + 1:
            temp_stany.append(x)


    stany.clear()

    min_cost, min_way = calculate_way(temp_stany, values)
    print(min_cost, min_way)


def greedy():
    new = spawn_arrays()
    print_table(new)

    all_cities = [[0 for j in range(number_of_cities)] for i in range(number_of_cities)]
    for city in range(number_of_cities):
        all_cities[city] = alphabet[city]
    ways = ['A']
    for i in range(number_of_cities - 1):
        for city in all_cities:
            string = str(ways[0])
            city = str(city)
            if city in string:
                continue
            else:
                ways.append(string + str(city))
        print(ways)

        ways.pop(0)

        min_value, min_way = calculate_way(ways, new)

        new_array = []
        for way in ways:
            if way == min_way:
                new_array.append(way)
        ways.clear()
        ways = new_array

    final_way = []
    for x in ways:
        y = str(x) + "A"
        final_way.append(y)

    bfs_value, bfs_way = calculate_way(final_way, new)
    print()
    print(bfs_value, bfs_way)


def stack_display(stack):
    for val in stack:
        x = alphabet[val]
        print(x, end='|')
    print()


def dfs_stack(n, visited, possible_connections, stack, ans):
    if visited[n] != 0:
        return
    else:
        visited[n] = 1
        stack.append(n)
        if len(stack) == number_of_cities:
            string = ""
            for x in stack:
                a = alphabet[x]
                string = string + str(a)
            ans.append(string)

        stack_display(stack)

        num = 0
        for relation in possible_connections[n]:
            if relation != 0:
                dfs_stack(num, visited, possible_connections, stack, ans)
            num = num + 1

        x = stack.pop()
        visited[x] = 0

        stack_display(stack)


def DFS():
    print_table(values)
    possible_connections = [[0 for j in range(number_of_cities)] for i in range(number_of_cities)]
    for y in range(number_of_cities):
        for x in range(number_of_cities):
            if values[y][x] != 0 and values[y][x]!="X":
                possible_connections[y][x] = 1
    visited = [0 for j in range(number_of_cities)]
    ans = []
    stack = []
    n = 0
    dfs_stack(n, visited, possible_connections, stack, ans)
    final_ans = []
    for x in ans:
        y = str(x) + "A"
        final_ans.append(y)
    final_ans = chaeck_if(final_ans)
    minimum, min_way = calculate_way(final_ans, values)
    print(minimum, min_way)


def minimum_spanning_tree():
    array = spawn_arrays()
    print_table(array)
    way = "A"
    cities = []
    choose_best = []
    for x in range(number_of_cities):
        cities.append(alphabet[x])
    for i in range(number_of_cities-1):
        for city in cities:
            if (city not in way):
                ways = way + city
                choose_best.append(ways)
                ways = city + way
                choose_best.append(ways)
        min_cost, min_way = calculate_way(choose_best, array)
        choose_best.clear()
        way = min_way
    if(len(way) == number_of_cities):
        first = way[0]
        last = way[-1]
        ways = way + first
        choose_best.append(ways)
        ways = last + way
        choose_best.append(ways)
    min_cost, min_way = calculate_way(choose_best, array)
    print(min_cost, min_way)


def bidirectional_search():
    print_table(values)
    index = index_2d('X')
    first_city = alphabet[index[0]]
    second_city = alphabet[index[1]]
    forbidden_way = first_city + second_city
    forbidden_way_reversed = second_city + first_city
    cities = []
    choose_best = []
    temp_array = []
    final_ways = []
    for x in range(number_of_cities):
        cities.append(alphabet[x])
    for city in cities:
        if (city not in first_city):
            ways = first_city + city
            choose_best.append(ways)
    for way in choose_best:
        if forbidden_way in way or forbidden_way_reversed in way:
            continue
        else:
            temp_array.append(way)
    for x in temp_array:
        y = x + second_city
        final_ways.append(y)
    print(final_ways)
    min_cost, min_way = calculate_way(final_ways, values)
    print(min_cost, min_way)
    choose_best.clear()
    temp_array.clear()


#BFS()
#DFS()
#minimum_spanning_tree()
greedy()
#bidirectional_search()