list=[{'beijing':{'mianji':'100pm','renkou':'200'},'shanghai':{'mianji':'150pm','renkou':'200'}}]
for i in list:
    for a,b in i.items():
        for c,d in b.items():
            print(a,c,d)
