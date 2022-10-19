#!/usr/bin/env python
# coding: utf-8

# In[217]:


import pandas as pd
cn20 = pd.read_csv('./2--1210个样本号和N20,位置信息.csv', sep = ',',encoding='utf-8') 


# In[218]:


new_n20 = []
for i in range(len(cn20['Target sequences'])):
    new_n20.append(cn20['Target sequences'][i].strip()[-20:])


# In[219]:


cn20['Target sequences'] = new_n20


# In[220]:


seq_sample = {}
seqs = cn20['Target sequences']
samples = cn20['Samples']
for i in range(len(seqs)):
    seq_sample[samples[i]] = seqs[i]


# In[306]:


import pandas as pd
data3 = pd.read_table(r'./3--_T_Primers--引物和基因片段染色质位置表.csv', sep=',', error_bad_lines=False)
data4 = pd.read_table(r'./4--G_A_Primers--引物和基因片段染色质位置表.csv', sep=',', error_bad_lines=False) 
data3['n20'] = data3['N20PAM'].apply(lambda x: x.strip()[:20])
data4['n20'] = data4['N20PAM'].apply(lambda x: x.strip()[:20])
n201 = data3['n20']
n202 = data4['n20']
full1 = data3['Pages']
full2 = data4['Pages']
dic = {}
for i in range(len(n201)):
    dic.setdefault(n201[i],full1[i])
for i in range(len(n202)):
    dic.setdefault(n202[i],full2[i])


# In[321]:


data3['n20'] = data3['N20PAM'].apply(lambda x: x.strip()[:20])
data4['n20'] = data4['N20PAM'].apply(lambda x: x.strip()[:20])

n3ct = data3['CtoTorGtoA']
nchr = data3['CHROMOSOME']
ncp = data3['CHROM_POSITION']
np = data3['N20PAM']
si = data3['SITE']
acc = data3['ACCESSION']
n320 = data3['n20']

n4ct = data4['CtoTorGtoA']
n4chr = data4['CHROMOSOME']
n4cp = data4['CHROM_POSITION']
n4p = data4['N20PAM']
si4 = data4['SITE']
acc4 = data4['ACCESSION']
n420 = data4['n20']

dicCTGA = {}
dicChro = {}
dicChroP = {}
dicN20Pam = {}
dicSite = {}
dicAcc = {}

for i in range(len(n320)):
    dicCTGA.setdefault(n320[i],nct[i])
    dicChro.setdefault(n320[i],nchr[i])
    dicChroP.setdefault(n320[i],ncp[i])
    dicN20Pam.setdefault(n320[i],np[i])
    dicSite.setdefault(n320[i],si[i])
    dicAcc.setdefault(n320[i],acc[i])
for i in range(len(n420)):
    dicCTGA.setdefault(n420[i],n4ct[i])
    dicChro.setdefault(n420[i],n4chr[i])
    dicChroP.setdefault(n420[i],n4cp[i])
    dicN20Pam.setdefault(n420[i],n4p[i])
    dicSite.setdefault(n420[i],si4[i])
    dicAcc.setdefault(n420[i],acc4[i])
    
CTGAL,CHROL,CHROPL,N20PAML,SITEL,ACCL = [],[],[],[],[],[]

for i in range(len(cn20['Target sequences'])):
    try:
        n20 = cn20['Target sequences'][i]
        CTGAL.append(dicCTGA[n20])
        CHROL.append(dicChro[n20])
        CHROPL.append(dicChroP[n20])
        N20PAML.append(dicN20Pam[n20])
        SITEL.append(dicSite[n20])
        ACCL.append(dicAcc[n20])

    except:
        CTGAL.append('error')
        CHROL.append('error')
        CHROPL.append('error')
        N20PAML.append('error')
        SITEL.append('error')
        ACCL.append('error')


# In[240]:


full0 = []
for i in range(len(cn20['Target sequences'])):
    try:
        n20 = cn20['Target sequences'][i]
        full0.append(dic[n20])
    except:
        full0.append('error')


# In[241]:


cn20['Pages'] = full0


# In[242]:


cn20.to_csv('./pages.csv')


# In[243]:


primer1l = []
primer1r = []
primer2l = []
primer2r = []
primer3l = []
primer3r = []
for i in range(len(full0)):
    s = full0[i]

    try:
        s1 = s.split('1 LEFT PRIMER')[1].split('2 LEFT PRIMER')[0]
        s2 = s.split('2 LEFT PRIMER')[1].split('3 LEFT PRIMER')[0]
        s3 = s.split('3 LEFT PRIMER')[1].split('4 LEFT PRIMER')[0]
        s1l = s1.split('RIGHT PRIMER')[0].split('0.00')[-1]
        s2l = s2.split('RIGHT PRIMER')[0].split('0.00')[-1]
        s3l = s3.split('RIGHT PRIMER')[0].split('0.00')[-1]
        s1r = s1.split('PRODUCT SIZE')[0].split('0.00')[-1]
        s2r = s2.split('PRODUCT SIZE')[0].split('0.00')[-1]
        s3r = s3.split('PRODUCT SIZE')[0].split('0.00')[-1]
        primer1l.append(s1l.strip())
        primer1r.append(s1r.strip())
        primer2l.append(s2l.strip())
        primer2r.append(s2r.strip())
        primer3l.append(s3l.strip())
        primer3r.append(s3r.strip())
