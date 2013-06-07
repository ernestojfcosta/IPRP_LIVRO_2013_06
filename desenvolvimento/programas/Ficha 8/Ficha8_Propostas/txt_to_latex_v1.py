'''
Created on 2009/11/05

@author: luis
'''

def converte_para_latex(paragrafo):
    latex_parag=paragrafo

    sdf=paragrafo.lstrip()
    if sdf!="":
        if paragrafo.isupper():
            latex_parag="\\title{"+paragrafo+"}\n\maketitle"
        elif sdf[0].isdigit():
            marca = True
            conta=0
            i=0
            while marca:
                if i%2==0:
                    if sdf[i].isdigit():
                        conta=conta+1
                    else:
                        marca=False
                else:
                    if sdf[i]!=".":
                        marca=False                  
                i=i+2
                    
            prefix_section="sub"*(conta-1)    
            latex_parag="\\"+prefix_section+"section{"+paragrafo[i-2:]+"}"
    return latex_parag
    

def converte_txt_para_latex(name_fich_in,name_fich_out):
    fich_in=open(name_fich_in,'r')
    fich_out=open(name_fich_out,'w')
    fich_out.write("\\documentclass[a4paper,10pt]{report}\n\n")
    fich_out.write("\\usepackage{color}\n\n")
    fich_out.write("\\begin{document}\n\n")

    for p in fich_in.read().split('\n'):
        fich_out.write(converte_para_latex(p))
        fich_out.write('\n\n')
        
    fich_out.write("\\end{document}\n");
    fich_in.close()
    fich_out.close()




if __name__ == '__main__':
    converte_txt_para_latex('text.txt','latex.tex')
    print "Done.."