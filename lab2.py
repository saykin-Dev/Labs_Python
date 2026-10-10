""" ДЗ: написать функцию чистки списка от всех пустых элементов"""
""" Разобрать Декораторы базово. """

def is_empty(collection): # на вход коллекция, на выход True если она пустая, или False если что-то в ней есть
    if collection is None:
        return True
    elif isinstance(collection, str) and collection == '':
        return True
    elif isinstance(collection, (list, tuple, set, frozenset, dict)) and len(collection) == 0:
        return True
    return False

def clean(user_collection): # на вход список, на выходе рекурсивно очищенный масив без пустых элементов где-либо
    if not isinstance(user_collection, (list, tuple, set, frozenset, dict)):
        return user_collection
    elif isinstance(user_collection, (list, tuple, set, frozenset)):
        result = []
        for element in user_collection:
            cleaned_element = clean(element)
            if not is_empty(cleaned_element):
                result.append(cleaned_element)

        if isinstance(user_collection, set):
            return set(result)
        elif isinstance(user_collection, frozenset):
            return frozenset(result)
        elif isinstance(user_collection, tuple):
            return tuple(result)
        elif isinstance(user_collection, list):
            return list(result)
        return result

    elif isinstance(user_collection, dict):
        result_dic = {}
        for key, value in user_collection.items():
            cleaned_dic_element = clean(value)
            if not is_empty(cleaned_dic_element):
                result_dic[key] = cleaned_dic_element
        return result_dic
    
print(clean(['abs', '', {'': '123', 'a': '2344', 'df': ['', 223, 'sdfsfg']}, {}]))



