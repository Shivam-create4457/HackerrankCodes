#!/bin/python3

import math
import os
import random
import re
import sys

def identyChar(n):
    if n%2==0 and (n in  range(2,6) or n>20):
        print('Not Weird')
    else:
        print('Weird')

if __name__ == '__main__':
    n = int(input().strip())
    identyChar(n)
