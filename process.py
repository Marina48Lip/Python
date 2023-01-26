def search(sn):
    res_list = []
    with open('data.txt', 'r', encoding='utf-8') as file:
        while True:
            some_str = file.readline()
            if not some_str:
                if not file.readline():
                    break
            if some_str.rstrip() == sn:
                res_list.append(sn)
                for i in range(1, 5):
                    res_list.append(file.readline().rstrip())
                res_list.append('')
    if len(res_list) > 0:
        return res_list
    return 'Таких людей не найдено'


def export(res):
    with open('data.txt', 'a', encoding='utf-8') as file:
        for ind in range(5):
            file.write(res[ind] + '\n')
        file.write(res[5])

