def main(table):

    for i in range(len(table)):
        count_None = table[i].count(None)
        while count_None != 0:
            table[i].remove(None)
            count_None -= 1

        if table[i] != []:
            if table[i][0] == "Не выполнено":
                table[i][0] = "Нет"
            else:
                table[i][0] = "Да"
            table[i][3] = f'{table[i][3][8:10]}'\
                f'-{table[i][3][3:5]}'\
                f'-{table[i][3][0:2]}'
            table[i][1] = f'{table[i][1][0:3]}-{table[i][1][3:6]}'\
                f'-{table[i][1][6:10]}'
            table[i][2] = '%.3f' % round(float(table[i][2]), 3)

    count_None = table.count([])
    while count_None != 0:
        table.remove([])
        count_None -= 1
    return table


print(main([
    ['Не выполнено', '4197552325', None, None, '0.2', '15-06-2001'],
    ['Не выполнено', '3722521154', None, None, '1.0', '26-10-1999'],
    ['Выполнено', '0197860964', None, None, '0.4', '17-11-2001'],
    [None, None, None, None, None, None],
    ['Выполнено', '6631952981', None, None, '0.2', '09-09-2000'],
]))
print('\n')
print(main([
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    ['Выполнено', '7304877308', None, None, '0.6', '16-12-2003'],
    ['Выполнено', '5082119591', None, None, '0.4', '23-05-2002'],
    ['Выполнено', '6961176167', None, None, '0.7', '20-10-2001'],
]))
