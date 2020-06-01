# create json object
# fill in json parts
# write to file
import os, sys
import json, datetime

VERSION = "Metadata generator v1.0.0"

def parse(infile, outfile):

    fo= open(outfile, "w")
    metadata = {}

    metadata["type"] = "Feature"
    geometry  = {}
    geometry["type"] = "Point"
    geometry["coordinates"] = [107.3,222.4]
    metadata["geometry"] = geometry
    properties = {}
    properties["dataStarted"] = (datetime.datetime.now() - datetime.timedelta(minutes=5)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    properties["dataEnded"] = (datetime.datetime.now() - datetime.timedelta(minutes=3)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    properties["dataTypes"] = ["one", "two"]
    metadata["properties"] = properties

    fo.write(json.dumps(metadata))
    fo.close()
    return

if __name__ == "__main__":
    print VERSION+"\n"

    infile = sys.argv[1]
    outputdir = sys.argv[2]

    outfile = outputdir+"/INPUT_FILE.metadata.json"
    print "writing metadata to "+outfile
    outlog = outputdir+"/"+"output.log"
    fo= open(outlog, "w+")
    print "Generating random metadata for file: "+infile+"\n"
    fo.write("Generating random metadata for file: "+infile+"\n")
    print "writing metadata to "+outfile+"\n"
    fo.write("writing metadata to "+outfile+"\n")
    fo.close()
    parse(infile, outfile)

    print "  ** Done **\n"