import string
from fuzzywuzzy import fuzz

def calibrate_school(university_list, school):
    exclude = set(string.punctuation)
    school = ''.join(ch for ch in school if ch not in exclude)
    school.replace('  ', '')
    if school.encode('utf-8') in university_list.keys():
        return university_list[school]
    else:
        scores = {}
        for uni in university_list:
            scores[uni] = fuzz.partial_ratio(school, uni)
        choice = max(scores, key=scores.get)
        return university_list[choice]

def calibrate_degree(degree):
    if degree.find('M') != -1 or degree.find('m') != -1:
        return 1
    elif degree.find('D') != -1 or degree.find('d') != -1:
        return 2
    else:
        print degree
        exit(0)