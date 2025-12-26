import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    result = "Not Weird"

    if n % 2 != 0:
        result = "Weird"
    else:
        if 6 <= n <= 20:
            result = "Weird"
        elif 2 <= n <= 5:
            result = "Not Weird"
        elif n > 20:
            result = "Not Weird"

    print(result)
