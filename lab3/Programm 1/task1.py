import re

def solve(string):
    """ Возвращает количество смайликов вида ;<) в строке
    374856 % 6 = 0 => Глаза: :
    374856 % 5 = 0 => Нос: -
    374856 % 7 = 6 => Рот: P
    """
    pattern = r':-P'
    return len(re.findall(pattern, string))