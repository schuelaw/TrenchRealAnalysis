import re

source = open("trench-0.1.tex","r")
dest = open("trench-0.2.tex","w")

i = 0
while True:
    line = source.readline()
    if len(line) == 0: break
    if line.find("centereps") != -1:
        params = re.findall(r'{(.+?)}',line)
        params[2]=params[2].replace("eps","png")
        newline="\\begin{center}\n"+\
        "\includegraphics[width="+params[0]+",height="+params[1]+\
                "]{png/"+params[2]+"}" + "\n\end{center}"
        dest.write(newline+"\n")
    else:
        dest.write(line)

dest.close()
source.close()
