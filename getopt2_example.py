#!/usr/local/anaconda3/bin/python3
#

import sys
args=sys.argv

f1=open(args[1]+'.log','r')
line=f1.readline()

f2=open(args[1]+'.xyz','w')

c=0
d=0
while line:
    line=f1.readline()
    if 'ITR. 0' in line:
        while line:
            line=f1.readline()
            c+=1
            if 'Item' in line:
                f2.write(str(c-1)+'\n')
                f2.write(args[1]+'\n')
                break
    
    if 'Optimized' in line:
        while d<c-1:
            d+=1
            line=f1.readline()
            f2.write(line) 
