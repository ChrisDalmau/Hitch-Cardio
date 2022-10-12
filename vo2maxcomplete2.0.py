#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:50:12 2022

@author: christopherdalmau
"""

import matplotlib.pyplot as plt
import sys


lista = list()
listb = list()

gender = input("Enter your gender(M/W)")
age = int(input("Enter your age"))

resthr = int(input("Enter your resting heart rate: "))
maxhr = int(input("enter your max heart rate: "))
try:
    vo2max = (maxhr / resthr) * 15.3
except ZeroDivisionError:
    sys.exit()

lista.append(1)
listb.append(vo2max)

i = 2
    

if(gender == "M"):
    if (age >= 18) and (age <= 25):
        if (vo2max > 60):
            print("Your vo2max is excellent keep up the good work")
        elif(vo2max >=52) and (vo2max <=60):
            print("Your vo2 max is good. Keep up the good work")
        elif(vo2max>=37) and (vo2max<=51):
            print("Your vo2 max is average.")
        elif(vo2max>=30) and (vo2max <=36):
            print("Your vo2 max is not good. Try hard to get back on track.")
        elif(vo2max<30):
            print("Your vo2max is very bad. Work hard to get better.")
    elif (age >= 26) and (age <= 35):
        if (vo2max > 56):
            print("Your vo2max is excellent keep up the good work")
        elif(vo2max >=49) and (vo2max <=56):
            print("Your vo2 max is good. Keep up the good work")
        elif(vo2max>=35) and (vo2max<=48):
            print("Your vo2 max is average.")
        elif(vo2max>=30) and (vo2max <=34):
            print("Your vo2 max is not good. Try hard to get back on track.")
        elif(vo2max<30):
            print("Your vo2max is very bad. Work hard to get better.")
    elif (age >= 36) and (age <= 45):
        if (vo2max > 51):
            print("Your vo2max is excellent keep up the good work")
        elif(vo2max >=43) and (vo2max <=51):
            print("Your vo2 max is good. Keep up the good work")
        elif(vo2max>=31) and (vo2max<=42):
            print("Your vo2 max is average.")
        elif(vo2max>=26) and (vo2max <=30):
            print("Your vo2 max is not good. Try hard to get back on track.")
        elif(vo2max<26):
            print("Your vo2max is very bad. Work hard to get better.")
    elif (age >= 46) and (age <= 55):
        if (vo2max > 45):
            print("Your vo2max is excellent keep up the good work")
        elif(vo2max >=39) and (vo2max <=45):
            print("Your vo2 max is good. Keep up the good work")
        elif(vo2max>=29) and (vo2max<=38):
            print("Your vo2 max is average.")
        elif(vo2max>=25) and (vo2max <=28):
            print("Your vo2 max is not good. Try hard to get back on track.")
        elif(vo2max<25):
            print("Your vo2max is very bad. Work hard to get better.")
    elif (age >= 56) and (age <= 65):
        if (vo2max > 41):
            print("Your vo2max is excellent keep up the good work")
        elif(vo2max >=36) and (vo2max <=41):
            print("Your vo2 max is good. Keep up the good work")
        elif(vo2max>=26) and (vo2max<=35):
            print("Your vo2 max is average.")
        elif(vo2max>=22) and (vo2max <=25):
            print("Your vo2 max is not good. Try hard to get back on track.")
        elif(vo2max<22):
            print("Your vo2max is very bad. Work hard to get better.")
    elif (age > 65):
        if (vo2max > 37):
            print("Your vo2max is excellent keep up the good work")
        elif(vo2max >=33) and (vo2max <=37):
            print("Your vo2 max is good. Keep up the good work")
        elif(vo2max>=22) and (vo2max<=32):
            print("Your vo2 max is average.")
        elif(vo2max>=20) and (vo2max <=21):
            print("Your vo2 max is not good. Try hard to get back on track.")
        elif(vo2max<20):
            print("Your vo2max is very bad. Work hard to get better.")

if(gender == "W"):
    if (age >= 18) and (age <= 25):
        if (vo2max > 56):
            print("Your vo2max is excellent keep up the good work")
        elif(vo2max >=47) and (vo2max <=56):
            print("Your vo2 max is good. Keep up the good work")
        elif(vo2max>=33) and (vo2max<=46):
            print("Your vo2 max is average.")
        elif(vo2max>=28) and (vo2max <=32):
            print("Your vo2 max is not good. Try hard to get back on track.")
        elif(vo2max<28):
            print("Your vo2max is very bad. Work hard to get better.")
    elif (age >= 26) and (age <= 35):
        if (vo2max > 52):
            print("Your vo2max is excellent keep up the good work")
        elif(vo2max >=45) and (vo2max <=52):
            print("Your vo2 max is good. Keep up the good work")
        elif(vo2max>=31) and (vo2max<=44):
            print("Your vo2 max is average.")
        elif(vo2max>=26) and (vo2max <=30):
            print("Your vo2 max is not good. Try hard to get back on track.")
        elif(vo2max<26):
            print("Your vo2max is very bad. Work hard to get better.")
    elif (age >= 36) and (age <= 45):
        if (vo2max > 45):
            print("Your vo2max is excellent keep up the good work")
        elif(vo2max >=38) and (vo2max <=45):
            print("Your vo2 max is good. Keep up the good work")
        elif(vo2max>=27) and (vo2max<=37):
            print("Your vo2 max is average.")
        elif(vo2max>=22) and (vo2max <=26):
            print("Your vo2 max is not good. Try hard to get back on track.")
        elif(vo2max<22):
            print("Your vo2max is very bad. Work hard to get better.")
    elif (age >= 46) and (age <= 55):
        if (vo2max > 40):
            print("Your vo2max is excellent keep up the good work")
        elif(vo2max >=32) and (vo2max <=37):
            print("Your vo2 max is good. Keep up the good work")
        elif(vo2max>=25) and (vo2max<=31):
            print("Your vo2 max is average.")
        elif(vo2max>=20) and (vo2max <=24):
            print("Your vo2 max is not good. Try hard to get back on track.")
        elif(vo2max<20):
            print("Your vo2max is very bad. Work hard to get better.")
    elif (age >= 56) and (age <= 65):
        if (vo2max > 37):
            print("Your vo2max is excellent keep up the good work")
        elif(vo2max >=32) and (vo2max <=37):
            print("Your vo2 max is good. Keep up the good work")
        elif(vo2max>=22) and (vo2max<=31):
            print("Your vo2 max is average.")
        elif(vo2max>=18) and (vo2max <=21):
            print("Your vo2 max is not good. Try hard to get back on track.")
        elif(vo2max<18):
            print("Your vo2max is very bad. Work hard to get better.")
    elif (age > 65):
        if (vo2max > 32):
            print("Your vo2max is excellent keep up the good work")
        elif(vo2max >=28) and (vo2max <=32):
            print("Your vo2 max is good. Keep up the good work")
        elif(vo2max>=19) and (vo2max<=27):
            print("Your vo2 max is average.")
        elif(vo2max>=17) and (vo2max <=18):
            print("Your vo2 max is not good. Try hard to get back on track.")
        elif(vo2max<17):
            print("Your vo2max is very bad. Work hard to get better.")
        

while resthr >= 0:
    
    resthr = int(input("Enter your resting heart rate: "))
    maxhr = int(input("enter your max heart rate: "))
    vo2max = int()
    try:
        vo2max = (maxhr / resthr) * 15.3
    except ZeroDivisionError:
        sys.exit()
    lista.append(i)
    listb.append(vo2max)
    plt.plot(lista,listb)
    plt.show()
    i += 1
    if(gender == "M"):
        if (age >= 18) and (age <= 25):
            if (vo2max > 60):
                print("Your vo2max is excellent keep up the good work")
            elif(vo2max >=52) and (vo2max <=60):
                print("Your vo2 max is good. Keep up the good work")
            elif(vo2max>=37) and (vo2max<=51):
                print("Your vo2 max is average.")
            elif(vo2max>=30) and (vo2max <=36):
                print("Your vo2 max is not good. Try hard to get back on track.")
            elif(vo2max<30):
                print("Your vo2max is very bad. Work hard to get better.")
        elif (age >= 26) and (age <= 35):
            if (vo2max > 56):
                print("Your vo2max is excellent keep up the good work")
            elif(vo2max >=49) and (vo2max <=56):
                print("Your vo2 max is good. Keep up the good work")
            elif(vo2max>=35) and (vo2max<=48):
                print("Your vo2 max is average.")
            elif(vo2max>=30) and (vo2max <=34):
                print("Your vo2 max is not good. Try hard to get back on track.")
            elif(vo2max<30):
                print("Your vo2max is very bad. Work hard to get better.")
        elif (age >= 36) and (age <= 45):
            if (vo2max > 51):
                print("Your vo2max is excellent keep up the good work")
            elif(vo2max >=43) and (vo2max <=51):
                print("Your vo2 max is good. Keep up the good work")
            elif(vo2max>=31) and (vo2max<=42):
                print("Your vo2 max is average.")
            elif(vo2max>=26) and (vo2max <=30):
                print("Your vo2 max is not good. Try hard to get back on track.")
            elif(vo2max<26):
                print("Your vo2max is very bad. Work hard to get better.")
        elif (age >= 46) and (age <= 55):
            if (vo2max > 45):
                print("Your vo2max is excellent keep up the good work")
            elif(vo2max >=39) and (vo2max <=45):
                print("Your vo2 max is good. Keep up the good work")
            elif(vo2max>=29) and (vo2max<=38):
                print("Your vo2 max is average.")
            elif(vo2max>=25) and (vo2max <=28):
                print("Your vo2 max is not good. Try hard to get back on track.")
            elif(vo2max<25):
                print("Your vo2max is very bad. Work hard to get better.")
        elif (age >= 56) and (age <= 65):
            if (vo2max > 41):
                print("Your vo2max is excellent keep up the good work")
            elif(vo2max >=36) and (vo2max <=41):
                print("Your vo2 max is good. Keep up the good work")
            elif(vo2max>=26) and (vo2max<=35):
                print("Your vo2 max is average.")
            elif(vo2max>=22) and (vo2max <=25):
                print("Your vo2 max is not good. Try hard to get back on track.")
            elif(vo2max<22):
                print("Your vo2max is very bad. Work hard to get better.")
        elif (age > 65):
            if (vo2max > 37):
                print("Your vo2max is excellent keep up the good work")
            elif(vo2max >=33) and (vo2max <=37):
                print("Your vo2 max is good. Keep up the good work")
            elif(vo2max>=22) and (vo2max<=32):
                print("Your vo2 max is average.")
            elif(vo2max>=20) and (vo2max <=21):
                print("Your vo2 max is not good. Try hard to get back on track.")
            elif(vo2max<20):
                print("Your vo2max is very bad. Work hard to get better.")

    if(gender == "W"):
        if (age >= 18) and (age <= 25):
            if (vo2max > 56):
                print("Your vo2max is excellent keep up the good work")
            elif(vo2max >=47) and (vo2max <=56):
                print("Your vo2 max is good. Keep up the good work")
            elif(vo2max>=33) and (vo2max<=46):
                print("Your vo2 max is average.")
            elif(vo2max>=28) and (vo2max <=32):
                print("Your vo2 max is not good. Try hard to get back on track.")
            elif(vo2max<28):
                print("Your vo2max is very bad. Work hard to get better.")
        elif (age >= 26) and (age <= 35):
            if (vo2max > 52):
                print("Your vo2max is excellent keep up the good work")
            elif(vo2max >=45) and (vo2max <=52):
                print("Your vo2 max is good. Keep up the good work")
            elif(vo2max>=31) and (vo2max<=44):
                print("Your vo2 max is average.")
            elif(vo2max>=26) and (vo2max <=30):
                print("Your vo2 max is not good. Try hard to get back on track.")
            elif(vo2max<26):
                print("Your vo2max is very bad. Work hard to get better.")
        elif (age >= 36) and (age <= 45):
            if (vo2max > 45):
                print("Your vo2max is excellent keep up the good work")
            elif(vo2max >=38) and (vo2max <=45):
                print("Your vo2 max is good. Keep up the good work")
            elif(vo2max>=27) and (vo2max<=37):
                print("Your vo2 max is average.")
            elif(vo2max>=22) and (vo2max <=26):
                print("Your vo2 max is not good. Try hard to get back on track.")
            elif(vo2max<22):
                print("Your vo2max is very bad. Work hard to get better.")
        elif (age >= 46) and (age <= 55):
            if (vo2max > 40):
                print("Your vo2max is excellent keep up the good work")
            elif(vo2max >=32) and (vo2max <=37):
                print("Your vo2 max is good. Keep up the good work")
            elif(vo2max>=25) and (vo2max<=31):
                print("Your vo2 max is average.")
            elif(vo2max>=20) and (vo2max <=24):
                print("Your vo2 max is not good. Try hard to get back on track.")
            elif(vo2max<20):
                print("Your vo2max is very bad. Work hard to get better.")
        elif (age >= 56) and (age <= 65):
            if (vo2max > 37):
                print("Your vo2max is excellent keep up the good work")
            elif(vo2max >=32) and (vo2max <=37):
                print("Your vo2 max is good. Keep up the good work")
            elif(vo2max>=22) and (vo2max<=31):
                print("Your vo2 max is average.")
            elif(vo2max>=18) and (vo2max <=21):
                print("Your vo2 max is not good. Try hard to get back on track.")
            elif(vo2max<18):
                print("Your vo2max is very bad. Work hard to get better.")
        elif (age > 65):
            if (vo2max > 32):
                print("Your vo2max is excellent keep up the good work")
            elif(vo2max >=28) and (vo2max <=32):
                print("Your vo2 max is good. Keep up the good work")
            elif(vo2max>=19) and (vo2max<=27):
                print("Your vo2 max is average.")
            elif(vo2max>=17) and (vo2max <=18):
                print("Your vo2 max is not good. Try hard to get back on track.")
            elif(vo2max<17):
                print("Your vo2max is very bad. Work hard to get better.")
    

    