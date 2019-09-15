import operator


# data_set = {"Kostas": ["java", "prolog", "ai"],
#             "Petros": ["c", "c++", "ml"],
#             "Stathis": ["c++", "java", "php", "da"],
#             "Giorgos": ["pyhton", "php", "da"],
#             "Arianna": ["c++", "python", "da"],
#             "Lydia": ["ai", "ml", "da"],
#             "Alexia": ["c", "python", "ai"],
# }

data_set = {"Kostas": ["java", "prolog", "ai"],
            "Arianna": ["c++", "python", "da"],
            "Lydia": ["ai", "ml", "da"],
            "Alexia": ["c", "python", "ai"],
            "Petros": ["c", "c++", "ml"],
            "Stathis": ["c++", "java", "php", "da"],
            "Giorgos": ["python", "php", "da"],
}

languages = ["c", "c++", "python", "java", "prolog", "php", "ai", "ml", "da"]


def intialize_tree():
    un_man = []
    count_man = 0
    for lang in languages:
        for person in data_set:
            if lang in data_set[person]:
                count_man +=1
                last_man = person
        if count_man == 1:
            un_man.append(last_man)
        count_man = 0
    return un_man


def person_languages():
    person_value = {}
    lang_freq = languages_freq()
    addition_weigth = 0
    for person in data_set:
        for lang in data_set[person]:
            addition_weigth += len(data_set)/lang_freq[lang]
        person_value[person] = len(data_set[person]) + addition_weigth
        addition_weigth = 0
    return person_value


def possible_selection(solution, person_value):
    rest_persons = []
    for person in data_set:
        if person not in solution:
            rest_persons.append({'name': person, 'weight': person_value[person]})
    rest_persons.sort(reverse=True, key=operator.itemgetter('weight'))
    return rest_persons


def checkforsolution(solution):
    known_lang = []
    for person in solution:
        known_lang = known_lang + data_set[person]
    known_lang = list(set(known_lang))
    if len(known_lang) == 9:
        return True
    else:
        return False


def find_solution(solution):
    if checkforsolution(solution):
        print("The best solution is ", solution)
        return -1
    else:
        remain_person = possible_selection(solution, person_languages())
        for item in remain_person:
            solution.append(item['name'])
            flag = find_solution(solution)
            if flag == -1:
                return -1


def languages_freq():
    counter =0
    lang_freq ={}
    for lang in languages:
        for person in data_set:
            if lang in data_set[person]:
                counter +=1
        lang_freq[lang] = counter
        counter = 0
    return lang_freq


if __name__ == "__main__":
    root = intialize_tree()
    solution = root
    find_solution(solution)




