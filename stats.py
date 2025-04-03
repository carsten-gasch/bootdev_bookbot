def get_num_words(string):
    return len(string.split())


def get_count_characters(string):
    ret = {}
    for c in string:
        if c.lower() in ret:
            ret[c.lower()] += 1
        else:
            ret[c.lower()] = 1
    return ret


def sorted_list(chars):
    sorted_list = []
    for item, amount in chars.items():
        char = {"name": item, "amount": amount}
        sorted_list.append(char)
    sorted_list.sort(reverse=True, key=sort_by_amount)
    return sorted_list


def sort_by_amount(dict):
    return dict["amount"]
