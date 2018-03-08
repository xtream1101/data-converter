import datetime

SHEET1 = [
    {'holla': 'jedi', 'bomb': 1, 'price': 12, 'the': 124,
     'com': datetime.datetime(2018, 2, 20, 0, 0), 'is': 'super rad', 'dot': False},
    {'holla': 'sith', 'bomb': 4, 'price': 25, 'the': 54,
     'com': datetime.datetime(2018, 2, 20, 0, 0), 'is': 'hella cool', 'dot': True},
    {'holla': 'jedi', 'bomb': None, 'price': 55, 'the': 45,
     'com': datetime.datetime(2018, 2, 20, 0, 0), 'is': 'fly as shit', 'dot': False},
    {'holla': 'sith', 'bomb': None, 'price': 23, 'the': 4,
     'com': datetime.datetime(2018, 2, 20, 0, 0), 'is': 'dope to the max', 'dot': True},
    {'holla': 'jei', 'bomb': 1, 'price': 51053, 'the': 154,
     'com': datetime.datetime(2018, 2, 20, 0, 0), 'is': 'wavy extream', 'dot': False}]

SHEET2 = [
    {'of ': True, 'glory': datetime.datetime(2018, 2, 20, 0, 0), 'blades': 47},
    {'of ': False, 'glory': datetime.datetime(2018, 2, 20, 0, 0), 'blades': 12},
    {'of ': True, 'glory': datetime.datetime(2018, 2, 20, 0, 0), 'blades': 18}]

HEADERLESS_SHEET1 = [
    [12, 'super rad', 124, 1, False, datetime.datetime(2018, 2, 20, 0, 0), 'jedi'],
    [25, 'hella cool', 54, 4, True, datetime.datetime(2018, 2, 20, 0, 0), 'sith'],
    [55, 'fly as shit', 45, None, False, datetime.datetime(2018, 2, 20, 0, 0), 'jedi'],
    [23, 'dope to the max', 4, None, True, datetime.datetime(2018, 2, 20, 0, 0), 'sith'],
    [41053, 'wavy extream', 154, 1, False, datetime.datetime(2018, 2, 20, 0, 0), 'jei']
]

HEADERLESS_SHEET2 = [
    [47, True, datetime.datetime(2018, 2, 20, 0, 0)],
    [12, False, datetime.datetime(2018, 2, 20, 0, 0)],
    [18, True, datetime.datetime(2018, 2, 20, 0, 0)]
]
