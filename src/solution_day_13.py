from utils.file_reader import read_file_as_strings
from utils.printer import timing_decorator


@timing_decorator
def day_13_part_1(file):
    data = read_file_as_strings(file)

    games = generate_games(data)

    tokens = 0
    for game in games:
        tokens += calculate_tokens(games, game, 0)

    return tokens


@timing_decorator
def day_13_part_2(file):
    data = read_file_as_strings(file)

    games = generate_games(data)

    tokens = 0
    for game in games:
        tokens += calculate_tokens(games, game, 10000000000000)

    return tokens


def generate_games(data):
    games = {}
    buttons = {}
    for line in data:
        if "Button A" in line:
            button_x = int(line[line.index("X+") + 2 : line.index(",")])
            button_y = int(line[line.index("Y+") + 2 :])
            buttons["Button A"] = (button_x, button_y)
        elif "Button B" in line:
            button_x = int(line[line.index("X+") + 2 : line.index(",")])
            button_y = int(line[line.index("Y+") + 2 :])
            buttons["Button B"] = (button_x, button_y)
        elif "Prize" in line:
            button_x = int(line[line.index("X=") + 2 : line.index(",")])
            button_y = int(line[line.index("Y=") + 2 :])
            prize_location = (button_x, button_y)
            games[prize_location] = buttons
            buttons = {}
    return games


def calculate_tokens(games, game, addition):
    prize_location_x, prize_location_y = game
    prize_location_x += addition
    prize_location_y += addition
    buttons = games[game]
    button_a_x, button_a_y = buttons["Button A"]
    button_b_x, button_b_y = buttons["Button B"]

    # prize_location_x = (button_a_x * m) + (button_b_x * n)
    # prize_location_y = (button_a_y * m) + (button_b_y * n)
    # Cramer's rule
    d = (button_a_x * button_b_y) - (button_b_x * button_a_y)
    d_a = (prize_location_x * button_b_y) - (prize_location_y * button_b_x)
    d_b = (prize_location_y * button_a_x) - (prize_location_x * button_a_y)

    result_a = d_a / d
    result_b = d_b / d

    if (
        result_a < 0
        or result_b < 0
        or not result_a.is_integer()
        or not result_b.is_integer()
    ):
        return 0
    else:
        return int((3 * result_a) + (1 * result_b))
