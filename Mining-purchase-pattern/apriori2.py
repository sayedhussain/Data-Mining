

def find_patterns(pattern):
    global k
    fk = {}
    temp_pattern = [i for j in patterns for i in j]
    print(temp_pattern)
    for item in temp_pattern:
        print(item)
        support = temp_pattern.count(item)
        if support >= min_support:
            fk[frozenset(item)] = support
    main_dict.update(fk)
    while len(fk) != 0:
        k += 1
        Ck=generate_candidates(fk,k)
        fk = generate_frequent_pattern(Ck)
        main_dict.update(fk)
    return main_dict


def generate_frequent_pattern(ck):
    fk = {}
    list_frequent = [i for i in ck]
    for i in list_frequent:
        count = 0
        for j in patterns:
            if i.issubset(j) == True:
                count+=1

        if count >= min_support:
            fk[frozenset(i)] = count
    return fk



def generate_candidates(fk,k):
    main_dict = {}
    list_candidates = [i for i in fk]
    print(list_candidates)
    new_list = []
    for i in range(0, len(list_candidates) - 1):
        for j in range(i + 1, len(list_candidates)):
            flag = pruning(list_candidates[i], list_candidates[j],k)
            if flag:
                new_list.append(list_candidates[i].union(list_candidates[j]))
    new_list = list(set(new_list))
    return new_list


def pruning(obj1, obj2,k):
    out_count = 0
    main_candidate = obj1.union(obj2)
    for j in patterns:
        if main_candidate.issubset(j):
            out_count +=1
    if out_count >= min_support:
        flag_subset = True
    else:
        flag_subset = False

    if len(main_candidate) > k or flag_subset == False:
        return False
    else:
        return True

def find_closedpatterns(dict1):
    closed_dic = {}
    list_keys = list(dict1.keys())
    subset_list = []
    maximal_freq_list = []
    for i in range(0,len(list_keys)):
        for j in range(0, len(list_keys)):
            if list_keys[i] == list_keys[j]:
                continue
            if list_keys[i].issubset(list_keys[j]) == True:
                subset_list.append(list_keys[i])
                if dict1[list_keys[i]] != dict1[list_keys[j]]:
                    closed_dic[list_keys[i]] =  dict1[list_keys[i]]
        if list_keys[i] not in subset_list:
            maximal_freq_list.append(list_keys[i])
            closed_dic[list_keys[i]] = dict1[list_keys[i]]

    print(closed_dic)
    print(maximal_freq_list)
    # last_element = list_keys[-1]
    # for i in list_keys:
    #     if last_element.issubset(i) == False and dict1[last_element] == dict1[i]:
    #         closed_dic[last_element] = dict1[last_element]
    print()









if __name__ == '__main__':
    candidate_itemset = {}
    frequesnt_itemset = {}
    main_dict = {}
    min_support = int(input())
    k=1
    patterns = []
    try:
        while True:
            pattern = input()
            pattern= pattern.strip()
            if pattern == None or pattern == '':
                raise Exception
            patterns += [pattern.split(' ')]

    except:
        print(patterns)
        find_patterns(patterns)
        find_closedpatterns(main_dict)






