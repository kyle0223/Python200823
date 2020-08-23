# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:30:59 2020

@author: kyle
"""

import random 
a=random.randint(1,100)

while True:
    num=int(input('輸入1~100的數字'))
    if num<=0 or num>100:
        print("重新輸入")
    else:
        if num<a: 
            if a-num<=20:
                print("大一點(大20以內)")
            else:
                print("大很多(20以外)")
        elif num>a:
            if num-a<=20:
                print("小一點(小20以內)")
            else:
                print("小很多(20以外)")
        else:
            print("答對")
            print('-----------------------------------------------------------------------------------------------------')
            break