# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 13:37:18 2023

@author: Box White
"""

import tkinter
from tkinter import scrolledtext
import csv

#空間の性質を表す概念の名前を格納したリスト

SpaceName = ['Compact','Hausdorff','MetricSpace','T0','T1','T2'
             ,'T3','T4','T5','Separable','Lindeloef','LocallyCompact'
             ,'UniformSpace','Complete','SecondCountable','Regular',
             'BaireSpace','Normal','SemitopologicalGroup',
             'TopologicalGroup']
"""
CSVファイルから情報を読み取り,定理を表すリストを作る.
"""
#定理を表す集合とリスト.
#形式はTheoremSets1が[定理の名前,{前提条件の文字列の集合},{結論の文字列の集合}]
#TheoremLists1が[定理の名前,[前提条件の文字列のリスト],[結論の文字列のリスト]]
TheoremSets1 = []
TheoremLists1 = []
#CSVの形式は第一列に定理の名前
#第二列から第八列に前提条件の文字列
#第九列から改行までが結論の文字列
#空欄は数字で埋める
with open("TopologyGadget1.csv") as filename:
    f = csv.reader(filename,delimiter = ',',lineterminator = 'n')
    numberString = ['1','2','3','4','5','6','7']
    for row in f:
        theoremname = row[0]
        premiseString = []
        conclusionString = []
        premiseSet = set()
        conclusionSet = set()
        for i in range(6):
            string1 = row[i+1]
            boolean1 = False
            for j in range(7):
                if string1 == numberString[j]:
                    boolean1 = True
            if boolean1 == False:
                premiseString.append(string1)
                premiseSet.add(string1)
                
        for i in range(6):
            string2 = row[i+8]
            boolean2 = False
            for j in range(7):
                if string2 == numberString[j]:
                    boolean2 = True
            if boolean2 == False:
                conclusionString.append(string2)
                conclusionSet.add(string2)
                
        listA = [theoremname,premiseString,conclusionString]
        TheoremLists1.append(listA)
        
        listB = [theoremname,premiseSet,conclusionSet]
        TheoremSets1.append(listB)
            
        
"""
リストからキーの添え字を取り出す
"""
def takeIndex(list1,search_key):
    for i in range(len(list1)):
        if list1[i] == search_key:
            return(i)
"""
「定理を適用」ボタンにつけるコマンド.結論側のチェックから定理を適用し,
新しいチェックをつける.
"""
def takeCondition():
    # 結論側のチェックの入った定理の名前を格納する集合
    condition_names = set()
    for i in range(len(SpaceName)):
        bool1 = booleans2[i].get()
        if bool1:
            condition_names.add(SpaceName[i])
    #　定理を適用した後にチェックの入る定理のSpaceNameの番号を格納する.
    conclusion_numbers = []
    # まずTheoremSets1を順番に見ていく.
    # 定理の前提条件の集合がチェックの入った集合に含まれているなら処理を開始
    for j in range(len(TheoremSets1)):
        theorem1 = TheoremSets1[j]
        if theorem1[1] <= condition_names:
            list1 = TheoremLists1[j]
            #定理の前提を表す文字列と結論を表す文字列を作る.
            #この文字列はtextboxに出力される.
            premiseString = ''
            for k in range(len(list1[1])):
                premiseString1 = list1[1][k]
                premiseString = premiseString + premiseString1 + '\n'
            conclusionString = ''
            for k in range(len(list1[2])):
                conclusionString = conclusionString + list1[2][k] + '\n'
            
            #textboxに出力される文字列の生成と表示
            # 前提 ===> （改行）　結論の形式で生成される.
            string1 = premiseString + " ====> \n" + conclusionString 
            txt.insert(tkinter.END,string1)
            string2 = '------------------------ \n'
            txt.insert(tkinter.END,string2)
            #定理を適用したときに得られる結論の番号をconclusion_numbersに格納
            for k in range(len(list1[2])):
                spacename_number = takeIndex(SpaceName,list1[2][k])
                conclusion_numbers.append(spacename_number)
                
                
    
        #conclusion_numbersに格納された結論のチェックを有効にする.      
        for l in range(len(SpaceName)):
            for s in range(len(conclusion_numbers)):
                if l == conclusion_numbers[s]:
                    booleans2[l].set(True)
                
        
"""
「前提入力完了」につけるコマンド.前提のチェックボックスに入ったチェックを
結論にコピーする
"""           
def checkFirst():
    for i in range(len(SpaceName)):
        bool1 = booleans[i].get()
        if bool1:
            booleans2[i].set(True)
            
"""
「リセット」につけるコマンド.前提と結論のすべてのチェックをクリアする.
"""
def resetAll():
    for i in range(len(SpaceName)):
        booleans[i].set(False)
        booleans2[i].set(False)
    txt.delete("1.0","end")
#以下は画面の生成
tki = tkinter.Tk()

tki.geometry('900x700')

tki.title('check button')

label1 = tkinter.Label(tki,text = 'premise')
label1.place(x = 50,y = 30)
label2 = tkinter.Label(tki,text = 'conclusion')
label2.place(x = 300,y = 30)



booleans = [0]* len(SpaceName)
for i in range(len(SpaceName)):
    booleans[i] = tkinter.BooleanVar()
    booleans[i].set(False)
    chk = tkinter.Checkbutton(tki,variable = booleans[i],text = SpaceName[i])
    chk.place(x = 50,y = 30 + (i+1)*24)
    
booleans2 = [0]*len(SpaceName)
for i in range(len(SpaceName)):
    booleans2[i] = tkinter.BooleanVar()
    booleans2[i].set(False)
    chk = tkinter.Checkbutton(tki,variable = booleans2[i],text = SpaceName[i])
    chk.place(x = 300,y = 30 + 24*(i+1))
    
btn = tkinter.Button(tki,text = '定理を適用',command = takeCondition)
btn.place(x = 200,y = 600)

btn2 = tkinter.Button(tki,text = '前提入力完了',command = checkFirst)
btn2.place(x = 50,y = 600)

btn3 = tkinter.Button(tki,text = 'リセット',command = resetAll)
btn3.place(x = 300,y = 600 )

txt = scrolledtext.ScrolledText(tki,width = 50,height = 20)
txt.place(x = 500,y = 30)


tki.mainloop()