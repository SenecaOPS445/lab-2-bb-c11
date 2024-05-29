#!/usr/bin/env python3

# Author:[Bishwash BC]
# Author ID: [184751212]
# Date Created: [2024/05/28]

import sys

if len(sys.argv) == 1:
    timer = 3

elif len(sys.argv) == 2:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')

