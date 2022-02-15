def solution(id_list, report, k):
    report_set = list(set(report))
    dict_mail = {}
    dict_reported = {}
    list_send = [0]*len(id_list)
    for i in id_list:
        dict_mail[i]=[]

    for i in report_set:
        id,ed = i.split(' ')
        dict_mail[id].append(ed)

        if ed in dict_reported.keys():
            dict_reported[ed] += 1
        else:
            dict_reported[ed] = 1

    for idx,i in enumerate(id_list):
        for j in dict_mail[i]:
            if j not in dict_reported.keys():
                list_send[idx] = 0
            elif dict_reported[j] < k:
                continue
            elif dict_reported[j] >= k:
                list_send[idx] += 1
    return list_send
