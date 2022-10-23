import os
import numpy as np
import random


def pcr_pick_up_300():
    three_star_list = os.listdir('E:/CookBot/resource/pcr/3star')
    two_star_list = os.listdir('E:/CookBot/resource/pcr/2star')
    one_star_list = os.listdir('E:/CookBot/resource/pcr/1star')
    three_star_pick_list = list()
    two_star_pick_list = list()
    one_star_pick_list = list()
    p_normal = np.array([0.795, 0.18, 0.018, 0.007])
    p_tenth = np.array([0.975, 0.018, 0.007])
    result = '当前卡池：鬼剑' + '\n' + '三星:'
    for i in range(30):
        for j in range(9):
            normal_pick = np.random.choice([1, 2, 3, 4], p=p_normal.ravel())
            if normal_pick == 3 or normal_pick == 4:
                three_star_pick = random.choice(three_star_list)
                three_star_pick_list.append(three_star_pick)
            elif normal_pick == 2:
                two_star_pick = random.choice(two_star_list)
                two_star_pick_list.append(two_star_pick)
            elif normal_pick == 1:
                one_star_pick = random.choice(one_star_list)
                one_star_pick_list.append(one_star_pick)
        tenth_pick = np.random.choice([2, 3, 4], p=p_tenth.ravel())
        if tenth_pick == 3 or tenth_pick == 4:
            three_star_pick = random.choice(three_star_list)
            three_star_pick_list.append(three_star_pick)
        else:
            two_star_pick = random.choice(two_star_list)
            two_star_pick_list.append(two_star_pick)
    for i in range(len(three_star_pick_list)):
        result = result + ' ' + three_star_pick_list[i]
    result = result + str(len(three_star_pick_list)) + '只！' + '\n' + '二星:' + str(len(two_star_pick_list)) + '只！\n' + '一星' + str(len(one_star_pick_list)) + '只！'
    print(result)


s = '抽卡pcrup一井'  # 当前版本：鬼剑
if s[0:2] == '抽卡':
    game = s.replace('抽卡', '')
    if 'pcr' in game:
        if game[3:7] == 'up一井':
            pcr_pick_up_300()
