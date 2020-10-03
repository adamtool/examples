# Transforms the .gml files from http://www.topology-zoo.org into LTS in APT format 
import os

def transformFile(file):
    name = str(file)
    file = open("TOPOLOGY ZOO/" + name + ".gml", "r")
    lines = file.readlines()
    file.close()

    countNodes = 0
    source = 0
    target = 0
    edges = []
    for line in lines:
        if line.startswith( "  node"):
            countNodes = countNodes + 1
        if line.startswith( "    source "):
            s = line.replace("    source ", "")
            source = int(s)
        if line.startswith( "    target "):
            t = line.replace("    target ", "")
            target = int(t)
            edges.append([source,target])

    newfile = open("TOPOLOGY ZOO/" + name + ".apt","w")
    newfile.write(".name \"" + name + "\"\n")
    newfile.write(".type LTS\n")
    newfile.write(".states\n")
    for x in range(0, countNodes):
        if x == 0:
             newfile.write("sw%03d[initial]\n" % x)
        else:
            newfile.write("sw%03d\n" % x)
    newfile.write(".labels\n")
    edgesSet = set(tuple(e) for e in edges)
    for x in range(0, len(edgesSet) * 2):
        newfile.write("fwd%03d\n" % x)
    newfile.write(".arcs\n")
    x = 0
    for edge in edgesSet:
        newfile.write("sw%03d fwd%03d sw%03d\n" %(edge[0], x, edge[1]))
        newfile.write("sw%03d fwd%03d sw%03d\n" %(edge[1], len(edgesSet) + x, edge[0]))
        x = x + 1

def main():
    for file in os.listdir("TOPOLOGY ZOO"):
        fileName = str(file)
        transformFile(fileName.replace(".gml",""))

main()
