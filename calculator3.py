#!/usr/bin/env python3
import sys

#ConfigName
JiShuH = JiShuL = YangLao = YiLiao = ShiYe = GongShang = ShengYu = GongJiJin = 0
#name basedon salary
SheBaomoney = taxmoney = finalmoney = salary1 = 0

#cal-function
def cal(salary):       
    #salary name
    global SheBaomoney,taxmoney,finalmoney,salary1
    global JiShuH,JiShuL,YangLao,YiLiao,ShiYe,GongShang,ShengYu,GongJiJin
    ratio = YangLao + YiLiao + ShiYe + ShengYu + GongShang + GongJiJin
    #choose which Jishu to use 
    if salary <= JiShuL:
        salary1 = JiShuL
    elif salary >= JiShuH:
        salary1 = JiShuH
    else:
        salary1 = salary
    #cal_taxmoney
    SheBaomoney = salary1 * ratio
    ifmoney = salary - SheBaomoney
    if ifmoney <= 3500:
        finalmoney = salary - SheBaomoney
    else:
        shallmoney = salary - SheBaomoney - 3500
        if shallmoney <= 1500:
            taxmoney = shallmoney * 0.03 - 0
        elif 1500 <= shallmoney <= 4500:
            taxmoney = shallmoney * 0.10 - 105 
        elif 4500 <= shallmoney <= 9000:
            taxmoney = shallmoney * 0.20 - 555 
        elif 9000 <= shallmoney <= 35000:
            taxmoney = shallmoney * 0.25 - 1005 
        elif 35000 <= shallmoney <= 55000:
            taxmoney = shallmoney * 0.30 - 2755
        elif 55000 <= shallmoney <= 80000:
            taxmoney = shallmoney * 0.35 - 5505
        else:
            taxmoney = shallmoney * 0.45 - 13505
        finalmoney = salary - SheBaomoney - taxmoney
        return finalmoney,SheBaomoney,taxmoney

#get_path(config/userinfo)
argvs = sys.argv[1:]
configfilepath_value = ''
userinfofilepath_value = ''
outfilepath_value = ''
for i,j in enumerate(sys.argv):
    if(i == 0):
        continue
    if(i == 2):
        configfilepath = j
    if(i == 4):
        userinfofilepath = j
    if(i == 6):
        outputfilepath = j

#get_configname_value
with open(configfilepath, 'r') as file:
    for line in file:        
        j = line.split('=')
        j[0] = j[0].strip()
        j[1] = j[1].strip()     # include('\n','\r','\t',' ')
        try:
            if j[0] == 'JiShuH':
                JiShuH = float(j[1])
            elif j[0] == 'JiShuL':
                JiShuL = float(j[1])
            elif j[0] == 'YangLao':
                YangLao = float(j[1])
            elif j[0] == 'YiLiao':
                YiLiao = float(j[1])
            elif j[0] == 'ShiYe':
                ShiYe = float(j[1])
            elif j[0] == 'GongShang':
                GongShang = float(j[1])
            elif j[0] == 'ShengYu':
                ShengYu = float(j[1])
            elif j[0] == 'GongJiJin':
                GongJiJin = float(j[1])
        except ValueError:
            print('Parameter Error')

#cal-salary with userinfo in JiShu
with open(userinfofilepath, 'r') as file:
    for line in file:
        j = line.split(',')
        startsalary = j[1].strip()
        try:
            cal(int(j[1]))
            finalmoney = format(finalmoney, ".2f")
            SheBaomoney = format(SheBaomoney, ".2f")
            taxmoney = format(taxmoney, ".2f")
            print(j[0]+','+startsalary+','+str(SheBaomoney)+','+str(taxmoney)+','+str(finalmoney))
            content = j[0]+','+startsalary+','+str(SheBaomoney)+','+str(taxmoney)+','+str(finalmoney)+'\n'
            with open(outputfilepath, 'a') as file:
                file.write(content)
        except ValueError:
            print('Parameter Error')                                                                

