import copy

def get_speed(tile, direction):
    if tile == "p":
        return default_speed/2
    if tile == "c":
        return default_speed

    x = int(tile)
    y = int(direction)
    if x == y:
        return default_speed*2
    if x%4 == (y+2)%4:
        return default_speed/4
    if (x%4 == (y+1)%4) or (x%4 == (y+3)%4):
        return default_speed*0.75

def run_path_with_log(path):
    percent = 50
    pos = 0
    tick = 0
    speed = 0
    newspeed = 0

    while pos < len(path)/2-1 or percent < 50:

        if percent < 50:
            dir = path[pos*2-1]
        else:
            dir = path[pos * 2 + 1]

        if tick%crew_speed_check_time == 0:
            newspeed = get_speed(path[pos * 2], dir)

        stringtoadd = ""
        if not speed == newspeed:
            stringtoadd = "   new speed: " + str(newspeed)
            speed = newspeed
        print(str(tick) + ": " + str(percent) + stringtoadd)


        percent = percent + speed
        if percent >= 100:
            pos = pos + 1
            percent = percent -100
            print("New tile: " + str(pos + 1))

        tick = tick + 1

    return tick

def run_path(path):
    percent = 50
    pos = 0
    tick = 0
    speed = 0
    newspeed = 0

    while pos < len(path)/2-1 or percent < 50:

        if percent < 50:
            dir = path[pos*2-1]
        else:
            dir = path[pos * 2 + 1]

        if tick%crew_speed_check_time == 0:
            newspeed = get_speed(path[pos * 2], dir)

        speed = newspeed


        percent = percent + speed
        if percent >= 100:
            pos = pos + 1
            percent = percent -100

        tick = tick + 1

    return tick

def generate_straight_path(length, direction):
    path = ""
    for i in range(length):
        path += direction*2
    return path[:-1]

def generate_right_down_path(length):
    path = ""
    for i in range(length):
        path += "21"
        path += "12"
    return path

def print_coordinate_matrix(coordinate_matrix):
    maxx = 0
    minx = 0
    maxy = 0
    miny = 0

    for tile in coordinate_matrix:
        if tile[1][0] > maxx:
            maxx = tile[1][0]
        if tile[1][0] < minx:
            minx = tile[1][0]
        if tile[1][1] > maxy:
            maxy = tile[1][1]
        if tile[1][1] < miny:
            miny = tile[1][1]

    for y in range(maxy, miny-1, -1):
        string = ""
        for x in range(minx, maxx+1):
            string += get_tile_string(coordinate_matrix, [x, y])
        print(string)


def get_tile_string(coordinate_matrix, coordinate):
    for tile in coordinate_matrix:
        if tile[1] == coordinate:
            if tile[0] == "0":
                return "^"
            if tile[0] == "1":
                return ">"
            if tile[0] == "2":
                return "v"
            if tile[0] == "3":
                return "<"
            if tile[0] == "p":
                return "p"
            if tile[0] == "c":
                return "c"
            return "Error"
    return " "


def create_coordinate_matrix(path):
    coordinate = [0, 0]
    coordinate_matrix = []
    for i in range(int(len(path)/2)):
        i *= 2

        coordinate_matrix.append([path[i], copy.deepcopy(coordinate)])

        if path[i+1] == "0":
            coordinate =  copy.deepcopy(coordinate_matrix[int(i/2)][1])
            coordinate[1] += 1
        if path[i+1] == "1":
            coordinate =  copy.deepcopy(coordinate_matrix[int(i/2)][1])
            coordinate[0] += 1
        if path[i+1] == "2":
            coordinate =  copy.deepcopy(coordinate_matrix[int(i/2)][1])
            coordinate[1] += -1
        if path[i+1] == "3":
            coordinate =  copy.deepcopy(coordinate_matrix[int(i/2)][1])
            coordinate[0] += -1
    return coordinate_matrix

default_speed = 11
path1 = "p2" + generate_straight_path(15, "2") + "1" + generate_straight_path(15, "1") + "2" + "p0"
pathpart = "21122112211221221112"
path2 = "p2" + pathpart*3 + "p001"
crew_speed_check_time = 5


print(run_path(path1))
print(run_path(path2))
print(run_path("p2" + generate_right_down_path(15) + "p0"))
