from string import Template
from generator import *
import os
import uuid
pardon_list = ("template.tex","model.tex")
NUM = int(input("howmany?"))
fs = Template(r"""\documentclass{ctexart}
\pagestyle{empty}
\usepackage{array}
\usepackage{geometry}
\usepackage{tabularx}
\geometry{left = 1 cm, right = 1 cm, top = 1 cm, bottom = 1 cm}
\usepackage{multirow}

\begin{document}
$mao
\end{document}""")

with open("template.tex", "r", encoding="utf-8") as f:
    s = Template(f.read())

k = open(f"ans_With_{NUM}_Included.txt", "w+", encoding="utf-8")


def gene(auuid):
    otolist = [[GEN_oto() for i in range(6)] for i in range(10)]
    bignumlist = [[GEN_bignum() for i in range(1)] for i in range(5)]
    calist = [[GEN_CA() for i in range(5)] for i in range(8)]

    tran1 = '\\\\\n'.join(
        [' & '.join([f'${j[0]}=$' for j in i]) for i in otolist]) + '\\\\'

    tran2 = '\\\\\n'.join(
        [' & '.join([f'${j[0]}=$' for j in i]) for i in bignumlist]) + '\\\\'
    tran3 = '\\\\\n'.join(
        [' & '.join([f'${j[0]}=$' for j in i]) for i in calist]) + '\\\\'

    ans1 = '\n'.join(['\t'.join([str(j[1]) for j in i]) for i in otolist])

    ans2 = '\n'.join([' '.join([str(j[1]) for j in i]) for i in bignumlist])

    ans3 = '\n'.join([' '.join([str(j[1]) for j in i]) for i in calist])
    k.write(f"UID:{auuid}\n{ans1}\n{ans2}\n{ans3}\n\n")
    return s.safe_substitute(uid=auuid, tran1=tran1, tran2=tran2, tran3=tran3)


try:
    with open("trueOutput.tex", "w+", encoding="utf-8") as f:
        f.write(
            fs.safe_substitute(
                mao='\n'.join([gene(uuid.uuid4().urn[9:])
                               for i in range(NUM)])))
    os.system("xelatex trueOutput.tex")
    for i in filter(
            lambda x: any((x.endswith(j) for j in
                           ("tex", "log", "aux","gz"))) and x not in pardon_list,
            os.listdir()):
        os.remove(i)
finally:
    k.close()
