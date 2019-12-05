import os
import sys
import decimal
from dumpcode import *

VERSION = "DecDump v1.0.1"

if __name__ == "__main__":
    print VERSION+"\n"

    infile = sys.argv[1]
    outputdir = sys.argv[2]

    outfile = outputdir+"/"+"output.log"
    print "converting to decimal ASCII: "+infile+"\n"
    dumpdata(infile, outfile)

    print "  ** Done **\n"