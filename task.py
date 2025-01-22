def calculate_love_score(name1,name2):
    result=name1+name2
    tcount=0
    rcount=0
    ucount=0
    ecount=0
    totalTrue=0
    for char in result:
        if(char=='t' or char=='T'):
            tcount+=1
        elif(char=='r' or char=='R'):
            rcount+=1
        elif(char=='u' or char=='U'):
            ucount+=1
        elif(char=='e' or char=='E'):
            ecount+=1
        else:
            totalTrue=0
    print(f"T occurs {tcount} times")  
    print(f"R occurs {rcount} times")  
    print(f"U occurs {ucount} times")  
    print(f"E occurs {ecount} times")  
    totalTrue=tcount+rcount+ucount+ecount
    print(f"Total = {totalTrue}")

    lcount=0
    ocount=0
    vcount=0
    ecount=0
    for char in result:
        if(char=='l' or char=='L'):
            lcount+=1
        elif(char=='o' or char=='O'):
            ocount+=1
        elif(char=='v' or char=='V'):
            vcount+=1
        elif(char=='e' or char=='E'):
            ecount+=1
        else:
            totalLove=0
    print(f"L occurs {lcount} times")  
    print(f"O occurs {ocount} times")  
    print(f"V occurs {vcount} times")  
    print(f"E occurs {ecount} times")  
    totalLove=lcount+ocount+vcount+ecount
    print(f"Total = {totalLove}")
    print(f"Love score = {totalTrue}{totalLove}")

name1=input('Enter name1: ')
name2=input('Enter name2: ')
calculate_love_score(name1,name2)





