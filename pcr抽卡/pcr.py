import os
import numpy as np
import random


def pcr_pick_ten():
    three_star_list = os.listdir('E:/CookBot/resource/pcr/3star')
    two_star_list = os.listdir('E:/CookBot/resource/pcr/2star')
    one_star_list = os.listdir('E:/CookBot/resource/pcr/1star')
    three_star_pick_list = list()
    two_star_pick_list = list()
    one_star_pick_list = list()
    p_normal = np.array([0.795, 0.18, 0.025])
    p_tenth = np.array([0.975, 0.025])
    result = '三星:'
    for i in range(9):
        normal_pick = np.random.choice([1, 2, 3], p=p_normal.ravel())
        if normal_pick == 3:
            three_star_pick = random.choice(three_star_list)
            three_star_pick_list.append(three_star_pick)
        elif normal_pick == 2:
            two_star_pick = random.choice(two_star_list)
            two_star_pick_list.append(two_star_pick)
        else:
            one_star_pick = random.choice(one_star_list)
            one_star_pick_list.append(one_star_pick)
    tenth_pick = np.random.choice([2, 3], p=p_tenth.ravel())
    if tenth_pick == 3:
        three_star_pick = random.choice(three_star_list)
        three_star_pick_list.append('#' + three_star_pick + '#')
    else:
        two_star_pick = random.choice(two_star_list)
        two_star_pick_list.append(two_star_pick)
    if len(three_star_pick_list) == 0:
        result = result + '没抽到！'
    else:
        for i in range(len(three_star_pick_list)):
            result = result + ' ' + three_star_pick_list[i]
    result = result + '\n' + '二星:'
    for i in range(len(two_star_pick_list)):
        result = result + ' ' + two_star_pick_list[i]
    result = result + '\n' + '一星:'
    for i in range(len(one_star_pick_list)):
        result = result + ' ' + one_star_pick_list[i]
    print(result)
    """if to == 'private':
        send_private_message(id, result)
    elif to == 'group':
        send_group_message(id, result)"""


s = '抽卡pcrup'
if s[0:2] == '抽卡':
    game = s.replace('抽卡', '')
    if 'pcr' in game:
        pcr_pick_ten()
