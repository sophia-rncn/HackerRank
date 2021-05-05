#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    if n <= 1 or n >=100:
        quit()
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0:
        if n in range(6, 21):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")