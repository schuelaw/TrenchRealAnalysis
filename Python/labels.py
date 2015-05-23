import re

source = open("trench-0.2.tex","r")
dest = open("trench-0.3.tex","w")

while True:
    line = source.readline()
    if len(line) == 0: break
    if line.find("sectionend:") != -1:
        line=line.replace("\label{sectionend:\\thesection}","")
    dest.write(line)
source.close()
dest.close()
