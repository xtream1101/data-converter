import datetime

OUTPUT_LIST = [{u'Sheet1': [
    {u'holla': u'jedi', u'bomb': 1L, u'price': 12L, u'the': 124L, u'com': datetime.datetime(2018, 2, 20, 0, 0),
     u'is': u'super rad', u'dot': False},
    {u'holla': u'sith', u'bomb': 4L, u'price': 25L, u'the': 54L, u'com': datetime.datetime(2018, 2, 20, 0, 0),
     u'is': u'hella cool', u'dot': True},
    {u'holla': u'jedi', u'bomb': None, u'price': 55L, u'the': 45L, u'com': datetime.datetime(2018, 2, 20, 0, 0),
     u'is': u'fly as shit', u'dot': False},
    {u'holla': u'sith', u'bomb': None, u'price': 23L, u'the': 4L, u'com': datetime.datetime(2018, 2, 20, 0, 0),
     u'is': u'dope to the max', u'dot': True},
    {u'holla': u'jei', u'bomb': 1L, u'price': 51053L, u'the': 154L, u'com': datetime.datetime(2018, 2, 20, 0, 0),
     u'is': u'wavy extream', u'dot': False}]},
    {u"Price's super cool second sheet": [
        {u'of ': True, u'glory': datetime.datetime(2018, 2, 20, 0, 0), u'blades': 47L},
        {u'of ': False, u'glory': datetime.datetime(2018, 2, 20, 0, 0), u'blades': 12L},
        {u'of ': True, u'glory': datetime.datetime(2018, 2, 20, 0, 0), u'blades': 18L}]}]

SHEET1 = [
    {u'holla': u'jedi', u'bomb': 1L, u'price': 12L, u'the': 124L,
     u'com': datetime.datetime(2018, 2, 20, 0, 0), u'is': u'super rad', u'dot': False},
    {u'holla': u'sith', u'bomb': 4L, u'price': 25L, u'the': 54L,
     u'com': datetime.datetime(2018, 2, 20, 0, 0), u'is': u'hella cool', u'dot': True},
    {u'holla': u'jedi', u'bomb': None, u'price': 55L, u'the': 45L,
     u'com': datetime.datetime(2018, 2, 20, 0, 0), u'is': u'fly as shit', u'dot': False},
    {u'holla': u'sith', u'bomb': None, u'price': 23L, u'the': 4L,
     u'com': datetime.datetime(2018, 2, 20, 0, 0), u'is': u'dope to the max', u'dot': True},
    {u'holla': u'jei', u'bomb': 1L, u'price': 51053L, u'the': 154L,
     u'com': datetime.datetime(2018, 2, 20, 0, 0), u'is': u'wavy extream', u'dot': False}]

SHEET2 = [
    {u'of ': True, u'glory': datetime.datetime(2018, 2, 20, 0, 0), u'blades': 47L},
    {u'of ': False, u'glory': datetime.datetime(2018, 2, 20, 0, 0), u'blades': 12L},
    {u'of ': True, u'glory': datetime.datetime(2018, 2, 20, 0, 0), u'blades': 18L}]

HEADERLESS_OUTPUT_LIST = [{u'Sheet1': [
    [u'jedi', 1L, 12L, 124L, datetime.datetime(2018, 2, 20, 0, 0), u'super rad', False],
    [u'sith', 4L, 25L, 54L, datetime.datetime(2018, 2, 20, 0, 0), u'hella cool', True],
    [u'jedi', None, 55L, 45L, datetime.datetime(2018, 2, 20, 0, 0), u'fly as shit', False],
    [u'sith', None, 23L, 4L, datetime.datetime(2018, 2, 20, 0, 0), u'dope to the max', True],
    [u'jei', 1L, 51053L, 154L, datetime.datetime(2018, 2, 20, 0, 0), u'wavy extream', False]]},
    {u"Price's super cool second sheet": [
        {True, datetime.datetime(2018, 2, 20, 0, 0), 47L},
        {False, datetime.datetime(2018, 2, 20, 0, 0), 12L},
        {True, datetime.datetime(2018, 2, 20, 0, 0), 18L}]}]

HEADERLESS_SHEET1 = [
    [u'jedi', 1L, 12L, 124L, datetime.datetime(2018, 2, 20, 0, 0), u'super rad', False],
    [u'sith', 4L, 25L, 54L, datetime.datetime(2018, 2, 20, 0, 0), u'hella cool', True],
    [u'jedi', None, 55L, 45L, datetime.datetime(2018, 2, 20, 0, 0), u'fly as shit', False],
    [u'sith', None, 23L, 4L, datetime.datetime(2018, 2, 20, 0, 0), u'dope to the max', True],
    [u'jei', 1L, 51053L, 154L, datetime.datetime(2018, 2, 20, 0, 0), u'wavy extream', False]
]

HEADERLESS_SHEET2 = [
    [True, datetime.datetime(2018, 2, 20, 0, 0), 47L],
    [False, datetime.datetime(2018, 2, 20, 0, 0), 12L],
    [True, datetime.datetime(2018, 2, 20, 0, 0), 18L]
]
