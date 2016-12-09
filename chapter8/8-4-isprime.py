#!  /usr/local/bin/python3
# _*_ coding:utf-8 _*_
import math
import os

"""
    this file  is a prime test function: 
"""
def main():
    '''
        main entrance
    '''
    print(isprime(110))
    
    print(isprime(111))
    print(isprime(112))
    

def isprime(number):
    """
    parameter: int number
    return True/Fase
    """
    sqrt_number = int(math.sqrt(number))
    flag = False
    print(sqrt_number)
    for i in range(2, sqrt_number): 
        if number % i == 0:
            print(i)
            flag = True
            break
    return flag

        
    


if __name__ == '__main__':
    #test1=isprime(110)
    #print((test1))
    print(isprime(1232141241231))
