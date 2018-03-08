import datetime

SHEET1 = [
    {'holla': 'jedi', 'bomb': 1, 'price': 12, 'the': 124,
     'com': datetime.datetime(2018, 2, 20, 0, 0), 'is': 'super rad', 'dot': False},
    {'holla': 'sith', 'bomb': 4, 'price': 25, 'the': 54,
     'com': datetime.datetime(2018, 2, 20, 0, 0), 'is': 'hella cool', 'dot': True},
    {'holla': 'jedi', 'bomb': None, 'price': 55, 'the': 45,
     'com': datetime.datetime(2018, 2, 20, 0, 0), 'is': 'fly as shit',  'dot': False},
    { 'holla':  'sith',  'bomb': None,  'price': 23,  'the': 4,
      'com': datetime.datetime(2018, 2, 20, 0, 0), 'is': 'dope to the max', 'dot': True},
    {'holla': 'jei', 'bomb': 1, 'price': 51053, 'the': 154,
     'com': datetime.datetime(2018, 2, 20, 0, 0), 'is': 'wavy extream', 'dot': False}]

SHEET2 = [
    {'of ': True, 'glory': datetime.datetime(2018, 2, 20, 0, 0), 'blades': 47},
    {'of ': False, 'glory': datetime.datetime(2018, 2, 20, 0, 0), 'blades': 12},
    {'of ': True, 'glory': datetime.datetime(2018, 2, 20, 0, 0), 'blades': 18}]

HEADERLESS_SHEET1 = [
    ['jedi', 1, 12, 124, datetime.datetime(2018, 2, 20, 0, 0), 'super rad', False],
    ['sith', 4, 25, 54, datetime.datetime(2018, 2, 20, 0, 0), 'hella cool', True],
    ['jedi', None, 55, 45, datetime.datetime(2018, 2, 20, 0, 0), 'fly as shit', False],
    ['sith', None, 23, 4, datetime.datetime(2018, 2, 20, 0, 0), 'dope to the max', True],
    ['jei', 1, 51053, 154, datetime.datetime(2018, 2, 20, 0, 0), 'wavy extream', False]
]

HEADERLESS_SHEET2 = [
    [True, datetime.datetime(2018, 2, 20, 0, 0), 47],
    [False, datetime.datetime(2018, 2, 20, 0, 0), 12],
    [True, datetime.datetime(2018, 2, 20, 0, 0), 18]
]