#     print(s1,s2,s3,s1l,s2l,s3l,s1r,s2r,s3r)
    except:
        primer1l.append('error')
        primer1r.append('error')
        primer2l.append('error')
        primer2r.append('error')
        primer3l.append('error')
        primer3r.append('error')
#     print(i)


# In[244]:


cn20['primer1l'] = primer1l
cn20['primer1r'] = primer1r
cn20['primer2l'] = primer2l
cn20['primer2r'] = primer2r
cn20['primer3l'] = primer3l
cn20['primer3r'] = primer3r


# In[250]:


cn20.to_csv('./cn20.csv')


# In[251]:


import pandas as pd

finddf = pd.read_table(r'./67.csv', sep=',', error_bad_lines=False)


# In[252]:


numberl = []
findl = []
for i in finddf['lookup']:
    try:
        numberl.append(int(i))
    except:
        findl.append(i.split(' ')[-1])


# In[253]:


numberl = []
findl = []
look = finddf['lookup']
for i in range(len(look)):
    if i%2 == 0:
        numberl.append(look[i])
    else:
        findl.append(look[i].split(' ')[-1])


# In[254]:


finddic = {}
for i in range(len(findl)):
    finddic.setdefault(int(numberl[i]),findl[i])


# In[255]:


import collections
od = collections.OrderedDict(sorted(finddic.items()))


# In[257]:


fin = []
sam = cn20['Samples']
for i in sam:
    try:
        fin.append(finddic[i])
    except:
        fin.append('error')


# In[258]:


cn20['find'] = fin


# In[260]:


cn20.to_csv('./cn202.csv')


# In[282]:


finddf = pd.read_excel(r'./cn202.xls', sep=',', error_bad_lines=False)


# In[293]:


fl = []
fr = []
p1l = finddf['primer1l']
p1r = finddf['primer1r']
p2l = finddf['primer2l']
p2r = finddf['primer2r']
find = finddf['6find']
for i in range(len(find)):
    if find[i]!='unfound':
        fl.append(p1l[i])
        fr.append(p1r[i])
    else:
        fl.append(p2l[i])
        fr.append(p2r[i])


# In[296]:


finddf['final left primer'] = fl
finddf['final right primer'] = fr


# In[325]:


finddf.to_csv('./Full information.csv')


# In[323]:


finddf['CtoT_GtoA'] = CTGAL
finddf['Chromosome'] = CHROL
finddf['Chromosome position'] = CHROPL
finddf['N20PAM'] = N20PAML
finddf['Site'] = SITEL
finddf['Accession'] = ACCL


# In[334]:


finddf = pd.read_excel(r'./Full information.xls', sep=',', error_bad_lines=False)


# In[336]:


table1 = finddf[['Samples','Chromosome','Target sequences','FULL']]
table1.to_excel('./table1.xls')


# In[337]:


table2 = finddf[['Samples','primer1l','primer1r','primer2l','primer2r','primer3l','primer3r']]
table2.to_excel('./table2.xls')


# In[366]:


table3 = finddf[['Samples','Target sequences','Plates-96','Sites','5contain']]
table3 = table3[table3['5contain']=='in']
table3 = table3[['Samples','Target sequences','Plates-96','Sites']]
table3.to_excel('./table3.xls')


# In[367]:


table4 = finddf[['Samples','Target sequences','Sites-96Plates','Sites-48Plates','5contain']]
table4 = table4[table4['5contain']!='in']
table4 = table4[['Samples','Target sequences','Sites-96Plates','Sites-48Plates']]
table4.to_excel('./table4.xls')


# In[350]:


table5 = finddf[['Samples','Target sequences','Efficiencies','6find']]
table5 = table5[table5['6find']!='unfound']
table5 = table5[['Samples','Target sequences','Efficiencies']]

table5.to_excel('./table5.xls')


# In[351]:


table6 = finddf[['Samples','Target sequences','Plates-96','Sites','6find']]
table6 = table6[table6['6find']=='unfound']
table6 = table6[['Samples','Target sequences','Plates-96','Sites']]

table6.to_excel('./table6.xls')


# In[353]:


table7 = finddf[['Samples','primer2l','primer2r','6find']]
table7 = table7[table7['6find']=='unfound']
table7 = table7[['Samples','primer2l','primer2r']]


# In[358]:


Sites_2F = []
Primer_2R = []

alphal = ['A','B','C','D','E','F','G','H']
# alphalist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
j = 0
a = 0
for i in range(len(table7)):
#     first_letter = alphalist[a]
    if j%(8*12)==0:
        a+=1
    i = i%8 
    letter = alphal[i]
    i +=1
    j+=1
    Acount = str(a)+'A'+'-'+letter+str(i)
    Bcount = str(a)+'B'+'-'+letter+str(i)
    Sites_2F.append(Acount)
    Primer_2R.append(Bcount)
table7['Sites_2F'] = Sites_2F
table7['Primer_2R'] = Primer_2R

table7.to_excel('./table7.xls')

