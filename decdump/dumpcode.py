import os
import sys
import decimal

def printable(c):
    if ord(c) >= 32 and ord(c) <-126:
        return c
    return '.'

def dumpdata(infile ,outfile):
    fi= open(infile, "r")
    fo= open(outfile, "w")

    for i in range(8):
        x=""
        y=""
        for j in range(16):
            c=fi.read(1)
            if c=="":
                x=x+"--- "
                y=y+' '
            else:
                x=x+str(ord(c)).zfill(3)+" "
                y=y+printable(c)
        fo.write(x+y+"\n")

    fi.close()
    fo.close()
    return