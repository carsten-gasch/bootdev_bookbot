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
