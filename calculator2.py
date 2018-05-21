#!/usr/bin/env python3
import sys

def cal(salary):

    ifmoney = salary - salary * (0.08 + 0.02 + 0.005 + 0.06)
    if ifmoney <= 3500:
        finalmoney = salary - salary * (0.08 + 0.02 + 0.005 + 0.06)
        finalmoney = format(finalmoney, ".2f")
        return finalmoney
    else:
        shallmoney = salary - salary * (0.08 + 0.02 + 0.005 + 0.06) - 3500
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
    finalmoney = salary -  salary * (0.08 + 0.02 + 0.005 + 0.06) - taxmoney
    finalmoney = format(finalmoney, ".2f")
    return finalmoney

if __name__ == '__main__':
    allsalary = sys.argv[1:]
    for i in allsalary:
        j = i.split(':')
        try:
            j[1] = cal(int(j[1])) 
            print(j[0] + ':' + j[1])
        except ValueError:
            print('Parameter Error')
