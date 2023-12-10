import re
regexp = r"ВТ((\s)?(–)?(\w{0,})?([а-яА-Я]{0,})?(\s)?){0,4}ИТМО"
def testRegex(value):
    match = re.search(regexp, value)
    if match != None:
        print(match.group())
    else:
        print("None")
testRegex("А ты знал, что ВТ – лучшая кафедра в ИТМО?") #ВТ - лучшая кафедра в ИТМО
testRegex("ВТ получит первое место в тесте ИТМО") #None
testRegex("И конечно же все в ВТ начали ОПД и кодекс ИТМО учить") # ВТ начали ОПД и кодекс ИТМО
testRegex("fieiu hfiu3h2ihi2 ВТ 3шг23иш - кммумуу 23 ИТМО ацацуау") #None
testRegex("fieiu hfiu3h2ihi2 ВТ 3шг23иш - кммумуу 2уаук укаукпук3 ИТМО ацацуау")
#None