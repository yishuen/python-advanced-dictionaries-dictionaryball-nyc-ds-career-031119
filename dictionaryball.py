game_dictionary = {'home': {'team_name': 'Brooklyn Nets',
                            'colors': ['Black', 'White'],
                            'players': {'Alan Anderson': {
                                            'number': 0,
                                            'shoe': 16,
                                            'points': 22,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 3,
                                            'blocks': 1,
                                            'slam_dunks': 1
                                        },
                                        'Reggie Evans': {
                                            'number': 30,
                                            'shoe': 14,
                                            'points': 12,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 12,
                                            'blocks': 12,
                                            'slam_dunks': 7
                                        },
                                        'Brook Lopez': {
                                            'number': 11,
                                            'shoe': 17,
                                            'points': 17,
                                            'rebounds': 19,
                                            'assists': 10,
                                            'steals': 3,
                                            'blocks': 1,
                                            'slam_dunks': 15
                                        },
                                        'Mason Plumlee': {
                                            'number': 1,
                                            'shoe': 19,
                                            'points': 26,
                                            'rebounds': 12,
                                            'assists': 6,
                                            'steals': 3,
                                            'blocks': 8,
                                            'slam_dunks': 5
                                        },
                                        'Jason Terry': {
                                            'number': 31,
                                            'shoe': 15,
                                            'points': 19,
                                            'rebounds': 2,
                                            'assists': 2,
                                            'steals': 4,
                                            'blocks': 11,
                                            'slam_dunks': 1
                                        }
                                        }},
                    'away': {'team_name': 'Charlotte Hornets',
                            'colors': ['Turquoise', 'Purple'],
                            'players': {'Jeff Adrien': {
                                            'number': 4,
                                            'shoe': 18,
                                            'points': 10,
                                            'rebounds': 1,
                                            'assists': 1,
                                            'steals': 2,
                                            'blocks': 7,
                                            'slam_dunks': 2
                                        },
                                        'Bismak Biyombo': {
                                            'number': 0,
                                            'shoe': 16,
                                            'points': 12,
                                            'rebounds': 4,
                                            'assists': 7,
                                            'steals': 7,
                                            'blocks': 15,
                                            'slam_dunks': 10
                                        },
                                        'DeSagna Diop': {
                                            'number': 2,
                                            'shoe': 14,
                                            'points': 24,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 4,
                                            'blocks': 5,
                                            'slam_dunks': 5
                                        },
                                        'Ben Gordon': {
                                            'number': 8,
                                            'shoe': 15,
                                            'points': 33,
                                            'rebounds': 3,
                                            'assists': 2,
                                            'steals': 1,
                                            'blocks': 1,
                                            'slam_dunks': 0
                                        },
                                        'Brendan Haywood': {
                                            'number': 33,
                                            'shoe': 15,
                                            'points': 6,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 22,
                                            'blocks': 5,
                                            'slam_dunks': 12
                                        }}}}

def game_dict():
    return game_dictionary

def all_players():
    players = {}
    for t, x in game_dict().items():
        players.update(x['players'])
    return players

def num_points_scored():
    for p, s in all_players().items():
        if p == name:
            return s['points']

def shoe_size():
    for p, s in all_players().items():
        if p == name:
            return s['shoe']

def team_colors():
    for t, s in game_dict().items():
        if s['team_name'] == team:
            return s['colors']

def team_names():
    names = []
    for t, s in game_dict().items():
        names.append(s['team_name'])
    return names

def player_numbers():
    numbers = []
    for t, s in game_dict().items():
        if s['team_name'] == team:
            for p, stuff in s['players'].items():
                numbers.append(stuff['number'])
    return numbers

def player_stats():
    for p, s in all_players().items():
        if p == name:
            return s
