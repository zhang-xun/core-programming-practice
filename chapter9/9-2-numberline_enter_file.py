#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_
"""
    this file will show the NUMBER line when enter the XXX.XX file
    input : file_name and line_number

"""

import os.path


def main():
    file_name_var = input("please input your filename:")
    line_number_var = input("please input your line number")
    line_number_var = int(line_number_var)
    print(type(line_number_var))
    #full_file_name = os.path.curdir() + "/" + file_name_var
    f = open(file_name_var,"r")
    for i in f:
        if int(line_number_var) > 0:
            
            line_number_var = line_number_var -1
            print(f.readline())


if __name__ == "__main__":
    main()
