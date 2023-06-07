# Initial thoughts were direct with triangles.
# Then the mirrored position was introduced
# followed by talking with Eric Stratigakis (https://abstractigakis.io)
# We spoke about my initial pseudo code, and how the approach is best coded
# the theory is you can stack rooms in directions, and the relative positions can be used to calculate the validity of the shot


from math import hypot
from numpy import zeros


def calcHypotenuse(p1, p2):
    return hypot((p1[0] - p2[0]), (p1[1] -  p2[1]))
    

def computeGCD(x, y):
    while(y):
        x, y = y, x % y
    return abs(x)


def get_position_by_multiplier(initial_position, multipliers, dimensions):
    multipliers_x = multipliers[0]
    multipliers_y = multipliers[1]

    dimension_x = dimensions[0]
    dimension_y = dimensions[1]

    position_x = initial_position[0]
    position_y = initial_position[1]

    # Calculate the relative position based on multiples, or direct difference
    final_x = dimension_x*multipliers_x + position_x if multipliers_x % 2 == 0 else dimension_x*multipliers_x + (dimension_x - position_x)
    final_y = dimension_y*multipliers_y + position_y if multipliers_y % 2 == 0 else dimension_y*multipliers_y + (dimension_y - position_y)

    return (final_x, final_y)


def solution(dimensions, your_position, trainer_position, distance):
    # Get Room Dimensions
    room_width = dimensions[0]
    room_height = dimensions[1]

    # Get my position
    my_posX = your_position[0]
    my_posY = your_position[1]

    # Identify the coverage distance of my beam based on travel

    north_distance_multiples = (distance + my_posY)//room_height + 1
    south_distance_multiples = (distance - my_posY)//room_height + 1
    west_distance_multiples = (distance - my_posX)//room_width + 1
    east_distance_multiples = (distance + my_posX)//room_width + 1


    max_width = (east_distance_multiples + west_distance_multiples)*room_width + 1
    max_height = (north_distance_multiples + south_distance_multiples)*room_height + 1

    width_offset = west_distance_multiples*room_width
    height_offset = south_distance_multiples*room_height

    grid = zeros(shape=(max_width, max_height))

    # Populate the grid with relative possible positions for me and the trainer
    for i in range(-1*west_distance_multiples, east_distance_multiples):
        for j in range(-1*south_distance_multiples, north_distance_multiples):
            trainer_pos_result = get_position_by_multiplier(
                trainer_position, [i, j], dimensions)

            trainer_posX_multiplied = trainer_pos_result[0]
            trainer_posY_multiplied = trainer_pos_result[1]

            my_pos_result = get_position_by_multiplier(
                your_position, [i, j], dimensions)

            my_posX_multiplied = my_pos_result[0]
            my_posY_multiplied = my_pos_result[1]

            grid[trainer_posX_multiplied+width_offset][trainer_posY_multiplied+height_offset] = 1
            grid[my_posX_multiplied+width_offset][my_posY_multiplied+height_offset] = 2


    attempted_shots = set()
    successes = 0

    # Attempt to cycle through multiples and see if the shots are succecssful
    for i in range(-1*west_distance_multiples, east_distance_multiples):
        for j in range(-1*south_distance_multiples, north_distance_multiples):
            attempted_trainer_posX, attempted_trainer_posY = get_position_by_multiplier(
                trainer_position, [i, j], dimensions)
            if distance < calcHypotenuse([attempted_trainer_posX, attempted_trainer_posY], your_position):
                continue
            diffY = attempted_trainer_posY - my_posY
            diffX = attempted_trainer_posX - my_posX
            d = computeGCD(diffY, diffX)
            diffY = int(diffY/d)
            diffX = int(diffX/d)
            if (diffY, diffX) in attempted_shots:
                continue
            attempted_shots.add((diffY, diffX))
            ray_x, ray_y = my_posX + width_offset, my_posY + height_offset
            while True:
                ray_x += diffX
                ray_y += diffY
                entity = grid[ray_x][ray_y]
                if entity == 1:
                    successes += 1
                    break
                elif entity == 2:
                    break
    return successes


# Tests to try:
assert solution([3, 2], [1, 1], [2, 1], 4) == 7
assert solution([2, 5], [1, 2], [1, 4], 11) == 27
assert solution([23, 10], [6, 4], [3, 2], 23) == 8
assert solution([1250, 1250], [1000, 1000], [500, 400], 10000) == 196
assert solution([10, 10], [4, 4], [3, 3], 5000) == 739323
assert solution([2, 3], [1, 1], [1, 2], 4) == 7
assert solution([3, 4], [1, 2], [2, 1], 7) == 10
assert solution([4, 4], [2, 2], [3, 1], 6) == 7
assert solution([300, 275], [150, 150], [180, 100], 500) == 9
# assert solution([3, 4], [1, 1], [2, 2], 500) == 54243
assert solution([3, 2], [1, 1], [2, 1], 7) == 19
print('that is it')
