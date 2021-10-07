import streamlit as st
import numpy as np
import pandas as pd
import re
st.title("Web Cutter by Team2")
seqs=""
user_input = st.text_input("Sequence goes here",seqs)



def restriction_sites(seq, recog_seq):
    #Searching the indices of all restriction_sites in a sequence
    sites = []
    for site in re.finditer(recog_seq, seq):
        sites.append(site.start()+1)     #Storing The index of each restrictive Enzyme
        
    return sites


if __name__ == '__main__':
    
    
    # Storing Enzyme name and its recognition sequence in a dictionary
    
    name = {"GAATTC":"ECoRI","CCAGG":"EcoRII","CCTGG":"EcoRII","GGATCC":"BamHI","AAGCTT":"HindIII","TCGA":"TaqI","GCGGCCGC":"NotI","GANTC":"HinFI","GATC":"Sau3AI","CAGCTG":"PvuII*","CCCGGG":"SmaI","GGCC":"HaeIII","GACGC":"Hgal","AGCT":"Alul","GATATC":"EcoRV","CAGCAGN25NN":"EcoP151","GGTACC":"Kpnl","CTGCAG":"Pstl","GAGCTC":"Sacl","GTCGAC":"Sall","AGTACT":"Scal","ACTAGT":"Spel","GCATGC":"Sphl","AGGCCT":"Stul","TCTAGA":"Xbal"}       
    rec_seq_all = ["GAATTC","CCAGG","CCTGG","GGATCC","AAGCTT","TCGA","GCGGCCGC","GANTC","GATC","CAGCTG","CCCGGG","GGCC","GACGC","AGCT","GATATC","CAGCAGN25NN","GGTACC","CTGCAG","GAGCTC","GTCGAC","AGTACT","ACTAGT","GCATGC","AGGCCT","TCTAGA"]

    Table=dict()
    positions=list()
    noofcuts=list()
    enzymes=list()

    for n in rec_seq_all:
        Table[n]=restriction_sites(user_input,n)
        positions.append(Table[n])
        noofcuts.append(len(Table[n]))
        enzymes.append(name[n])
        print(f"{name[n]}   {len(Table[n])}  {Table[n]} {n.lower()}")
    
    #exporting the output file in csv format
    
    
    data={'Enzyme Name':enzymes,'No. of cuts':noofcuts,'Positions Of sites':positions,'Recognition Sequence':rec_seq_all}

    Rtable=pd.DataFrame(data,columns=['Enzyme Name','No. of cuts','Positions Of sites','Recognition Sequence'])
    
    Rtable.to_csv("Output.csv")
    df = pd.read_csv("Output.csv")  # read a CSV file inside the 'data" folder next to 'app.py'


    st.title("Analysis")  # add a title
    st.write(df)  # visualize my dataframe in the Streamlit app