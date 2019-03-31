
def spade():
    temp_dict = main_dict.copy()
    for i in range(2,6):
        candidate_dict = generate_candidates(temp_dict)
        if len(candidate_dict) == 0:
            break
        candidate_dict = {key: item for key,item in candidate_dict.items() if len(item) >= min_support}
        for i in candidate_dict:
            frequent_dict[i] = len(candidate_dict[i])
        temp_dict = candidate_dict

    print_format(frequent_dict)


def generate_candidates(temp_dict):
    cand_dict = {}
    for item,keys in temp_dict.items():
        for i in range(len(keys)):
            if keys[i][1] >= len(patterns2[keys[i][0]])-1:
                continue
            sid = keys[i][0]
            next_item = patterns2[sid][keys[i][1]+1]
            new_cand = ' '.join([item, next_item])
            if new_cand not in cand_dict:
                cand_dict[new_cand] = [(sid, keys[i][1]+1)]
            else:
                cand_dict[new_cand].append((sid, keys[i][1]+1))
    return cand_dict




def print_format(dick):
    main_list = list(dick.items())
    main_list.sort(key= lambda x :  (-x[1], x[0]))
    for index,i in enumerate(main_list):
        print('[' +str(i[1])+', ' + '\''+i[0] + '\']')
        if index == 19:
            break



if __name__ == '__main__':
    min_support = 2
    frequent_dict = {}
    main_dict = {}
    patterns2 = []
    try:
        sid= 0
        while True:
            pattern = input()
            pattern = pattern.strip()
            if pattern == None or pattern == '':
                raise Exception
            patterns2.append([i.strip() for i in pattern.split(' ') if i.strip() != ''])
            for eid,item in enumerate(pattern.split(' ')):
                if item.strip() == '' or item.strip() == None:
                    continue
                if item.strip() in main_dict:
                    main_dict[item.strip()].append((sid,eid))
                else:
                    main_dict[item.strip()] =[(sid,eid)]
            sid +=1

    except:
        main_dict = {key: item for key, item in main_dict.items() if len(item) >= min_support}
        spade()

