#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_ 
"""
    cout a file : how many lines in that files
"""
def count_line(file_name):
    return sum( 1  for line in open(file_name) )





if __name__ == "__main__":
    filename = input("please input the filename")

    lines = count_line(filename)
    print(lines)
