# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 21:36:25 2023
@author: HP
"""
#Snake and Ladder

from PIL import Image
import random

def show_brd():
    img=Image.open("E:\py_prog\snakenladder.png")
    img.show()

def check_ladder(pp):
    l_dict={1:38,4:14,9:31,21:42,28:84,51:67,72:91,80:99}
    k=l_dict.keys()
    if pp in k:
        print('Ladder')
        pp=l_dict[pp]
    return pp

def check_snake(pp):
    s_dict={17:7,54:34,62:19,64:60,87:36,92:73,95:73,98:79}
    k=s_dict.keys()
    if pp in k:
        print('Snake')
        pp=s_dict[pp]
    return pp

def p_dice():
    k=input("Press ENTER to roll the dice:")
    dice=random.randint(1, 6)
    print('Dice showed',dice)
    return dice    
      
def play():
    p1=input('Player 1:')
    p2=input('Player 2:')
    print()
    show_brd()
    pp1,pp2,turn=1,1,0
    while True:
        if turn%2==0:
            print(p1,',Your Turn')
            dice=p_dice()
            pp1+=dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            if pp1==100:
                print(p1,'Won')
                break
            elif pp1>100:
                pp1=pp1-dice
            print('You are at',pp1,'\n\n')
            
     
        else:
            print(p2,',Your Turn')
            dice=p_dice()
            pp2+=dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            if pp2==100:
                print(p2,'Won')
                break
            elif pp1>100:
                pp2=pp2-dice
            print('You are at',pp2,'\n\n')
        turn+=1
#function call
play()