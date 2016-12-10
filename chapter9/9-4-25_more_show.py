#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_ 

import os
def show(filename):
    """
        25 lines stop util any key pressed!
        input: file of a name
        output: show text
    """
    flag = 0
    with open(filename,"r") as f:
        for line in f:
            
            if flag == 25: 
                os.system("read -s -n 1 -p 'press any key to continue '")
                flag = 0
                continue
            else:
                print(line.strip())
                flag+=1
                


if __name__ == "__main__":
    filename = input("please input filename:")
    show(filename)
