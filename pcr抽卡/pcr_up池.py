import os
import numpy as np
import random


def pcr_pick_up_300(id, to):
    three_star_list = os.listdir('E:/CookBot/resource/pcr/3star')
    two_star_list = os.listdir('E:/CookBot/resource/pcr/2star')
    one_star_list = os.listdir('E:/CookBot/resource/pcr/1star')
    up_princess_list = os.listdir('E:/CookBot/resource/pcr/up')
    three_star_pick_list = list()
    three_star_pick_number = list()
    two_star_pick_list = list()
    one_star_pick_list = list()
    p_normal = np.array([0.795, 0.18, 0.018, 0.007])
    p_tenth = np.array([0.975, 0.018, 0.007])
    result = '当前卡池：万圣复刻' + '\n' + '三星:'
    k = 1
    for i in range(30):
        for j in range(9):
            normal_pick = np.random.choice([1, 2, 3, 4], p=p_normal.ravel())
            if normal_pick == 4:
                up_princess_pick = random.choice(up_princess_list)
                three_star_pick_list.append(up_princess_pick)
                three_star_pick_number.append(k)
            elif normal_pick == 3:
                three_star_pick = random.choice(three_star_list)
                three_star_pick_list.append(three_star_pick)
                three_star_pick_number.append(k)
            elif normal_pick == 2:
                two_star_pick = random.choice(two_star_list)
                two_star_pick_list.append(two_star_pick)
            elif normal_pick == 1:
                one_star_pick = random.choice(one_star_list)
                one_star_pick_list.append(one_star_pick)
            k += 1
        tenth_pick = np.random.choice([2, 3, 4], p=p_tenth.ravel())
        if tenth_pick == 4:
            up_princess_pick = random.choice(up_princess_list)
            three_star_pick_list.append(up_princess_pick)
            three_star_pick_number.append(k)
        if tenth_pick == 3:
            three_star_pick = random.choice(three_star_list)
            three_star_pick_list.append(three_star_pick)
            three_star_pick_number.append(k)
        else:
            two_star_pick = random.choice(two_star_list)
            two_star_pick_list.append(two_star_pick)
        k += 1
    for i in range(len(three_star_pick_list)):
        result = result + ' ' + three_star_pick_list[i] + str(three_star_pick_number[i])
    result = result + ' 共' + str(len(three_star_pick_list)) + '只！' + '\n' + '二星:' + str(len(two_star_pick_list)) + '只！\n' + '一星:' + str(len(one_star_pick_list)) + '只！'
    print(result)
    """if to == 'private':
        send_private_message(id, result)
    elif to == 'group':
        send_group_message(id, result)"""


s = '抽卡pcrup一井'  # 当前版本：鬼剑
if s[0:2] == '抽卡':
    game = s.replace('抽卡', '')
    if 'pcr' in game:
        if game[3:7] == 'up一井':
            pcr_pick_up_300(id, 'to')
