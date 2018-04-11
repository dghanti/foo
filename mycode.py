import json
from pprint import pprint
import pandas as pd

import sys
def main(argv):
    header = "\\documentclass{article}\n\\usepackage{pgfplots}\n\\pgfplotsset{compat=1.7}\n \\pagenumbering{gobble}\n"

    opentags = "\\begin{document}\n\\begin{tikzpicture}[scale=1.5,\n declare function={binom(\\k,\\n,\\p)=\\n!/(\\k!*(\\n-\\k)!)*\\p^\\k*(1-\\p)^(\\n-\\k);}\n ]\n"

    maincode = "\\draw[->] (-2.2,0) -- (8,0) node[right] {$x$};\n\\draw[->] (0,-0.2) -- (0,8) node[above] {$p(x)$};\n\\draw[style=help lines] (0,0) grid (7, 6) (4,4) grid +(1,1);\n     \\begin{axis}[\n samples at={0,...,"+sys.argv[1]+"},\n ybar=0pt, bar width=1,\n axis x line=center,\n axis y line=center,\n title style={at={(0.6,0)},anchor=north,yshift=-5ex},\n title=\LARGE{Binomial Distribution}\n ]\n \\addplot [fill=blue!50, fill opacity=0.5] {binom(x, "+sys.argv[1]+", "+sys.argv[2]+")}; \\addlegendentry{$p="+sys.argv[2]+"$}\n \\addplot [fill=red!50, fill opacity=0.5] {binom(x, "+sys.argv[1]+", "+sys.argv[3]+")}; \\addlegendentry{$p="+sys.argv[3]+"$}\n \\addplot [no marks,fill,blue!40,smooth,fill opacity=0.2,samples="+sys.argv[1]+"] {binom(x, "+sys.argv[1]+","+sys.argv[2]+")}\closedcycle;\n \\addplot [no marks,fill,red!40,smooth,fill opacity=0.2,samples="+sys.argv[1]+"] {binom(x, "+sys.argv[1]+","+sys.argv[3]+")}\closedcycle;\n \\end{axis}\n"
    
    other1 = "\\fill[black] (5.05cm, 100pt) node [below right,fill=white,yshift=-4pt] {$\\displaystyle p(x) = {n \\choose x}\\theta^x(1 - \\theta)^{n-x}$};\n"
    
    other2 = "\\begin{flushright}\n \\def\\arraystretch{1.1}\n \\begin{tabular}{rl}\n Samples:  & $\\{0,1,\\ldots,n\\}$\\\\\n $\\mu$:  & $n \\theta$\\\\\n $\\sigma^2$:  &  $n \\theta(1-\\theta)$\n \\end{tabular}\n \\end{flushright}\n"
    
    closetags = "\\end{tikzpicture}\n"+other2+"\\end{document}\n"

    copyright = "\\node [below right,black,xshift=75ex,yshift=-10ex]{\\tiny \\textcopyright diagram.ai};\n"

# print header+"\n"+opentags+"\n"+maincode+"\n"+other1+"\n"+copyright+"\n"+closetags


df=pd.read_json('distributions.json')
df.drop(df.head(1).index, inplace=True)
print df

#data = json.load(open('distributions.json'))
#pprint(data)

if __name__== "__main__":
    main(sys.argv[1:])
